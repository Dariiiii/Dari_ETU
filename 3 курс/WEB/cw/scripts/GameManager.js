import { eventManager } from "./EventManager.js"
import { mapManager } from "./MapManager.js"
import { spriteManager } from "./SpriteManager.js"
import { soundManager } from "./SoundManager.js"
import { Bonus, Enemy, Player } from "./EntityManager.js"

let canvas = document.getElementById('map')
let ctx = canvas.getContext('2d')

export class GameManager {
    factory = {}//фабрика объектов
    entities = [[], []]//объекты
    player = null
    laterKill = []//отложенное уничтожение объекта
    time = 0
    level = 1
    changeLevelFlag = false

    initPlayer(obj) {
        if (this.level == 2) {
            this.player.posX = obj.posX
            this.player.posY = obj.posY
            this.entities[this.level - 1].push(this.player)
        }
        else {
            this.player = obj
            this.entities[this.level - 1].push(this.player)
        }
    }

    kill(obj) {
        this.laterKill.push(obj)
    }

    update() {
        if (this.player === null)
            return
        if (this.player.hp <= 0)
            this.gameOver();
        this.checkLevel()
        this.player.moveX = 0
        this.player.moveY = 0

        if (eventManager.actions["up"]) {
            this.player.moveY = -1
        }
        if (eventManager.actions["down"]) {
            this.player.moveY = 1
        }
        if (eventManager.actions["left"]) {
            this.player.moveX = -1
        }
        if (eventManager.actions["right"]) {
            this.player.moveX = 1
        }

        this.entities[this.level - 1].forEach((entity) => {
            try {
                entity.update()
            }
            catch (ex) {
            }
        });

        for (let i = 0; i < this.laterKill.length; i++) {
            let idx = this.entities[this.level - 1].indexOf(this.laterKill[i])
            if (idx > -1)
                this.entities[this.level - 1].splice(idx, 1)
        }
        if (gameManager.laterKill.lenght > 0)
            gameManager.laterKill.lenght = 0
        document.getElementById("score").innerText = gameManager.player.money;
        document.getElementById("hp").innerText = gameManager.player.hp;
        document.getElementById("mana").innerText = gameManager.player.mana;
        document.getElementById("key").innerText = gameManager.player.key;
        mapManager.drawBackground(ctx)
        this.draw(ctx)
        mapManager.draw(ctx)
    }

    draw(ctx) {
        if (this.entities[this.level - 1].length === 0) {
            setTimeout(() => { this.draw(ctx) }, 100)
        } else {
            for (let i = 0; i < this.entities[this.level - 1].length; i++) {
                this.entities[this.level - 1][i].draw(ctx)
            }
        }
    }

    loadAll() { 
        mapManager.loadMap('../map1.json')
        spriteManager.loadAtlas('../sprites.json', '../1.png')
        this.factory['player'] = Player
        this.factory['enemy'] = Enemy
        this.factory['bonus'] = Bonus
        mapManager.drawBackground(ctx)
        mapManager.parseEntities()
        this.draw(ctx)
        mapManager.draw(ctx)
        soundManager.init()
        eventManager.setup(canvas)
    }

    play() {
        setInterval(updateWorld, 100);
    }

    checkLevel() {
        if (this.player.posX < 32 && this.player.posY < 6 * 32 && this.player.posY > 4 * 32 && this.level == 1) {
            console.log("lvl 2")
            this.level = 2
            this.newLevel()
        }
        else if (this.player.posX > 29 * 32 && this.player.posY < 6 * 35 && this.player.posY > 4 * 35 && this.level == 2) {
            this.level = 1
            this.changeLevelFlag = true
            this.newLevel()
        }
    }

    newLevel() {
        mapManager.tLayer = []
        mapManager.imgLoadCount = 0
        mapManager.imgLoaded = false
        mapManager.jsonLoaded = false
        if (this.level == 1)
            mapManager.loadMap('../map1.json')
        else {
            mapManager.loadMap('../map2.json')
        }
        mapManager.drawBackground(ctx)
        if (!this.changeLevelFlag)
            mapManager.parseEntities()
        else {
            for (let i = 0; i < gameManager.entities[this.level - 1].length; i++) {
                if (gameManager.entities[this.level - 1][i].name.startsWith("cat")) {
                    if (this.level == 1) {
                        this.player.sprite_name = "cat_right1"
                        this.player.posX = 33
                        this.player.posY = 160
                    }
                    else {
                        this.player.posX = 899
                        this.player.posY = 160
                    }
                    this.entities[this.level - 1][i] = this.player
                }
            }
        }
        this.draw(ctx)
        mapManager.draw(ctx)
    }
    gameOver() {
        localStorage['score'] = this.player.money
        window.location.href = "end.html"
    }
}
function updateWorld() {
    gameManager.update();
}
function run() {
    gameManager.loadAll()
    gameManager.play()
}
export let gameManager = new GameManager()
run()
