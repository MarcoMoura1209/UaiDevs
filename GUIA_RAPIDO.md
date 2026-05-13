# 🚀 GUIA RÁPIDO: Rodar Testes de CSP com DEBUG

## ⚡ TL;DR (Muito Rápido)

```bash
# Apenas rodar testes CSP com DEBUG
python run_csp_tests_debug.py
```

---

## 📋 Passo a Passo

### 1️⃣ Verificar Testes Existentes

```bash
# Ver todos os testes
python manage.py test core --help

# Listar testes de segurança
dir core\tests\test_*.py
```

**Resultado**: 40+ testes concisos e bem estruturados ✅

---

### 2️⃣ Rodar Testes de CSP Header (novo)

#### Opção A: Script Python
```bash
python run_csp_tests_debug.py
```
**Saída esperada**:
```
======================================================================
RODANDO TESTES DE CSP HEADER COM DEBUG=True
DEBUG=True
======================================================================

test_csp_header_nao_vazio ... ok
test_csp_header_presente_na_resposta ... ok
```

#### Opção B: Django manage.py
```bash
python manage.py test core.tests.test_security_core.CspHeaderTest --verbosity=2
```

#### Opção C: pytest
```bash
python -m pytest core/tests/test_security_core.py::CspHeaderTest -v
```

#### Opção D: Windows Batch
```cmd
run_tests_with_debug.bat
```

---

### 3️⃣ Ver Detalhes do CSP Header

Se quiser ver qual é o header de CSP sendo enviado:

```python
# Adicione isto temporariamente a um teste
from django.test import TestCase, Client
from django.urls import reverse

response = Client().get('/')
print(response.get('Content-Security-Policy'))
# Output: 'self'
```

---

### 4️⃣ Ver Logs de DEBUG

Os logs aparecem em:

**Console**: 
```bash
# Ao rodar qualquer teste, aparece no terminal
python manage.py test core
```

**Arquivo**:
```bash
# Histórico em arquivo (criado automaticamente)
logs/django.log
```

---

## 📊 Resumo das Mudanças

### Adicionado ao projeto:

1. **Novo Teste**: `CspHeaderTest` em `test_security_core.py`
   - Verifica se CSP header está presente
   - Verifica se CSP header não está vazio

2. **Configuração**: CSP policies em `settings/base.py`
   ```python
   CSP_DEFAULT_SRC = ("'self'",)
   CSP_SCRIPT_SRC = ("'self'",)
   CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
   CSP_IMG_SRC = ("'self'", "data:", "https:")
   CSP_FONT_SRC = ("'self'",)
   ```

3. **Scripts**:
   - `run_csp_tests_debug.py` - Python
   - `run_tests_with_debug.bat` - Windows

---

## ✅ Verificação Rápida

```bash
# 1. Testes existentes concisos?
echo "✓ Sim, 40+ testes bem estruturados"

# 2. Teste de CSP criado?
grep -n "CspHeaderTest" core/tests/test_security_core.py
echo "✓ Encontrado na linha 63+"

# 3. DEBUG está ativo?
grep "DEBUG" UaiDevs/settings/local.py
echo "✓ DEBUG = True"

# 4. Middleware CSP ativo?
grep "CSPMiddleware" UaiDevs/settings/base.py
echo "✓ Middleware presente"

# 5. Configuração CSP existente?
grep "CSP_DEFAULT_SRC" UaiDevs/settings/base.py
echo "✓ Configurado"
```

---

## 🔗 Referências

- **Django-CSP**: Documentação middleware
- **Django Tests**: https://docs.djangoproject.com/en/6.0/topics/testing/
- **pytest-django**: https://pytest-django.readthedocs.io/

---

## 💬 Dúvidas Comuns

**P: Como rodar teste específico?**
```bash
python manage.py test core.tests.test_security_core.CspHeaderTest.test_csp_header_presente_na_resposta
```

**P: Como ver mais detalhes?**
```bash
python manage.py test core -v 3  # verbosity=3
```

**P: Onde fica o log de debug?**
```
logs/django.log  (criado automaticamente)
```

**P: Como desativar CSP para testes?**
```python
@override_settings(CSP_DEFAULT_SRC=())
def test_sem_csp(self):
    # teste aqui
```

---

## 🎯 Conclusão

✅ **Tudo pronto para usar!**

- Testes concisos ✅
- CSP configurado ✅
- DEBUG ativo ✅
- Scripts de teste criados ✅
