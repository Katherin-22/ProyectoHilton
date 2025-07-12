    const images = [
        "../../static/img/jhonatan/habitacion1.jpg",
        "../../static/img/jhonatan/habitacion2.jpg",
        "../../static/img/jhonatan/habitacion3.jpg", 
    ];

    let currentIndex = 0;

    function changeBackgroundImage() {
        document.body.style.backgroundImage = `url(${images[currentIndex]})`;

        currentIndex = (currentIndex + 1) % images.length;
    }

    setInterval(changeBackgroundImage, 5000);

    changeBackgroundImage();

