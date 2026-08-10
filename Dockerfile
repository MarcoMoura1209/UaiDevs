# syntax=docker/dockerfile:1

# Build-time layer: keep dependency installation separate from the source tree
# so pip wheel/cache can be reused whenever requirements change only.
FROM python:3.14-slim-bookworm AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Compile/runtime headers needed for binary extensions such as psycopg2.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only the dependency declaration first. This is the cache-friendly layer:
# Docker can reuse the image layer whenever requirements.txt does not change.
COPY requirements.txt ./

# Create a virtualenv so the runtime image can copy the installed packages cleanly.
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip setuptools wheel \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy project files after dependencies have been installed. This minimizes build
# invalidation and keeps the dependency install step deterministic.
COPY . .

# Production static assets are collected during the build, reducing runtime work.
RUN DJANGO_SETTINGS_MODULE=UaiDevs.settings.production \
    SECRET_KEY="docker-build-placeholder" \
    DB_NAME="postgres" \
    DB_USER="postgres" \
    DB_PASSWORD="postgres" \
    DB_HOST="localhost" \
    DB_PORT="5432" \
    ALLOWED_HOSTS="localhost" \
    EMAIL_PASSWORD="dummy" \
    /opt/venv/bin/python manage.py collectstatic --noinput --clear

# Runtime stage: keep only the minimal Python runtime and app files.
FROM python:3.14-slim-bookworm AS final

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=UaiDevs.settings.production \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Install only the shared runtime libraries that the wheel-based PostgreSQL driver needs.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Bring over the dependency environment from the builder stage.
COPY --from=builder /opt/venv /opt/venv

# Bring over the application and static artifacts.
COPY --from=builder /app /app

# Use a dedicated non-root user for the application process.
RUN addgroup --system django && adduser --system --ingroup django --home /home/django django \
    && chown -R django:django /app /opt/venv

USER django

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "UaiDevs.wsgi:application"]
