import logging
from decouple import config
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django_ratelimit.decorators import ratelimit
from honeypot.decorators import check_honeypot
from .forms import Form


logger = logging.getLogger('core')


@check_honeypot
@ratelimit(key='ip', rate='10/h', method='POST', block=True)
def home(request):
    if request.method == 'POST':
        form = Form(request.POST)
        print(request.POST)
        if form.is_valid():
            cliente = form.save()
            logger.info('Formulario valido!!!')
            mensagem_email = (
                f"Nome: {cliente.nome}\n"
                f"Email: {cliente.email}\n"
                f"Telefone: {cliente.telefone}\n"
                f"Empresa: {cliente.empresa}\n\n"
                f"Mensagem:\n{cliente.mensagem}"
            )

            try:
                send_mail(
                    subject='Nova mensagem de contato - UaiDevs',
                    message=mensagem_email,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[config('EMAIL_DEFAULT')],
                )
            except Exception:
                logger.exception(
                    'Erro ao enviar e-mail de contato via send_mail'
                    )

            return redirect('core:home')

        else:
            logger.warning(
                'Formulario invalido. Erros: %s', form.errors.as_json()
                )

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
    robots_content = '''User-agent: *
Allow: /

Disallow: /static/
Disallow: /media/

Sitemap: https://uaidevs.com.br/sitemap.xml
'''

    return HttpResponse(robots_content, content_type='text/plain')
