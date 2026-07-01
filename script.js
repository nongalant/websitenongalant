function resizeText(){

    document.querySelectorAll(".row").forEach(row => {

        const text = row.querySelector(".fit");


        text.style.transform = "scale(1,1)";


        const rowHeight = row.clientHeight;


        const rect = text.getBoundingClientRect();


        const scaleX =
            (window.innerWidth * 0.995) / rect.width;


        const scaleY =
            rowHeight / rect.height;


        text.style.transform =
            `
            scaleX(${scaleX})
            scaleY(${scaleY})
            `;

    });

}


window.addEventListener("load", resizeText);
window.addEventListener("resize", resizeText);