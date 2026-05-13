#!/usr/bin/env python
"""
Script para rodar testes de CSP Header com DEBUG=True

Uso:
    python run_csp_tests_debug.py

Isso executará apenas os testes de CSP com logging detalhado.
"""
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UaiDevs.settings.local')
    
    django.setup()
    
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=2, interactive=True, keepdb=False)
    
    print("\n" + "="*70)
    print("RODANDO TESTES DE CSP HEADER COM DEBUG=True")
    print(f"DEBUG={settings.DEBUG}")
    print("="*70 + "\n")
    
    failures = test_runner.run_tests(['core.tests.test_security_core.CspHeaderTest'])
    
    sys.exit(bool(failures))
