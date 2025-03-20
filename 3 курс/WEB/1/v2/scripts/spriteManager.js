import { gameManager } from "./gameManager.js"
import { mapManager } from "./mapManager.js"

export let spriteManager = {
    images : new Array(),
    sprites : new Array(),
    imgLoaded : false,
    jsonLoaded : false,
    loadAtlas: function(images){
        let request = new XMLHttpRequest();
        request.onreadystatechange = function(){
            if(request.readyState === 4 && request.status === 200) {
                spriteManager.parseAtlas(JSON.parse(request.responseText));
            }
        }
        request.open("GET", '/jsons', true);
        request.send();
        spriteManager.loadImg(images);
    },
    loadImg: function(imgnames){
        for (let i = 0; i< imgnames.length; i++){
            let image = new Image();
            image.src = imgnames[i];
            this.images.push(image);
        }
        this.imgLoaded = true;
    },
    parseAtlas: function(data){
        const hero = data['sprites_hj'];
        const tools = data['sprites_toolsj'];
        const treasure = data['sprites_treasurej'];
        const villain = data['sprites_vj'];
        const herol = data['sprites_hlj'];
        const tp = data['sprites_tpj']
        for (let i = 0; i< 6; i++) this.sprites.push(Array());
        for (let index in hero) {
            let frame = hero[index];
            this.sprites[0].push({name: frame.name, x: frame.x, y: frame.y, w: frame.width, h : frame.height});
        }
        for (let index in tools) {
            let frame = tools[index];
            this.sprites[1].push({name: frame.name, x: frame.x, y: frame.y, w: frame.width, h : frame.height});
        }
        for (let index in treasure) {
            let frame = treasure[index];
            this.sprites[2].push({name: frame.name, x: frame.x, y: frame.y, w: frame.width, h : frame.height});
        }
        for (let index in villain) {
            let frame = villain[index];
            this.sprites[3].push({name: frame.name, x: frame.x, y: frame.y, w: frame.width, h : frame.height});
        }
        for (let index in herol) {
            let frame = herol[index];
            this.sprites[4].push({name: frame.name, x: frame.x, y: frame.y, w: frame.width, h : frame.height});
        }
        for (let index in tp) {
            let frame = tp[index];
            this.sprites[5].push({name: frame.name, x: frame.x, y: frame.y, w: frame.width, h : frame.height});
        }
        this.jsonLoaded = true
    },

    drawSprite: function(context,name,x,y){
        if (!this.imgLoaded || !this.jsonLoaded)
            setTimeout( function () { spriteManager.drawSprite(context,name, x, y) }, 100 )
        else {
            //if(name.substring(0,2) == "h_" || (Math.abs(centerX - x) < 320 && Math.abs(centerY - y) < 320)){
                let sprite;
                sprite = this.getSprite(name);
                if (!mapManager.isVisible(x,y,sprite.w,sprite.h)) return;
                let index;
                for (let i = 0 ; i < this.sprites.length; i++){
                    for (let j = 0 ; j < this.sprites[i].length; j++){
                        if (this.sprites[i][j] == sprite) {
                            index = i;
                            break;
                        } 
                    }
                }
                x -= mapManager.view.x;
                y -= mapManager.view.y;
                //console.log(index);
                context.drawImage(this.images[index], sprite.x , sprite.y, sprite.w, sprite.h, x, y -32, sprite.w, sprite.h)
            //}
        }
    },
    getSprite: function(name) {
        for (let i = 0; i < this.sprites.length; i++) {
            let sprite = this.sprites[i]
            for (let j = 0; j < sprite.length; j++){
                if(sprite[j].name === name)
                    return sprite[j];
            }
        }
        return null;
    }
}