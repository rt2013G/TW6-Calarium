window.onload = () => {
    'use strict';
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('../static/pwa/sw.js').then(function (registration) {
    }, function (err) {
            console.log('service worker registration failed', err);
        });
    }
}

import { mobileRender } from "./mobile.js";

let playSound = false;
const audio = document.getElementById('audio_track');
audio.volume = 0.2;

document.body.addEventListener('click', () => {
    audio.play();
})

const soundToggle = document.getElementById('header__sound');
if(soundToggle) {
    soundToggle.addEventListener('click', () => {
    playSound = document.getElementById('header__sound').checked;
    audio.volume = playSound ? 0.2 : 0;
})}

let menu = true;
const burgerMenu = document.querySelector('.header__menu');
if(burgerMenu) {
    burgerMenu.addEventListener('click', () => {
    menu = !menu;
    if(menu) {
        $('.navigator').show()
    } else {
        $('.navigator').hide();
    }
})}

mobileRender();
