import logging
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import Form
from django_ratelimit.decorators import ratelimit
from honeypot.decorators import check_honeypot
from django.conf import settings


logger = logging.getLogger('core')

@check_honeypot
@ratelimit(key='ip', rate='10/h', method='POST', block=True)
def home(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                subject='Nova mensagem de contato - MouraWeb',
                message=f'Mensagem personalizada---- A ser definida ----',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['uaidevs.ia@gmail.com'],
            )
            return redirect('core:home')
    else:
        form = Form()

    return render(request, 'core/pages/home.html', context={
        'form': form,
    })


@require_http_methods(["GET"])
def sitemap(request):
    """Gera e serve o sitemap.xml dinamicamente"""
    sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">

    <url>
        <loc>https://uaidevs.com.br/</loc>
        <lastmod>2026-05-27</lastmod>
        <changefreq>monthly</changefreq>
        <priority>1.0</priority>
        <xhtml:link
            rel="alternate"
            hreflang="pt-BR"
            href="https://uaidevs.com.br/"/>
    </url>

</urlset>'''

    return HttpResponse(sitemap_content, content_type='application/xml')


@require_http_methods(["GET"])
def robots(request):
    """Gera e serve o robots.txt dinamicamente"""
    admin_url = getattr(settings, 'ADMIN_URL', 'admin/')
    robots_content = '''User-agent: *
Allow: /

Disallow: /{admin_url}/
Disallow: /static/
Disallow: /media/

Sitemap: https://uaidevs.com.br/sitemap.xml
'''

    return HttpResponse(robots_content, content_type='text/plain')
