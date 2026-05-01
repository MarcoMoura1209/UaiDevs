class FeedbackCarrosel {
    constructor() {
        this.currentIndex = 0;
        this.cards = document.querySelectorAll('.feedback-card');
        this.indicators = document.querySelectorAll('.indicador');
        this.totalSlides = this.cards.length;

        this.initEventListeners();
    }

    initEventListeners() {
        document.querySelector('.feedback-prev').addEventListener('click', () => this.prev());
        document.querySelector('.feedback-next').addEventListener('click', () => this.next());

        this.indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => this.goToSlide(index));
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
    new FeedbackCarousel();
});