import { mobileRender } from "./mobile.js";

let playSound = false;
const audio = document.getElementById('audio_track');
audio.volume = 0.2;

document.body.addEventListener('click', () => {
    audio.play();
})

document.getElementById('header__sound').addEventListener('click', () => {
    playSound = document.getElementById('header__sound').checked;
    audio.volume = playSound ? 0.2 : 0;
})

mobileRender();