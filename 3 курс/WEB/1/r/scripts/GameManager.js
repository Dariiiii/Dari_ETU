import {Zombie} from "./EntityManager.js"
import {Player} from "./EntityManager.js"
import {Bonus} from "./EntityManager.js"
import {Speed} from "./EntityManager.js"
import {eventManager} from "./EventManager.js"
import {mapManager} from "./MapManager.js"
import {soundManager} from "./SoundManager.js"

export class GameManager{
    level = 1
    factory = {}
    entities = []
    player = null
    laterKill = []
    isGameOver = false
    time
    iteration = 0
    recordsTable = []
    userInfo = {
        time: 0,
        name: ""
    }
    maxNumberOfBestRecords = 10
    constructor() {
        this.factory['player'] = Player
        this.factory['zombie'] = Zombie
        this.factory['bonus'] = Bonus
        this.factory['speed'] = Speed
    }

    initPlayer(obj){
        this.player = obj
    }

    kill(obj){
        this.laterKill.push(obj)
    }

    update(ctx){
        this.iteration++
        document.getElementById('playerName').innerHTML = localStorage["username"]
        document.getElementById('playerScore').innerHTML = this.player.score
        this.time = Number(localStorage["time"]) + Number(this.iteration)
        document.getElementById('playerTime').innerHTML = this.time.toString()
        if(this.isGameOver){

        }
        if (this.player === null)
            return

        this.player.moveX = 0
        this.player.moveY = 0


        if (eventManager.actions["up"]) {
            this.player.moveY = -1
            this.player.moveX = 0
        }
        if (eventManager.actions["down"]) {
            this.player.moveY = 1
            this.player.moveX = 0
        }
        if (eventManager.actions["left"]) {
            this.player.moveX = -1
            this.player.moveY = 0
        }
        if (eventManager.actions["right"]) {
            this.player.moveX = 1
            this.player.moveY = 0
        }

        this.entities.forEach((entity) => {
            try {
                entity.update()

            } catch (ex) {

            }
        });

        for (let i = 0; i < this.laterKill.length; i++) {
            let idx = this.entities.indexOf(this.laterKill[i])
            if (idx > -1)
                this.entities.splice(idx, 1)
        }
        mapManager.drawMap(ctx)
        this.draw(ctx)
    }

    draw(ctx){
        if(this.entities.length === 0) {
            setTimeout(() => {
                this.draw(ctx)
            }, 100)
        } else{
            for(let i = 0; i < this.entities.length; i++){
                this.entities[i].draw(ctx)
            }
        }
    }

    loadAll(canvas){
        eventManager.eventListener(canvas)
        soundManager.init()
    }

    play(ctx) {
        const interval = setInterval(() => {
            if (this.isGameOver){
                clearInterval(interval)
            }
            this.update(ctx)
            if (this.level === 2){
                if (localStorage["level"] === "2")
                    this.gameOver("win")
                clearInterval(interval)
            }
        }, 100)
    }

    gameOver(reason){
        console.log("GameOver")
        this.isGameOver = true
        document.getElementById('map').style.opacity = "0.25"
        if (reason === 'win'){
            document.getElementById('youWon').style.opacity = "1"
            soundManager.play("../sounds/win.mp3", {looping: false, volume: 1})
            this.addRecordInTable()
            this.showRecordTable()
        }
        else{
            document.getElementById('gameOver').style.opacity = "1"
            soundManager.play("../sounds/die.mp3", {looping: false, volume: 1})
        }
    }

    addRecordInTable(){
        if (localStorage["recordsTable"] !== undefined){
            this.recordsTable = JSON.parse(localStorage["recordsTable"])
        }
        this.userInfo.name = localStorage["username"]
        this.userInfo.time = this.time
        this.recordsTable.push(this.userInfo)
        this.recordsTable.sort((firstRecord, secondRecord) => firstRecord.time - secondRecord.time)
        localStorage["recordsTable"] = JSON.stringify(this.recordsTable)
        console.log(localStorage["recordsTable"])
    }


    showRecordTable(){
        let promise = new Promise((resolve) => {
            setTimeout(() => {
                document.getElementById('map').style.opacity = "0"
                document.getElementById("youWon").style.opacity = "0"
                setTimeout(() => {
                    resolve()
                }, 2000)
            }, 2000)
        })
        promise.then(() => {
            const recordsTable = document.getElementById("recordTable")
            recordsTable.style.opacity = "1"
            let bestNonRepeatingPlayers = []
            for(let i = 0; i < Math.min(this.recordsTable.length, this.maxNumberOfBestRecords); i++){
                const record = document.createElement("p")
                record.style.fontSize = "27px"
                console.log("yes")
                const place = i + 1
                if (!bestNonRepeatingPlayers.includes(this.recordsTable[i].name)){
                    record.innerHTML = place.toString() + '. ' + this.recordsTable[i].name + ' ' +
                        this.recordsTable[i].time.toString()
                    recordsTable.appendChild(record)
                    bestNonRepeatingPlayers.push(this.recordsTable[i].name)
                }
            }
        })
    }

}
export let gameManager = new GameManager()