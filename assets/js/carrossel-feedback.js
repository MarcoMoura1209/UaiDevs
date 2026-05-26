class FeedbackCarrossel {
    constructor() {
        this.currentIndex = 0;
        this.cards = document.querySelectorAll('.feedback-card');
        this.indicators = document.querySelectorAll('.indicador');
        this.totalSlides = this.cards.length;
        this.carrossel = document.querySelector('.carrossel-feedback');

        this.initEventListeners();
        this.initAriaAttributes();
    }

    initAriaAttributes() {
        // Adicionar aria-live para anúncios de mudança de slide
        this.carrossel.setAttribute('aria-live', 'polite');
        this.carrossel.setAttribute('aria-atomic', 'true');
        
        // Definir aria-current para o slide ativo
        this.cards.forEach((card, index) => {
            card.setAttribute('role', 'tabpanel');
            card.setAttribute('aria-labelledby', `feedback-${index}`);
        });

        this.indicators.forEach((indicator, index) => {
            indicator.setAttribute('role', 'tab');
            indicator.setAttribute('aria-label', `Ir para feedback ${index + 1}`);
            indicator.setAttribute('tabindex', index === 0 ? '0' : '-1');
            indicator.setAttribute('aria-selected', index === 0 ? 'true' : 'false');
        });
    }

    initEventListeners() {
        document.querySelector('.feedback-prev').addEventListener('click', () => this.prev());
        document.querySelector('.feedback-next').addEventListener('click', () => this.next());

        this.indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => this.goToSlide(index));
            indicator.addEventListener('keydown', (e) => {
                if (e.key === 'ArrowRight' && index < this.totalSlides - 1) {
                    this.goToSlide(index + 1);
                    this.indicators[index + 1].focus();
                } else if (e.key === 'ArrowLeft' && index > 0) {
                    this.goToSlide(index - 1);
                    this.indicators[index - 1].focus();
                }
            });
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') this.prev();
            if (e.key === 'ArrowRight') this.next();
        });
    }

    showSlide(index) {
        this.cards.forEach(card => card.classList.remove('active'));
        this.indicators.forEach(ind => ind.classList.remove('active'));

        this.cards[index].classList.add('active');
        this.indicators[index].classList.add('active');

        // Atualizar aria attributes
        this.indicators.forEach((indicator, i) => {
            indicator.setAttribute('aria-selected', i === index ? 'true' : 'false');
            indicator.setAttribute('tabindex', i === index ? '0' : '-1');
        });

        this.currentIndex = index;
    }

    next() {
        const nextIndex = (this.currentIndex + 1) % this.totalSlides;
        this.showSlide(nextIndex);
    }

    prev() {
        const prevIndex = (this.currentIndex - 1 + this.totalSlides) % this.totalSlides;
        this.showSlide(prevIndex);
    }

    goToSlide(index) {
        this.showSlide(index);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new FeedbackCarrossel();
});