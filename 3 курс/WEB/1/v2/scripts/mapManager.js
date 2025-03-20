import { gameManager } from "./gameManager.js"
export let mapManager = {
    mapData : new Array(),
    tLayer : [new Array(), new Array(), new Array(), new Array()],
    tSize : {x: 32, y: 32},
    mapSize : {0: {x: 50, y: 31}, 1:{x: 50, y: 50}, 2: {x: 15, y: 15}, 3: {x: 15, y: 15}},
    tileSets : new Array(),
    images : new Array(),
    jsonLoaded : false,
    imgLoaded : false,
    view : {x: 0, y: 0, w: 960, h: 800},
    loadMap : function(){
        let request = new XMLHttpRequest();
        request.onreadystatechange = function(){
            if (request.readyState === 4 && request.status === 200){
                mapManager.parseMap(JSON.parse(request.responseText));
            }
        }
        request.open("GET", '/paths', true);
        request.send();
    },

    parseMap : function(response){
        const path1 = response["map1_j"];
        const path2 = response['map2_j'];
        const path3 = response['tower1_j'];
        const path4 = response['tower2_j'];
        console.log(path1,path2,path3,path4);
        this.mapData.push(path1, path2, path3, path4);
        for (let i = 0; i < mapManager.mapData.length; i++) {
            for(let j = 0; j < mapManager.mapData[i].tilesets.length; j++){
                let img = new Image();
                img.src = this.mapData[i].tilesets[j].image;
                img.onload = function(){
                    if (!mapManager.images.includes(img)){
                        mapManager.images.push(img);
                    } 
                let tile = mapManager.mapData[i].tilesets[j];
                //console.log(tile);
                let tileset = {
                    firstgrid: tile.firstgid,
                    image: img,
                    name: tile.name,
                    xCount: tile.imagewidth / 32,
                    yCount: tile.imageheight / 32
                };
                //console.log(mapManager.tileSets.length)
                mapManager.tileSets.push(tileset);    
                }
            }
        }
        this.imgLoaded = true;
        this.jsonLoaded = true;
    },

    draw : function(context, mapNum){
        
        if (!mapManager.imgLoaded || !mapManager.jsonLoaded || mapManager.tileSets.length < 4) setTimeout(function(){mapManager.draw(context,mapNum)});
        else {
            this.centerAt(gameManager.player[gameManager.level].pos_x,gameManager.player[gameManager.level].pos_y);
            if (mapManager.tLayer[0].length == 0 && mapManager.tLayer[1].length == 0 && mapManager.tLayer[2].length == 0 && mapManager.tLayer[3].length == 0)
                for (let i = 0; i < mapManager.mapData.length; i++){
                    for (let id = 0; id < mapManager.mapData[i].layers.length;id++){
                        let layer = mapManager.mapData[i].layers[id];
                        if (layer.type === "tilelayer"){
                            mapManager.tLayer[i].push(layer);
                        }
                    } 
                }
            for(let i = 0; i < mapManager.tLayer[mapNum].length; i++){
                for(let j = 0; j < mapManager.tLayer[mapNum][i].data.length; j++){
                    if(mapManager.tLayer[mapNum][i].data[j] !== 0){
                        let tile = mapManager.getTile(mapManager.tLayer[mapNum][i].data[j]);
                        let pX = (j % this.mapSize[mapNum].x) * this.tSize.x
                        let pY = Math.floor(j / this.mapSize[mapNum].x) * this.tSize.y
                        if (!this.isVisible(pX,pY)) continue;
                        pX -=this.view.x;
                        pY -=this.view.y;
                        context.drawImage(tile.img,tile.px, tile.py, mapManager.tSize.x, mapManager.tSize.y,pX,pY,mapManager.tSize.x,mapManager.tSize.y);
                    }
                }
            }
        }
    },
    
    isVisible : function(pX,pY) {
        if (pX + this.tSize.x < this.view.x || pY + this.tSize.y < this.view.y || 
            pX > this.view.x + this.view.w || pY > this.view.y + this.view.h)
            return false;
        return true;
    },
    
    centerAt : function(x,y) {
        if (x < this.view.w / 2) this.view.x = 0;
        else if(x > this.mapSize[gameManager.level] - this.view.w/2) this.view.x = this.mapSize[gameManager.level] - this.view.w
        else this.view.x = x - this.view.w/2;
        if (y < this.view.h / 2) this.view.y = 0;
        else if (y > this.mapSize[gameManager.level] - this.view.h/2) this.view.y = this.mapSize[gameManager.level].y - this.view.h;
        else this.view.y = y - this.view.h/2;
    },
    getTile : function(tileIndex){
        let tile = {
            img: null,
            px:0, py: 0
        };
        let tileset = this.tileSets[0];
        //console.log(this.tileSets)
        tile.img = tileset.image;
        let id = tileIndex - tileset.firstgrid;
        let x = id % (tileset.xCount - 0.5);
        let y = Math.floor(id / (tileset.xCount - 0.5));
        tile.px = x * mapManager.tSize.x;
        tile.py = y * mapManager.tSize.y;
        return tile;
    },

    getTileSet: function(tileIndex){
        for (let i = mapManager.tileSets.length - 1; i >= 0; i--){
            if(mapManager.tileSets[i].firstgrid <= tileIndex){
                return mapManager.tileSets[i];
            }
        }
        return null;
    },

    parseEntities : function(){
        if (!this.imgLoaded || !this.jsonLoaded) setTimeout(function(){mapManager.parseEntities()});
        else {
            for (let i = 0; i < this.mapData.length; i++){
                gameManager.entities.push(new Array());
                for (let id = 0; id < this.mapData[i].layers.length;id++){
                    let entities = this.mapData[i].layers[id];
                    if (entities.type === 'objectgroup'){
                        for(let j = 0; j < entities.objects.length; j++){
                            let entity = entities.objects[j];
                            //console.log(entity);
                            try{
                                let obj;
                                if (entity.name === 'player'){
                                    obj = Object.create(gameManager.factory['player']);
                                }
                                else if (entity.name.substring(0, 7) === 'villain'){
                                    obj = Object.create(gameManager.factory['villain']);
                                }
                                else {
                                    obj = Object.create(gameManager.factory['tool']);
                                } 
                                obj.name= entity.name;
                                obj.pos_x = entity.x;
                                obj.pos_y = entity.y;

                                gameManager.entities[i].push(obj)
                                if (obj.name === "player")
                                    gameManager.initPlayer(obj,i);
                            } catch(ex){
                                console.log(ex);
                            }
                        }
                    }
                }
            }
        }
    },
    getTilesetIdx(x,y,ind) {
        let wX = Math.ceil((x - 8)/ this.tSize.x);
        let wY = Math.ceil((y - 32)/ this.tSize.y);
        let result = [];
        let idx = Math.floor(wY * this.mapSize[ind].x) + Math.floor(wX);
        for (let i = 0; i < this.tLayer[ind].length; i++) {
            if (this.tLayer[ind][i].data[idx] != 0) {
                result.push(this.tLayer[ind][i].data[idx]);
            }
        }
        return result;
    }
}
