import {gameManager} from "./GameManager.js"

export class MapManager{
    #mapData = null
    #tileSets = []
    #xCount = 0
    #yCount = 0
    #tSize = {x: 32, y: 32}
    #mapSize = {x:32, y:32}
    #imgLoadCount = 0
    #imgLoaded = false
    #jsonLoaded = false

    loadData(path){
        const request = new XMLHttpRequest()
        request.onreadystatechange = () => {
            if(request.readyState === 4 && request.status === 200){
                this.parseMap(request.responseText)
            }
        }
        request.open("GET", path, true)
        request.send()
    }

    parseMap(titleJSON){
        this.#mapData = JSON.parse(titleJSON)
        this.#xCount = this.#mapData.width
        this.#yCount = this.#mapData.height
        this.#tSize.x = this.#mapData.tilewidth
        this.#tSize.y = this.#mapData.tileheight
        this.#mapSize.x = this.#xCount * this.#tSize.x
        this.#mapSize.y = this.#yCount * this.#tSize.y
        for(let i = 0; i < this.#mapData.tilesets.length; i++){
            const img = new Image()
            img.onload = () => {
                this.#imgLoadCount++
                if(this.#imgLoadCount === this.#mapData.tilesets.length){
                    this.#imgLoaded = true
                }
            };
            img.src = this.#mapData.tilesets[i].image
            const t = this.#mapData.tilesets[i]
            let tileSet = {
                firstgid: t.firstgid,
                image: img,
                name: t.name,
                xCount: Math.floor(t.imagewidth / this.#tSize.x),
                yCount: Math.floor(t.imageheight / this.#tSize.y)
            };
            this.#tileSets.push(tileSet)
        }
        this.#jsonLoaded = true;
    }

    drawMap(ctx){
        if(!this.#imgLoaded || !this.#jsonLoaded){
            setTimeout(() => {this.drawMap(ctx)}, 100)
        } else{
            for( let id = 0; id < this.#mapData.layers.length; id++){
                const currentLayer = this.#mapData.layers[id]
                if(currentLayer.type === "tilelayer"){
                    this.#drawTileLayer(ctx, currentLayer)
                }

            }

        }
    }

    parseEntities(){
        if(!this.#imgLoaded || !this.#jsonLoaded){
            setTimeout(()=>{this.parseEntities()}, 100);
        } else{
            for(let j = 0; j < this.#mapData.layers.length; j++){
                if(this.#mapData.layers[j].type === 'objectgroup'){
                    const entities = this.#mapData.layers[j]
                    for(let i = 0; i < entities.objects.length; i++){
                        const entity = entities.objects[i]
                        try{
                            let obj = new gameManager.factory[entity.name]
                            obj.name = entity.name
                            obj.posX = entity.x
                            obj.posY = entity.y
                            obj.sizeX = entity.width
                            obj.sizeY = entity.height
                            gameManager.entities.push(obj)
                            if(entity.name === 'player')
                                gameManager.initPlayer(obj)
                        } catch (ex){
                            console.log("ERROR while creating:[" + entity.gid + "]" + entity.type + "," + ex)
                            console.log(entity.type)
                        }
                    }
                }
            }
        }
    }

    #drawTileLayer(ctx, currentLayer){
        for(let i = 0; i < currentLayer.data.length; i++){
            if(currentLayer.data[i] !== 0){
                const tile = this.#getTile(currentLayer.data[i])
                const pX = (i % this.#xCount) * this.#tSize.x
                const pY = Math.floor(i / this.#xCount) * this.#tSize.y
                ctx.drawImage(tile.img, tile.px, tile.py,
                    this.#tSize.x, this.#tSize.y, pX, pY, this.#tSize.x, this.#tSize.y)
            }
        }
    }

    #getTile(tileIndex){
        const tile = {
            img: null,
            px: 0,
            py: 0
        }
        const tileSet = this.#getTileSet(tileIndex)
        tile.img = tileSet.image
        const id = tileIndex - tileSet.firstgid
        const x = id % tileSet.xCount
        const y = Math.floor(id / tileSet.xCount)
        tile.px = x * this.#tSize.x
        tile.py = y * this.#tSize.y
        return tile
    }

    #getTileSet(tileIndex){
        for(let i = this.#tileSets.length - 1; i >= 0; i--){
            if(this.#tileSets[i].firstgid <= tileIndex){
                return this.#tileSets[i]
            }
        }
        return null;
    }

    getTileId(x, y, layerNumber){
        const id = Math.floor(y / this.#tSize.y) * this.#xCount + Math.floor(x / this.#tSize.x)
        return  this.#mapData.layers[layerNumber].data[id]
    }

}

export let mapManager = new MapManager()