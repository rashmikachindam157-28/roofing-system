// PAGE LOADING ANIMATION

window.addEventListener("load", function(){

document.body.style.opacity = "1";

});



// NAVBAR SCROLL EFFECT

window.addEventListener("scroll", function(){

const navbar = document.querySelector(".navbar");

if(window.scrollY > 50){

navbar.style.background = "rgba(0,0,0,0.8)";
navbar.style.backdropFilter = "blur(10px)";

}

else{

navbar.style.background = "rgba(255,255,255,0.05)";

}

});




// BUTTON CLICK ANIMATION

const buttons = document.querySelectorAll("button");

buttons.forEach(btn => {

btn.addEventListener("click", function(){

btn.style.transform = "scale(0.9)";

setTimeout(()=>{

btn.style.transform = "scale(1)";

},150);

});

});




// SERVICE CARD HOVER EFFECT

const cards = document.querySelectorAll(".service-card");

cards.forEach(card => {

card.addEventListener("mouseenter", () => {

card.style.transform = "translateY(-10px) scale(1.03)";

});

card.addEventListener("mouseleave", () => {

card.style.transform = "translateY(0) scale(1)";

});

});




// GALLERY IMAGE ZOOM

const images = document.querySelectorAll(".gallery-container img");

images.forEach(img => {

img.addEventListener("mouseenter", () => {

img.style.transform = "scale(1.1)";

});

img.addEventListener("mouseleave", () => {

img.style.transform = "scale(1)";

});

});




// FORM VALIDATION

const form = document.querySelector("form");

if(form){

form.addEventListener("submit", function(e){

const name = document.querySelector("input[name='name']").value;
const phone = document.querySelector("input[name='phone']").value;

if(name.length < 3){

alert("Please enter a valid name");
e.preventDefault();

}

if(phone.length < 10){

alert("Please enter a valid phone number");
e.preventDefault();

}

});

}




// SMOOTH SCROLL FOR NAV LINKS

document.querySelectorAll("a").forEach(anchor => {

anchor.addEventListener("click", function(e){

const target = document.querySelector(this.getAttribute("href"));

if(target){

e.preventDefault();

target.scrollIntoView({

behavior: "smooth"

});

}

});

});