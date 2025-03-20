import {mapManager} from "./MapManager.js"
import {gameManager} from "./GameManager.js"

export class PhysicsManager{
    escape = [594, 595, 597, 598]
    walkZone = [610, 611, 626, 627, 0, 613, 614, 629, 630]
    update(obj){
        if (obj.moveX === 0 && obj.moveY === 0)
            return "stop"

        if (obj.name === "zombie")
            this.pursuit(obj)


        let newX = obj.posX + Math.floor(obj.moveX * obj.speed)
        let newY = obj.posY + Math.floor(obj.moveY * obj.speed)

        let ts = mapManager.getTileId(newX + obj.sizeX / 2, newY + obj.sizeY / 2, 1)

        let e = this.entityAtXY(obj, newX, newY)
        if (e !== null && obj.onTouchEntity){
            obj.onTouchEntity(e)
        }
        if ((this.walkZone.includes(ts)) && (newX >= 0) && (newX < 960) && (newY >= 0) && (newY < 640) && (e === null)) {
            obj.posX = newX
            obj.posY = newY
        } else if ((this.escape.includes(ts)) && (newX >= 0) && (newX < 960) && (newY >= 0) &&
            (newY < 640) && (e === null) && (obj.name === "player") && (gameManager.level === 1) && (obj.score === 4)){
            console.log("NEXT LEVEL")
            gameManager.level = 2
        }
        else {
            return "break"
        }
        return "move"
    }

    entityAtXY(obj, x, y){
        for (let i = 0; i < gameManager.entities.length; i++) {
            let e = gameManager.entities[i];
            if (e.name !== obj.name) {
                if (x + obj.sizeX < e.posX || y + obj.sizeY < e.posY || x > e.posX + e.sizeX || y > e.posY + e.sizeY)
                    continue
                return e
            }
        }
        return null
    }

    pursuit(obj){
        let x = -1, y = -1, moveX, moveY
        let params = [-1, -1, -1, -1]
        for (let i = 0; i < gameManager.entities.length; i++) {
            let e = gameManager.entities[i]
            if (e.name === "player") {
                params[0] = e.posX - (obj.sizeX + obj.posX)
                params[1] = obj.posX - (e.posX + e.sizeX)
                params[2] = e.posY - (obj.posY + obj.sizeY)
                params[3] = obj.posY - (e.posY + e.sizeY)
                break
            }
        }
        if (params[0] >= 0){
            x = params[0]
            moveX = 1
        }
        if (params[1] >= 0){
            x = params[1]
            moveX = -1
        }
        if (params[2] >= 0){
            y = params[2]
            moveY = 1
        }
        if (params[3] >= 0){
            y = params[3]
            moveY = -1
        }
        if ((x + y <= 64) && (x !== -1) && (y !== -1)){
            if (x > y){
                obj.moveY = 0
                obj.moveX = moveX
            }
            else{
                obj.moveX = 0
                obj.moveY = moveY
            }

        }
    }
}

export let physicsManager = new PhysicsManager()