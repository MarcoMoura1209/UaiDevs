@echo off
REM Script para executar testes com DEBUG=True (Windows)
REM Uso: run_tests_with_debug.bat

echo.
echo =========================================================
echo  RODANDO TESTES DE CSP HEADER COM DEBUG=True
echo =========================================================
echo.

REM Define DEBUG=True para session
set DJANGO_SETTINGS_MODULE=UaiDevs.settings.local

REM Roda testes de CSP com verbosidade máxima
python manage.py test core.tests.test_security_core.CspHeaderTest --verbosity=2

echo.
echo =========================================================
echo  TESTES CONCLUIDOS
echo =========================================================
echo.
pause
