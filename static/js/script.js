// To get elements from the templates
const submit = document.getElementsByClassName('submit-btn')[0];
const peopleIcon = document.getElementById('people')
const title = document.getElementById('id_title');
const content = document.getElementById('id_content');
const fave = document.getElementById('fave');
const filter = document.getElementById('filter');
const pressIcon = document.getElementById('press-icon');
const logBtn = document.getElementsByClassName('log-btn')[0];
const logMsg = document.getElementsByClassName('log-msg')[0];
const scrollFadeIn = document.querySelectorAll('.fade-in');
const presentYear = document.getElementById('current-year');

/**
 * Event listener to ensure page loads before the functions
 * are called.
 */
document.addEventListener('DOMContentLoaded', function() {
    // Functions below will only be called if the variables are defined
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

    if (logBtn != undefined) {
        logBtn.addEventListener('click', logClick);
    }
})

/**
 * On hovering over the favorites button on the 
 * index page, the bullhorn icon on the header changes
 * to a heart.
 */
function faveHover() {
    pressIcon.classList.remove('fa-bullhorn');
    pressIcon.classList.add('fa-heart');
}

/**
 * On the mouse leaving the favorites button on the 
 * index page, the heart icon on the header changes
 * back to a bullhorn.
 */
function faveLeave() {
    pressIcon.classList.remove('fa-heart');
    pressIcon.classList.add('fa-bullhorn');
}

/**
 * On hovering over the search button on the 
 * index page, the bullhorn icon on the header changes
 * to a magnifying lass.
 */
function filterHover() {
    pressIcon.classList.remove('fa-bullhorn');
    pressIcon.classList.add('fa-magnifying-glass');
}

/**
 * On the mouse leaving the search button on the 
 * index page, the magnifying icon on the header changes
 * back to a bullhorn.
 */
function filterLeave() {
    pressIcon.classList.remove('fa-magnifying-glass');
    pressIcon.classList.add('fa-bullhorn');
}

/**
 * When the submit button is clicked, an alert will pop up
 * alerting the user which inputs on the article form need to be 
 * filled. 
 */
function submitCheck() {
    if (title.value.length == 0) {
        alert('The article needs a title!');
    }
    else if (content.value.length == 0) {
        alert('The article needs content!');
    }
}

/**
 * When the log in, sign up or log out buttons are clicked
 * a spinner will be revealed with a loading message.
 */
function logClick() {
    logMsg.classList.remove('visually-hidden');
    
}

// Sets the year on the footer to the present year
let today = new Date().getFullYear();
presentYear.innerHTML = today;

// Sets how much of the elements need to be visible 
let fadeOptions = {
    threshold: 0.1
};

/**
 * Triggers the animation effect when the selected
 * elements are visible to the user using an 
 * intersection observer API.
 * List of entries and visibleOnScroll (intersection 
 * observer) variable taken as parameters.
 * Ends the function if entry is not intersecting.
 * Returns True if entry is intersecting and stops 
 * observing that entry after the animation is in effect.
 */
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
