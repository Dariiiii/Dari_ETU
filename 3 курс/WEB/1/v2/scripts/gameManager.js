// import { mapManager } from "./mapManager.js"
// import { Hero, Enemy,Tools } from "./entities.js"
// import { spriteManager } from "./spriteManager.js"
// import { eventManager } from "./eventManager.js"
// import { soundManager } from "./soundManager.js"
let canvas = document.getElementById('map')
let context = canvas.getContext('2d')

export let gameManager = {
    factory: {},
    entities: [],
    time: 0,
    player: new Array(4),
    level: 0,
    laterKill: [],
    startTime: null,
    times: new Array(4),
    initPlayer: function (obj, level) {
        //onsole.log("hello");
        this.player[level] = obj;
    },
    kill: function (obj) {
        this.laterKill.push(obj);
    },
    draw: function (context) {
        for (let i = 0; i < gameManager.entities[this.level].length; i++) {
            this.entities[this.level][i].draw(context);
        }
    },
    checker: function () {
        for (let i = 0; i < gameManager.entities.length; i++) {
            for (let j = 0; j < gameManager.entities[i].length; j++) {
                if (gameManager.entities[i][j].name == 'treasure' || gameManager.entities[i][j].name == 'money')
                    return true;
            }
        }
        return false;
    },

    gameOver: function () {
        let current_score = {
            player: localStorage.getItem('game.username'),
            value: gameManager.player[gameManager.level].money,
            place: -1,
        }
        if (gameManager.checker()) localStorage.setItem('result', true);
        else localStorage.setItem('result', false);
        let score_table = JSON.parse(localStorage.getItem('game')) || [];
        score_table.push(current_score);
        score_table.sort((a, b) => b.value - a.value);
        score_table.forEach((record, index) => {
            record.place = index + 1;
        });
        localStorage.setItem('game', JSON.stringify(score_table));
        window.location.href = "/lose";
    },
    update: function () {
        if (gameManager.player[gameManager.level] === undefined)
            return;
        else if (gameManager.player[gameManager.level].health <= 0 || !gameManager.checker())
            gameManager.gameOver();
        else {
            gameManager.player[gameManager.level].movex = 0;
            gameManager.player[gameManager.level].movey = 0;
            if (eventManager.action["up"])
                gameManager.player[gameManager.level].movey = -1;
            if (eventManager.action["down"])
                gameManager.player[gameManager.level].movey = 1;
            if (eventManager.action["left"])
                gameManager.player[gameManager.level].movex = -1;
            if (eventManager.action["right"])
                gameManager.player[gameManager.level].movex = 1;
            gameManager.entities[gameManager.level].forEach(function (e) {
                e.update();
            });

            for (let i = 0; i < gameManager.laterKill.length; i++) {
                let idx = gameManager.entities[gameManager.level].indexOf(gameManager.laterKill[i]);
                if (idx > -1)
                    gameManager.entities[gameManager.level].splice(idx, 1);
            }

            if (gameManager.laterKill.lenght > 0)
                gameManager.laterKill.lenght = 0;

            document.getElementById("score").innerText = "Текущий результат: " + gameManager.player[gameManager.level].money;
            document.getElementById("health").innerText = "Уровень здоровья: " + gameManager.player[gameManager.level].health;
            document.getElementById("mana").innerText = "Уровень маны: " + gameManager.player[gameManager.level].manaPoint;
            document.getElementById("arrows").innerText = "Запас стрел: " + gameManager.player[gameManager.level].stock;
            document.getElementById("armor").innerText = "Состояние брони: " + gameManager.player[gameManager.level].armor;
            context.fillStyle = "black";
            context.fillRect(0, 0, canvas.width, canvas.height);
            mapManager.draw(context, gameManager.level);
            gameManager.draw(context);
            gameManager.times[gameManager.level] = new Date();
        }
    },
    loadAll: function () {
        let pngs = ["images/archer.png", "images/tools.png", "images/Gothic.png", "images/villains.png", "images/archer_l.png", "images/Castle2.png"];
        mapManager.loadMap();
        spriteManager.loadAtlas(pngs);
        gameManager.factory['player'] = Hero;
        gameManager.factory['villain'] = Enemy;
        gameManager.factory['tool'] = Tools;
        mapManager.parseEntities();
        context.fillStyle = "black";
        context.fillRect(0, 0, canvas.width, canvas.height);
        mapManager.draw(context, this.level);
        eventManager.setup(canvas);
        soundManager.init();
        soundManager.play("/sounds/back.mp3", { looping: true, volume: 1 })
    },
    play: function () {
        this.interval = setInterval(gameManager.update, 100);
    },
    nextLevel: function (index) {
        for (let i = 0; i < gameManager.player.length; i++) {
            if (i != index) {
                if (!gameManager.player[i].stock) setTimeout(function () { mapManager.parseEntities() });
                else {
                    gameManager.player[i].stock = gameManager.player[index].stock;
                    gameManager.player[i].manaPoint = gameManager.player[index].manaPoint;
                    gameManager.player[i].health = gameManager.player[index].health;
                    gameManager.player[i].money = gameManager.player[index].money;
                    gameManager.player[i].armor = gameManager.player[index].armor;
                }
            }
        }
        context.clearRect(0, 0, canvas.width, canvas.height);
        this.startTime = new Date();
    },
}