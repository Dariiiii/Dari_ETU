import {spriteManager} from "./SpriteManager.js"
import {physicsManager} from "./PhisycsManager.js"
import {gameManager} from "./GameManager.js"
import {soundManager} from "./SoundManager.js";
export class Entity{
    posX = 0
    posY = 0
    sizeX = 0
    sizeY = 0
    name = ''
    spriteName = ''
    kill(){
        gameManager.laterKill.push(this)
    }
}

export class Player extends Entity{
    speed = 5
    level = 1
    moveX = 0
    moveY = 0
    HP = 1
    score = 0
    spriteName = "player_down"
    constructor() {
        super()
        if (localStorage["speed"] !== undefined)
            this.speed = Number(localStorage["speed"])
    }
    onTouchEntity(obj){
        switch (obj.name){
            case "bonus":
                this.score += 1
                obj.kill()
                soundManager.play("../sounds/bonus.mp3", {looping: false, volume: 1})
                break
            case "speed":
                this.speed += 5
                obj.kill()
                soundManager.play("../sounds/apple.mp3", {looping: false, volume: 1})
                break
        }
    }

    draw(ctx){
        spriteManager.drawSprite(ctx, this.spriteName, this.posX, this.posY)

    }

    update(){
        physicsManager.update(this)
        if (this.HP < 1){
            this.kill()
            setTimeout(() => {gameManager.gameOver('death')}, 200)
            //gameManager.gameOver('death')
        }
        this.spriteUpdate()
    }



    spriteUpdate(){
        if (this.moveX === 1) {
            this.spriteName = 'player_right'
        } else if(this.moveX === -1){
            this.spriteName = 'player_left'
        } else if(this.moveY === 1){
            this.spriteName = 'player_down'
        } else if(this.moveY === -1){
            this.spriteName = 'player_up'
        }
    }
}

export class Zombie extends Entity{
    speed = 5
    moveX = 0
    moveY = 0
    spriteName = "zombie_down"
    draw(ctx){
        spriteManager.drawSprite(ctx, this.spriteName, this.posX, this.posY)
    }

    onTouchEntity(obj){
        if (obj.name === "player" && obj.HP > 0){
            soundManager.play("../sounds/hit.mp3", {looping: false, volume: 1})
            obj.HP -= 1
            console.log(obj.HP)
        }
    }

    update(){

        let x = Math.random()
        if (x < 0.5){
            let x = Math.random()
            if (x < 0.33){
                this.moveX = -1
            }
            else if ((x >= 0.33) && (x < 0.66)){
                this.moveX = -1
            }
            else if (x >= 0.66){
                this.moveX = 1
            }
        }
        else {
            x = Math.random()
            if (x < 0.33){
                this.moveY = -1
            }
            else if ((x >= 0.33) && (x < 0.66)){
                this.moveY = -1
            }
            else if (x >= 0.66){
                this.moveY = 1
            }
        }

        physicsManager.update(this)
        this.spriteUpdate()
    }



    spriteUpdate(){
        if (this.moveX === 1) {
            this.spriteName = 'zombie_right'
        } else if(this.moveX === -1){
            this.spriteName = 'zombie_left'
        } else if(this.moveY === 1){
            this.spriteName = 'zombie_down'
        } else if(this.moveY === -1){
            this.spriteName = 'zombie_up'
        }
    }
}

export class Bonus extends Entity{
    draw(ctx){
        spriteManager.drawSprite(ctx, this.spriteName, this.posX, this.posY)
    }

    update(){
        this.spriteUpdate()
    }



    spriteUpdate(){
        this.spriteName = "bonus"
    }
}

export class Speed extends Entity{
    draw(ctx){
        spriteManager.drawSprite(ctx, this.spriteName, this.posX, this.posY)
    }

    update(){
        this.spriteUpdate()
    }



    spriteUpdate(){
        this.spriteName = "speed"
    }
}
export let entity = new Entity()