document.addEventListener('DOMContentLoaded', function() {
    const submit = document.getElementsByClassName('submit-btn')[0];
    const title = document.getElementById('id_title');
    const content = document.getElementById('id_content');
    const fave = document.getElementById('fave');
    const filter = document.getElementById('filter')
    const pressIcon = document.getElementById('press-icon')

    if (fave != undefined) {
        fave.addEventListener('mouseover', faveHover);
        fave.addEventListener('mouseleave', faveLeave);
    }

    if (filter != undefined) {
        filter.addEventListener('mouseover', filterHover);
        filter.addEventListener('mouseleave', filterLeave);
    }

    if (submit != undefined) {
        submit.addEventListener('click', submitCheck);
    }

    function faveHover() {
        pressIcon.classList.remove('fa-bullhorn');
        pressIcon.classList.add('fa-heart');
    }

    function faveLeave() {
        pressIcon.classList.remove('fa-heart');
        pressIcon.classList.add('fa-bullhorn');
    }

    function filterHover() {
        pressIcon.classList.remove('fa-bullhorn');
        pressIcon.classList.add('fa-magnifying-glass');
    }

    function filterLeave() {
        pressIcon.classList.remove('fa-magnifying-glass');
        pressIcon.classList.add('fa-bullhorn');
    }

    function submitCheck() {
        if (title.value.length == 0) {
            alert('The article needs a title!');
        }
        else if (content.value.length == 0) {
            alert('The article needs content!');
        }
    }
})

const scrollFadeIn = document.querySelectorAll('.fade-in');
const presentYear = document.getElementById('current-year');

let today = new Date().getFullYear();
presentYear.innerHTML = today;

let fadeOptions = {
    threshold: 0.1
};

let visibleOnScroll = new IntersectionObserver(function(
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
