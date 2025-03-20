import { mapManager } from "./MapManager.js"
import { gameManager } from "./GameManager.js"

export class PhysicsManager {
    obstacle = ['labyrinth', 'passage']

    update(obj) {
        if (obj.moveX === 0 && obj.moveY === 0)
            return "stop"
        let newX = obj.posX + Math.floor(obj.moveX * obj.speed)
        let newY = obj.posY + Math.floor(obj.moveY * obj.speed)
        let flag = this.check(newX, newY)
        let e = this.entityAtXY(obj, newX, newY)
        if (e !== null) {
            obj.onTouchEntity(e)
        }
        if (flag && (newX >= 0) && (newX < 960) && (newY >= 0) && (newY < 640)) {
            obj.posX = newX
            obj.posY = newY
        }
        else
            return "break"
        return "move"
    }

    entityAtXY(obj, x, y) {
        for (let i = 0; i < gameManager.entities[gameManager.level - 1].length; i++) {
            let e = gameManager.entities[gameManager.level - 1][i];
            if (e.name !== obj.name) {
                if (x + obj.sizeX < e.posX || y + obj.sizeY < e.posY || x > e.posX + e.sizeX || y > e.posY + e.sizeY)
                    continue
                return e
            }
        }
        return null
    }

    firstUpdateEnemies(obj) {
        obj.moveY = 0
        obj.moveX = 0
        let pX = gameManager.player.posX;
        let pY = gameManager.player.posY;
        //если игрок близко бежим к нему
        if (Math.sqrt((obj.posX - pX) * (obj.posX - pX) + (obj.posY - pY) * (obj.posY - pY)) < 128) {
            if ((obj.posX - pX) < 0)
                obj.moveX = 1;
            else
                obj.moveX = -1;
            if ((obj.posY - pY) < 0)
                obj.moveY = 1;
            else
                obj.moveY = -1;
            //если совсем близко то атака
            if (Math.sqrt((obj.posX - pX) * (obj.posX - pX) + (obj.posY - pY) * (obj.posY - pY)) < 8)
                obj.attack(gameManager.player);

        }

        else {
            if (obj.pathX != null && obj.pathY != null) {
                if (Math.abs(obj.posX - obj.pathX) > 8 && Math.abs(obj.posY - obj.pathY) > 8 && obj.flag) {
                    if (obj.posX - obj.pathX < 0)
                        obj.moveX = 1;
                    else
                        obj.moveX = -1;
                    if ((obj.posY - obj.pathY) < 0)
                        obj.moveY = 1;
                    else
                        obj.moveY = -1;
                }
                else {
                    obj.pathX = Math.abs(Math.floor(Math.random() * (mapManager.mapSize.x + 1)));
                    obj.pathY = Math.abs(Math.floor(Math.random() * (mapManager.mapSize.y + 1)));
                }
            }
            else {
                obj.pathX = Math.abs(Math.floor(Math.random() * (mapManager.mapSize.x + 1)));
                obj.pathY = Math.abs(Math.floor(Math.random() * (mapManager.mapSize.y + 1)));
            }
        }
        let newX = obj.posX + Math.floor(obj.moveX * obj.speed);
        let newY = obj.posY + Math.floor(obj.moveY * obj.speed);
        obj.flag = this.check(newX, newY);
        if (obj.flag) {
            obj.posX = newX;
            obj.posY = newY;
            return "move";
        }
        else {
            return "break"
        }

    }

    secondUpdateEnemies(obj) {
        obj.moveY = 0
        obj.moveX = 0
        let pX = gameManager.player.posX;
        let pY = gameManager.player.posY;
        if (Math.sqrt((obj.posX - pX) * (obj.posX - pX) + (obj.posY - pY) * (obj.posY - pY)) < 128) {
            if ((obj.posX - pX) < 0)
                obj.moveX = 1;
            else
                obj.moveX = -1;
            if (Math.sqrt((obj.posX - pX) * (obj.posX - pX) + (obj.posY - pY) * (obj.posY - pY)) < 16)
                obj.attack(gameManager.player);
        }
        else if (obj.pathX != null && obj.flag) {
            if (Math.abs(obj.posX - obj.pathX) > 8) {
                if (obj.posX - obj.pathX < 0)
                    obj.moveX = 1
                else
                    obj.moveX = -1
            }
            else {
                obj.pathX = Math.abs(Math.floor(Math.random() * (mapManager.mapSize.x + 1)))
            }
        }
        else {
            obj.pathX = Math.abs(Math.floor(Math.random() * (mapManager.mapSize.x + 1)))
        }
        let newX = obj.posX + Math.floor(obj.moveX * obj.speed)
        obj.flag = this.check(newX, obj.posY);
        if (obj.flag) {
            obj.posX = newX;
            return "move";
        }
        else {
            return "break"
        }

    }

    check(x, y) {
        let ts = mapManager.getTileIdx(x, y)
        for (let i = 0; i < ts.length; i++) {
            if (this.obstacle.includes(ts[i])) {
                return false
            }
        }
        return true
    }

    attackEnemies(x, y) {
        if (gameManager.player.mana >= 20) {
            gameManager.player.mana -= gameManager.player.damage;
            for (let i = 0; i < gameManager.entities[gameManager.level - 1].length; i++) {
                if (Math.abs(x - gameManager.entities[gameManager.level - 1][i].posX) < 32 && Math.abs(y - gameManager.entities[gameManager.level - 1][i].posY) < 32) {
                    gameManager.entities[gameManager.level - 1][i].hp -= gameManager.player.damage;
                    if (gameManager.entities[gameManager.level - 1][i].hp <= 0) {
                        gameManager.entities[gameManager.level - 1][i].kill()
                        gameManager.player.money += 1
                    }
                }
            }
            let obj = new gameManager.factory['bonus']
            obj.name = "fireball";
            obj.sprite_name = "fireball";
            obj.posX = x;
            obj.posY = y;
            gameManager.entities[gameManager.level - 1].push(obj);
            setTimeout(() => { obj.kill() }, 3000)
        }
    }
}

export let physicsManager = new PhysicsManager()