// Code credit to stack overflow
document.body.scrollTop = document.documentElement.scrollTop = 0;

const scrollFadeIn = document.querySelectorAll('.fade-in');
const presentYear = document.getElementById('current-year');

let today = new Date().getFullYear();
presentYear.innerHTML = today;

const fadeOptions = {
    threshold: 0.01
};

const visibleOnScroll = new IntersectionObserver(function(
    entries, visibleOnScroll) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('scrolled');
                visibleOnScroll.unobserve(entry.target);
            }
        })
    }, fadeOptions);

scrollFadeIn.forEach(fade => {
    visibleOnScroll.observe(fade);
})