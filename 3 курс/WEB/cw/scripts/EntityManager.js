import { spriteManager } from "./SpriteManager.js"
import { physicsManager } from "./PhisycsManager.js"
import { gameManager } from "./GameManager.js"
import { mapManager } from "./MapManager.js"
import { soundManager } from "./SoundManager.js"

export class Entity {
    posX = 0
    posY = 0
    name = ''
    sprite_name = null
    extend(extendProto) {
        let object = Object.create(this);
        for (let property in extendProto) {
            if (this.hasOwnProperty(property) || typeof object[property] === 'undefined') {
                object[property] = extendProto[property];
            }
        }
        return object;
    }
    kill() {
        gameManager.laterKill.push(this)
    }
}

export class Player extends Entity {
    speed = 8
    moveX = 0
    moveY = 0
    hp = 120
    mana = 20
    damage = 20
    money = 0
    key = 0
    sprite_name = 'cat_left1'
    num_sprite = 1
    num_flower = []

    onTouchEntity(obj) {
        switch (obj.sprite_name) {
            case "coin":
                this.money += 1
                obj.kill()
                soundManager.play("../sound/coin.mp3", { looping: false, volume: 1 })
                break
            case "hp_f":
                if (this.hp <= 70) this.hp += 60
                else this.hp = 120
                obj.spriteUpdate()
                soundManager.play("../sound/eat.mp3", { looping: false, volume: 1 })
                break
            case "mana_f":
                this.mana += 60
                obj.spriteUpdate()
                soundManager.play("../sound/eat.mp3", { looping: false, volume: 1 })
                break
            case "button":
                obj.buttonClick(this)
                obj.sprite_name = "null"
                break
            case "pink_flower":
                this.num_flower.push(2)
                obj.sprite_name = "null"
                this.money+=1
                break
            case "blue_flower":
                this.num_flower.push(1)
                obj.sprite_name = "null"
                this.money+=1

                break
            case "red_flower":
                this.num_flower.push(3)
                obj.sprite_name = "null"
                this.money+=1
                break
            case "yellow_flower":
                this.num_flower.push(0)
                obj.sprite_name = "null"
                this.money+=1
                break
            case "box":
                if (this.key == 1) {
                    this.money += 5
                    soundManager.play("../sound/coin.mp3", { looping: false, volume: 1 })
                    obj.kill()
                    this.key = 0
                    gameManager.gameOver()
                }
                break
        }
    }

    spriteUpdate() {
        this.num_sprite = (this.num_sprite + 1) % 3
        if (this.moveX === 1)
            this.sprite_name = 'cat_right' + this.num_sprite
        else if (this.moveX === -1)
            this.sprite_name = 'cat_left' + this.num_sprite
        else if (this.moveY === 1)
            this.sprite_name = 'cat_down' + this.num_sprite
        else if (this.moveY === -1)
            this.sprite_name = 'cat_up' + this.num_sprite
    }

    draw(ctx) {
        this.spriteUpdate()
        spriteManager.drawSprite(ctx, this.sprite_name, this.posX, this.posY)
    }

    update() {
        physicsManager.update(this)
    }
}

export class Enemy extends Entity {
    speed = 1
    moveX = 0
    moveY = 0
    hp = 1
    pathX = null
    pathY = null
    flag = true
    attackTime = new Date()
    draw(ctx) {
        this.spriteUpdate()
        spriteManager.drawSprite(ctx, this.sprite_name, this.posX, this.posY)

    }

    spriteUpdate() {
        this.sprite_name = this.name[0]
        if (this.sprite_name == 'd') {
            this.sprite_name = 'dog'
            if (this.speed == 1 || this.hp == 1) {
                this.speed = 6
                this.hp = 40
            }
        }
        else if (this.sprite_name == 'm') {
            this.sprite_name = 'mouse'
            if (this.speed == 1 || this.hp == 1) {
                this.speed = 7
                this.hp = 20
            }
        }
        if (this.moveX === 1)
            this.sprite_name += '_right'
        else if (this.moveX === -1)
            this.sprite_name += '_left'
        else if (this.moveY === 1)
            this.sprite_name += '_down'
        else if (this.moveY === -1)
            this.sprite_name += '_up'
        else
            this.sprite_name += '_down'
    }

    update() {
        if (gameManager.level == 1)
            physicsManager.firstUpdateEnemies(this)
        else
            physicsManager.secondUpdateEnemies(this)
    }

    attack(player) {
        const time = new Date()
        if (Math.abs(time - this.attackTime) >= 3000) {
            this.attackTime = time;
            let current_damage = this.hp;
            player.hp -= current_damage;
            soundManager.play("../sound/damage.mp3", { looping: false, volume: 1 })
        }
    }
}

export class Bonus extends Entity {
    draw(ctx) {
        if (this.sprite_name === null)
            this.sprite_name = this.name
        if (this.name === "coin" || this.name === "mana_f" || this.name === "hp_f"
            || this.name === "box" || this.name === "button" || this.name === "yellow_flower"
            || this.name === "red_flower" || this.name === "pink_flower"
            || this.name === "blue_flower" || this.sprite_name === "f_false" || this.name === "fireball") {
            spriteManager.drawSprite(ctx, this.sprite_name, this.posX, this.posY);
        }

    }
    spriteUpdate() {
        this.sprite_name = "f_false"
        this.name = "f_false"
    }
    update() { }

    buttonClick(player) {
        if (gameManager.level == 1) {
            this.num_flower = []
            gameManager.entities[gameManager.level - 1][0].sprite_name = "null"
            gameManager.entities[gameManager.level - 1][1].sprite_name = "null"
            gameManager.entities[gameManager.level - 1][2].sprite_name = "null"
            gameManager.entities[gameManager.level - 1][3].sprite_name = "null"
            setTimeout(() => { gameManager.entities[gameManager.level - 1][0].sprite_name = gameManager.entities[gameManager.level - 1][0].name }, 4000)
            setTimeout(() => { gameManager.entities[gameManager.level - 1][1].sprite_name = gameManager.entities[gameManager.level - 1][1].name }, 1000)
            setTimeout(() => { gameManager.entities[gameManager.level - 1][2].sprite_name = gameManager.entities[gameManager.level - 1][2].name }, 2000)
            setTimeout(() => { gameManager.entities[gameManager.level - 1][3].sprite_name = gameManager.entities[gameManager.level - 1][3].name }, 3000)
            player.num_flower = []
            this.buttonGame(player)
        }
        else {
            for (let i = 0; i < mapManager.tLayer.length; i++) {
                if (mapManager.tLayer[i].name == 'labyrinth') {
                    mapManager.tLayer[i].data[223] = 241
                    mapManager.tLayer[i].data[552] = 0
                    this.kill()
                }
            }
        }
    }
    buttonGame(player) {
        if (player.num_flower.length == 4 && this.sprite_name == 'null') {
            for (let i = 0; i < player.num_flower.length; i++) {
                if (player.num_flower[i] != i) {
                    player.key = 0
                    this.sprite_name = this.name
                    break
                }
                else
                    player.key = 1
            }
            if (player.key == 1)
                this.kill()
        }
        else setTimeout(() => { this.buttonGame(player) }, 200)
    }
}
