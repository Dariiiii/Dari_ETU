import { soundManager } from "./soundManager.js";

function lastScreen(){
    soundManager.init();
    console.log("hello");
    let result = JSON.parse(localStorage.getItem('result'))
    if (result == false) {
        console.log("yes");   
        soundManager.play("/sounds/pobeda.mp3");
    }
    else {
        console.log("no");
        soundManager.play("/sounds/lose.mp3");
    }
    const canvas = document.getElementById('game_over');
    const context = canvas.getContext('2d');
    context.font = '25px Caveat';
    let score_table = JSON.parse(localStorage.getItem('game')) || [];
    let i = 0;
    while (score_table[i] !== undefined && i < 20) {
        context.fillText(score_table[i].place +' место : ' + score_table[i].value + ' очков,  игрок ' + score_table[i].player + ';',0,(i + 1) * 25);
        i++;
    }
}

lastScreen();