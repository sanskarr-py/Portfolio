const reveals = document.querySelectorAll(".reveal");

function revealSections() {

    const windowHeight = window.innerHeight;

    reveals.forEach(section => {

        const top = section.getBoundingClientRect().top;

        if(top < windowHeight - 120){

            section.classList.add("active");

        }

    });

}

window.addEventListener("scroll", revealSections);

revealSections();

