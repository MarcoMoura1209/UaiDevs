const botao = document.getElementById('menu-toggle');
const nav = document.getElementById('nav-menu');

botao.addEventListener('click', function() {
    nav.classList.toggle('nav-aberta');
    
    // Atualizar aria-expanded para acessibilidade
    const isExpanded = botao.getAttribute('aria-expanded') === 'true';
    botao.setAttribute('aria-expanded', !isExpanded);
    
    // Atualizar aria-hidden do menu
    nav.setAttribute('aria-hidden', isExpanded);
});

// Fechar menu quando um link é clicado
const links = nav.querySelectorAll('a');
links.forEach(link => {
    link.addEventListener('click', function() {
        nav.classList.remove('nav-aberta');
        botao.setAttribute('aria-expanded', 'false');
        nav.setAttribute('aria-hidden', 'true');
    });
});