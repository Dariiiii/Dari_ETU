import { gameManager } from "./GameManager.js"

export class MapManager {
    mapData = null
    tLayer = []
    xCount = 0
    yCount = 0
    tSize = { x: 32, y: 32 }
    mapSize = { x: 32, y: 32 }
    tileSets = []
    imgLoadCount = 0
    imgLoaded = false
    jsonLoaded = false

    loadMap(path) {
        var request = new XMLHttpRequest();
        request.onreadystatechange = function () {
            if (request.readyState === 4 && request.status === 200)
                mapManager.parseMap(request.responseText);
        };
        request.open("GET", path, true);
        request.send();
    }

    parseMap(tilesJSON) {
        this.mapData = JSON.parse(tilesJSON);
        this.xCount = this.mapData.width;
        this.yCount = this.mapData.height;
        this.tSize.x = this.mapData.tilewidth;
        this.tSize.y = this.mapData.tileheight;
        this.mapSize.x = this.xCount * this.tSize.x;
        this.mapSize.y = this.yCount * this.tSize.y;
        for (let i = 0; i < this.mapData.tilesets.length; i++) {
            const img = new Image()
            img.onload = function () {
                mapManager.imgLoadCount++;
                if (mapManager.imgLoadCount === mapManager.mapData.tilesets.length)
                    mapManager.imgLoaded = true;
            };
            img.src = this.mapData.tilesets[i].image;
            let t = this.mapData.tilesets[i];
            let ts = {
                firstgid: t.firstgid,
                image: img,
                name: t.name,
                xCount: Math.floor(t.imagewidth / mapManager.tSize.x),
                yCount: Math.floor(t.imageheight / mapManager.tSize.y)
            }
            this.tileSets.push(ts);
        }
        this.jsonLoaded = true;
        for (let id = 0; id < this.mapData.layers.length; id++) {
            if (this.mapData.layers[id].type === "tilelayer")
                this.tLayer.push(this.mapData.layers[id])
        }
    }

    drawBackground(ctx) {
        if (!this.imgLoaded || !this.jsonLoaded) {
            setTimeout(() => { this.drawBackground(ctx) }, 100)
        }
        else {
            for (let i = 0; i < this.tLayer[0].data.length; i++) {
                if (this.tLayer[0].data[i] !== 0) {
                    let tile = this.getTile(this.tLayer[0].data[i])
                    let pX = (i % this.xCount) * this.tSize.x
                    let pY = Math.floor(i / this.xCount) * this.tSize.y
                    ctx.drawImage(tile.img, tile.px, tile.py, this.tSize.x, this.tSize.y, pX, pY, this.tSize.x, this.tSize.y)
                }
            }
        }
    }

    draw(ctx) {
        if (!this.imgLoaded || !this.jsonLoaded) {
            setTimeout(() => { this.draw(ctx) }, 100)
        }
        else {
            for (let id = 1; id < this.tLayer.length; id++) {
                for (let i = 0; i < this.tLayer[id].data.length; i++) {
                    if (this.tLayer[id].data[i] !== 0) {
                        let tile = this.getTile(this.tLayer[id].data[i])
                        let pX = (i % this.xCount) * this.tSize.x
                        let pY = Math.floor(i / this.xCount) * this.tSize.y
                        ctx.drawImage(tile.img, tile.px, tile.py, this.tSize.x, this.tSize.y, pX, pY, this.tSize.x, this.tSize.y)
                    }
                }
            }
        }
    }

    getTile(tileIndex) {
        let tile = {
            img: null,
            px: 0,
            py: 0
        }
        let tileSet = this.getTileSet(tileIndex)
        tile.img = tileSet.image // и3oбpaжehиe иcкomoгo tileset 
        let id = tileIndex - tileSet.firstgid
        tile.px = id % tileSet.xCount * this.tSize.x
        tile.py = Math.floor(id / tileSet.xCount) * this.tSize.y
        return tile
    }

    getTileSet(tileIndex) {
        for (let i = this.tileSets.length - 1; i >= 0; i--) {
            if (this.tileSets[i].firstgid <= tileIndex) {
                return this.tileSets[i]
            }
        }
        return null;
    }

    parseEntities() {
        if (!this.imgLoaded || !this.jsonLoaded) {
            setTimeout(() => { this.parseEntities() }, 100);
        }
        else {
            let name = ''
            // gameManager.entities = []
            for (let j = 0; j < this.mapData.layers.length; j++) {
                if (this.mapData.layers[j].type === 'objectgroup') {
                    const entities = this.mapData.layers[j]
                    for (let i = 0; i < entities.objects.length; i++) {
                        const entity = entities.objects[i]
                        if (entity.name == 'cat_left1')
                            name = 'player'
                        else if (entity.name == 'mouse_left' || entity.name == 'dog_left')
                            name = 'enemy'
                        else
                            name = 'bonus'
                        try {
                            let obj = new gameManager.factory[name]
                            obj.name = entity.name
                            obj.posX = entity.x
                            obj.posY = entity.y - 32
                            obj.sizeX = entity.width
                            obj.sizeY = entity.height
                            if (name === 'player')
                                gameManager.initPlayer(obj)
                            else
                                gameManager.entities[gameManager.level - 1].push(obj)
                        } catch (ex) {
                            console.log("ERROR while creating:[" + entity.gid + "]" + entity.type + "," + ex)
                            console.log(entity.type)
                        }
                    }
                }
            }
        }
    }

    getTileIdx(x, y) {
        let wX1 = Math.ceil((x - 8) / this.tSize.x);
        let wY1 = Math.ceil((y - 8) / this.tSize.y);
        let id1 = Math.floor(wY1 * this.xCount) + Math.floor(wX1);
        let wX2 = Math.ceil((x - 24) / this.tSize.x);
        let wY2 = Math.ceil((y - 24) / this.tSize.y);
        let id2 = Math.floor(wY2 * this.xCount) + Math.floor(wX2);
        let res = []
        // console.log(this.tLayer[2].name)
        // const id = Math.floor(y / this.tSize.y) * this.xCount + Math.floor(x / this.tSize.x)
        for (var i = 0; i < this.tLayer.length; i++) {
            if (this.tLayer[i].data[id1] != 0 || this.tLayer[i].data[id2] != 0)
                res.push(this.tLayer[i].name)
        }
        return res
    }
}

export let mapManager = new MapManager()
