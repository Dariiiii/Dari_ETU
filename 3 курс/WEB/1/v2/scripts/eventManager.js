import { physicManager } from "./physicManager.js"
import { gameManager } from "./gameManager.js"
import { mapManager } from "./mapManager.js";
export let eventManager = {
    bind : [],
    action : [],

    setup : function(canvas){
        this.bind[87] = 'up';
        this.bind[65] = 'left';
        this.bind[83] = 'down';
        this.bind[68] = 'right';
        document.body.addEventListener("keydown", this.onKeyDown)
        document.body.addEventListener("keyup", this.onKeyUp)
        document.body.addEventListener("click", function(event) {
            var x = event.pageX - canvas.offsetLeft;
            var y = event.pageY - canvas.offsetTop;          
            console.log("X: " + x + ", Y: " + y);
            physicManager.attackEnemies(x + mapManager.view.x,y + mapManager.view.y,0);
        });
        canvas.addEventListener("contextmenu", function(event) {
            event.preventDefault();
            var x = event.pageX - canvas.offsetLeft;
            var y = event.pageY - canvas.offsetTop;
            console.log("X: " + x + ", Y: " + y);
            if(gameManager.player[gameManager.level].manaPoint >= 25)
            physicManager.attackEnemies(x + mapManager.view.x,y + mapManager.view.y,1);
        });
    },
    onKeyDown : function(event) {
        let action = eventManager.bind[event.keyCode]
        if (action)
            eventManager.action[action] = true
    },
    onKeyUp: function(event) {
        let action = eventManager.bind[event.keyCode]
        if (action)
            eventManager.action[action] = false
    }
    

}