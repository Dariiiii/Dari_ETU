import {spriteManager} from "./SpriteManager.js"
import {mapManager} from "./MapManager.js"
import {gameManager} from "./GameManager.js"


function run(){
    if (localStorage["level"] === undefined){
        localStorage["level"] = 1
    }
    if (localStorage["time"] === undefined){
        localStorage["time"] = 0
    }
    const canvas = document.getElementById("map")
    const ctx = canvas.getContext("2d")
    if (localStorage["level"] === "1"){
        console.log("check")
        mapManager.loadData('../maps/tilemap.json')
        spriteManager.loadAtlas('../sprites/sprites.json', '../sprites/sprites.png')
        mapManager.parseEntities()
        gameManager.loadAll(canvas)
        gameManager.play(ctx)
        setInterval(() =>{
            if (gameManager.level === 2){
                localStorage["time"] = gameManager.time
                localStorage["speed"] = gameManager.player.speed
                localStorage["level"] = 2
                window.location.reload()
            }
        }, 100)
    }
    else{
        mapManager.loadData('../maps/sec_level.json')
        spriteManager.loadAtlas('../sprites/sprites.json', '../sprites/sprites.png')
        mapManager.parseEntities()
        gameManager.loadAll(canvas)
        gameManager.play(ctx)
        if (gameManager.isGameOver){
            localStorage.clear()
        }
    }

}

run()