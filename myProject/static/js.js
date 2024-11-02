window.addEventListener('scroll', function() {
    const infoElements = document.querySelectorAll('.info');
    const navbar = document.querySelector('.navbar');
    const navbarHeight = navbar.offsetHeight;

    infoElements.forEach(function(infoElement) {
        const rect = infoElement.getBoundingClientRect();
        const elementTop = rect.top; 
        
        if (elementTop < navbarHeight) {
            const fadePercentage = Math.min((navbarHeight - elementTop) / navbarHeight, 1);
            infoElement.style.opacity = 1 - fadePercentage; 
        } else {
            infoElement.style.opacity = 1; 
        }
    });
});
