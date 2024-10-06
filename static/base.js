window.onscroll = function() { // event listener for scroll events.
    let navbar = document.getElementById('nav-bar'); 
    let offset = 40;
    // document.body.scrollTop = how much the page has been scrolled, document.documentElement.scrollTop does the same for root element (important for cross compatibility)
    if (document.body.scrollTop > offset || document.documentElement.scrollTop > offset) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
};