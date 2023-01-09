document.addEventListener('DOMContentLoaded', function() {
    const submit = document.getElementsByClassName('submit-btn');
    const title = document.getElementById('id_title');
    const content = document.getElementById('id_content');
    submit[0].addEventListener('click', submitCheck);
    submit[1].addEventListener('click', submitCheck)


    function submitCheck() {
        if (title.value.length == 0) {
            alert('You need a title!')
        }
        else if (content.value.length == 0) {
            alert('The article needs content!')
        }
    }
})

const scrollFadeIn = document.querySelectorAll('.fade-in');
const presentYear = document.getElementById('current-year');

let today = new Date().getFullYear();
presentYear.innerHTML = today;

const fadeOptions = {
    threshold: 0.1
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