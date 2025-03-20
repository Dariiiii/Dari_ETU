import { physicManager } from "./physicManager.js"
import { gameManager } from "./gameManager.js"
import { spriteManager } from "./spriteManager.js"

export let Entity  = {
    pos_x : 0,
    pos_y : 0,
    name : '',
    extend: function (extendProto) {
        let object = Object.create(this)
        for (let property in extendProto) {
            if (this.hasOwnProperty(property) || typeof object[property] === 'undefined') {
                object[property] = extendProto[property]
            }
        }
        return object
    }
}

export let Hero = Entity.extend({
    armor : 0,
    stock :30,
    manaPoint : 100,
    movex : 0,
    movey : 0,
    superAttack : 100, // обычная атака
    money : 0,
    damage : 30,
    health : 100,
    index : 1,
    frame : 0,
    speed : 8,
    sprite_name : "h_r1",
    draw: function(ctx) {
        if (this.frame % 100 == 0) this.index = (this.index + 1) % 6 + 1;
        if (this.movex === -1)
            this.sprite_name = "h_l" + this.index;
        else if (this.movex === 1)
            this.sprite_name = "h_r" + this.index;
        else if (this.movey === 1)
            this.sprite_name = "h_d" + this.index;
        else if (this.movey === -1)
            this.sprite_name = "h_u" + this.index;
        //console.log(this.sprite_name);
        spriteManager.drawSprite(ctx, this.sprite_name, this.pos_x, this.pos_y)
    },
    onTouchEntity: function (obj) {
        if (obj.name === "heal") {
            if (this.health + 20 < 100)
            this.health += 20;
            else this.health = 100;
            obj.kill()
        }
        else if (obj.name === "meat") {
            if (this.health + 50 < 100) this.health += 50;
            else this.health = 100;
            obj.kill(); 
        }
        else if (obj.name === "mana") {
            if(this.manaPoint + 50 < 100) this.manaPoint += 50;
            this.manaPoint = 100;
            obj.kill();
        }
        else if (obj.name === "shield") {
            this.armor += 20;
            obj.kill();
        }
        else if (obj.name === "arrow") {
            this.stock += 1;
            obj.kill();
        }
        else if (obj.name === "money"){
            this.money +=50;
            obj.kill();
        } 
        else if(obj.name === "treasure"){
            this.money +=100;
            obj.kill();
        }
        else if (obj.name === "trap"){
            this.health -=50;
            obj.kill();
        }
        else if(obj.name.substring(0, 2) === "to"){
            if (gameManager.times[gameManager.level] - gameManager.startTime > 2000){
                console.log(gameManager);
                gameManager.nextLevel(gameManager.level);
                gameManager.startTime = new Date();
                gameManager.level = Number(obj.name[obj.name.length - 1]);
            }
        }
    },
    update : function(){
        physicManager.update(this);
    }
})

export let Tools = Entity.extend({
    draw: function(context){
        if (this.name === "heal")
            spriteManager.drawSprite(context, "heal", this.pos_x, this.pos_y);
        else if (this.name === "shield")
            spriteManager.drawSprite(context, "shield", this.pos_x, this.pos_y);
        else if (this.name === "trap")
            spriteManager.drawSprite(context, "trap", this.pos_x, this.pos_y);
        else if (this.name === "money")
            spriteManager.drawSprite(context, "money", this.pos_x, this.pos_y);
        else if (this.name === "treasure")
            spriteManager.drawSprite(context, "treasure", this.pos_x, this.pos_y);        
        else if (this.name === "mana")
            spriteManager.drawSprite(context, "mana", this.pos_x, this.pos_y);
        else if (this.name === "arrow")
            spriteManager.drawSprite(context, "arrow", this.pos_x, this.pos_y);
        else if (this.name === "meat")
            spriteManager.drawSprite(context, "meat", this.pos_x, this.pos_y);
        else if (this.name.substring(0, 2) == "to")
            spriteManager.drawSprite(context, "to", this.pos_x, this.pos_y);

    },
    
    update: function(){},
    kill : function(){
        gameManager.kill(this);
    }
});
export let Enemy = Entity.extend({
    health : 100,
    index : 1,
    frame : 0,
    speed : 5,
    damage : 20,
    movex : 0,
    movey : 0,
    sprite_name : '',
    number : 0,
    pointerX : null,
    pointerY : null,
    attackTime : new Date(),
    draw: function(ctx) {
       // console.log(this.name);
        this.number = this.name[this.name.length - 1];
        //console.log(this.number);
        this.speed = parseInt(this.number);
        this.damage = parseInt(this.number) * 5;
        if (this.frame % 100 == 0) this.index = (this.index + 1) % 4 + 1;
        //console.log(this.index);
        //console.log(this.movex);
        if (this.movex == -1)
            this.sprite_name = "v" + this.number + "_l"  + this.index;
        else if (this.movex == 1 || (this.movex == 0 && this.movey == 0))
            this.sprite_name = "v" + this.number + "_r" + this.index;
        else if (this.movey == -1)
            this.sprite_name = "v" + this.number + "_d" + this.index;
        else if (this.movey == 1)
            this.sprite_name = "v" + this.number + "_u" + this.index;
        spriteManager.drawSprite(ctx, this.sprite_name, this.pos_x, this.pos_y)
    },
    update: function(){
        physicManager.updateEnemies(this);
    },
    kill : function(){
        gameManager.kill(this);
    },
    attack : function(player){
        const time = new Date()
        if (Math.abs(time - this.attackTime) >= 5000){
            this.attackTime = time;
            let current_damage = this.damage;
            if(player.armor - current_damage >= 0){
                player.armor-=current_damage
            }
            else {
                current_damage -= player.armor
                player.armor = 0;
                player.health -= current_damage;
            }
        }
    }
})


