import { mapManager } from "./mapManager.js";
import { spriteManager } from "./spriteManager.js";
import { gameManager } from "./gameManager.js";
import { Enemy } from "./entities.js";

export let  physicManager = {

    update: function (obj) {
        if (obj.movex === 0 && obj.movey === 0){
            return "stop";
        }
        let newX = obj.pos_x + Math.floor(obj.movex * obj.speed)
        let newY = obj.pos_y + Math.floor(obj.movey * obj.speed)
        //console.log(newX + " " + newY);
        let ts = mapManager.getTilesetIdx(newX, newY,gameManager.level);
        let e = this.entityAtXY(obj, newX, newY);
        //console.log(mapManager.tLayer[gameManager.level]);
        //console.log(ts);

        let checker = true;
        for (let i = 1;i < ts.length;i++){
            if (ts[i] != 0) {
                checker = false;
                break;
            }
        }
        if (e !== null)
            obj.onTouchEntity(e)
        if (ts[0]!=1365 && ts[0] != 1462 && 0 < newX < 1600 && 0 < newY < 992 && checker) {
            obj.pos_x = newX
            obj.pos_y = newY
        } else {
            console.log('врезался');
            return "break"
        }
        return "move"
    },

    entityAtXY: function(obj, x, y) {
        for (let i = 0; i < gameManager.entities[gameManager.level].length; i++) {
            let e = gameManager.entities[gameManager.level][i];
            if (e.name !== obj.name) {
                if (Math.abs(e.pos_x - obj.pos_x) < 32 && Math.abs(e.pos_y - obj.pos_y) < 32){
                    return e
                }
            }
        }
        return null
    },

    updateEnemies : function(obj) {
        let playerX = gameManager.player[gameManager.level].pos_x;
        let playerY = gameManager.player[gameManager.level].pos_y;
        if (Math.sqrt((obj.pos_x - playerX) * (obj.pos_x - playerX) + (obj.pos_y - playerY) * (obj.pos_y - playerY)) < 100){
            if((obj.pos_x - playerX) < 0) obj.movex = 1;
            else obj.movex = -1;
            if ((obj.pos_y - playerY) < 0) obj.movey = 1;
            else obj.movey = -1;
            if (Math.sqrt((obj.pos_x - playerX) * (obj.pos_x - playerX) + (obj.pos_y - playerY) * (obj.pos_y - playerY)) < 5){
                obj.attack(gameManager.player[gameManager.level]);
            }
        }
        else{
            if (obj.pointerX != null && obj.pointerY != null){
                if (Math.abs(obj.pos_x - obj.pointerX) > 10 && Math.abs(obj.pos_y - obj.pointerY) > 10){
                    if (obj.pos_x - obj.pointerX < 0) obj.movex = 1;
                    else obj.movex = -1;
                    if ((obj.pos_y - obj.pointerY) < 0) obj.movey = 1;
                    else obj.movey = -1;
                }
                else {
                    obj.pointerX = Math.abs(Math.floor(Math.random() * (mapManager.mapSize[gameManager.level].x * 32 + 1)));
                    obj.pointerY = Math.abs(Math.floor(Math.random() * (mapManager.mapSize[gameManager.level].y * 32 + 1)));
                }
            }
            else {
                obj.pointerX = Math.abs(Math.floor(Math.random() * (mapManager.mapSize[gameManager.level].x * 32 + 1)));
                obj.pointerY = Math.abs(Math.floor(Math.random() * (mapManager.mapSize[gameManager.level].y * 32 + 1)));
            }
        }
        let newX = obj.pos_x + Math.floor(obj.movex * obj.speed);
        let newY = obj.pos_y + Math.floor(obj.movey * obj.speed);
        obj.pos_x = newX;
        obj.pos_y = newY;
        return "move";
    },
    checker : function(obj){
        for (let i = 0;i < gameManager.entities[gameManager.level].length; i++){
            if (gameManager.entities[gameManager.level][i].attackTime && gameManager.entities[gameManager.level][i].health <= 0 ) {
                gameManager.entities[gameManager.level][i].kill();
                gameManager.player[gameManager.level].money +=100;
            } 
            console.log(gameManager.entities[gameManager.level][i].health);
        }
    },
    attackEnemies : function(x,y,type) {
        if (gameManager.player[gameManager.level].stock > 0){
            if (type == 0){
                for (let i = 0;i < gameManager.entities[gameManager.level].length; i++){
                    if (gameManager.entities[gameManager.level][i].attackTime) {
                        if (Math.abs(x-gameManager.entities[gameManager.level][i].pos_x) < 32 && Math.abs(y - gameManager.entities[gameManager.level][i].pos_y)< 32 ){
                            gameManager.player[gameManager.level].stock -= 1;
                            gameManager.entities[gameManager.level][i].health -= gameManager.player[gameManager.level].damage;
                            console.log("hit");
                            this.checker(gameManager.entities[gameManager.level][i]);
                            return
                        }
                    }
                }
                let obj = Object.create(gameManager.factory['tool']); 
                gameManager.player[gameManager.level].stock -= 1;
                obj.name= "arrow";
                obj.pos_x = x;
                obj.pos_y = y;
                gameManager.entities[gameManager.level].push(obj);
            }
            else{
                gameManager.player[gameManager.level].manaPoint -= 25;
                for (let i = 0;i < gameManager.entities[gameManager.level].length; i++){
                    if (gameManager.entities[gameManager.level][i].attackTime) {
                        if (Math.abs(x-gameManager.entities[gameManager.level][i].pos_x) < 32 && Math.abs(y - gameManager.entities[gameManager.level][i].pos_y)< 32 ){
                            gameManager.player[gameManager.level].stock -= 1;
                            gameManager.entities[gameManager.level][i].health -= gameManager.player[gameManager.level].superAttack;
                            this.checker(gameManager.entities[gameManager.level][i]);
                            console.log("hit");
                            return
                        }
                    }
                }
                let obj = Object.create(gameManager.factory['tool']); 
                gameManager.player[gameManager.level].stock -= 1;
                obj.name= "arrow";
                obj.pos_x = x;
                obj.pos_y = y;
                gameManager.entities[gameManager.level].push(obj);
                
            }
            
        }
        
    }
}