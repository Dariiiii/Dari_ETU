const canvas1 = document.getElementById('tetris');
const context1 = canvas1.getContext('2d');
const canvas2 = document.getElementById('nextFigure');
const context2 = canvas2.getContext('2d');
let score = document.getElementById('score');
let level = document.getElementById('level');

const details = {
    0: [
        [0, 1, 0],
        [1, 1, 0],
        [1, 0, 0]
    ],
    1: [
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0]
    ],
    2: [
        [1, 0, 0],
        [1, 0, 0],
        [1, 1, 0]
    ],
    3: [
        [0, 1, 0],
        [0, 1, 0],
        [1, 1, 0]
    ],
    4: [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0]
    ],
    5: [
        [1, 1],
        [1, 1]
    ],
    6: [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
    ]
}
const colors = [
    'rgb(251, 192, 124)',
    'rgb(249, 162, 64)',
    'rgb(255, 148, 26)',
    'rgb(231, 123, 0)',
    'rgb(178, 95, 0)',
    'rgb(251, 87, 11)',
    'rgb(204, 65, 0)'
];

const oneSize = 35;
const twoSize = 40;
let newScore = 0;
let newLevel = 1;
let shot = 0;
let field = [];
let sequenceOfDetails = [];
let rAF = null;
let currentDetail = getDetail();
let nextDetail = getDetail();
let endFlag = false;

for (let i = -3; i < 20; i++) {
    field[i] = [];
    for (let j = 0; j < 10; j++) {
        field[i][j] = 0;
    }
}

function getSequence() {
    if (sequenceOfDetails.length == 7) {
        sequenceOfDetails = [];
    }
    let indexDetail = Math.floor(Math.random() * 7);
    if (sequenceOfDetails.includes(indexDetail)) {
        return getSequence();
    }
    return indexDetail;
}

function getDetail() {
    const indexDetail = getSequence();
    sequenceOfDetails.push(indexDetail);
    const startX = Math.floor((10 - details[indexDetail].length) / 2);
    const startY = 1 - details[indexDetail].length;
    return {
        index: indexDetail,
        view: details[indexDetail],
        currentX: startX,
        currentY: startY
    }
}

function rotateDetail(detail) {
    let n = detail.length;
    let newDetail = new Array(n);
    for (var i = 0; i < n; i++) {
        newDetail[i] = new Array(n);
    }
    for (var i = 0; i < n; i++) {
        for (var j = 0; j < n; j++) {
            newDetail[j][n - 1 - i] = detail[i][j];
        }
    }
    return newDetail;
}

function correctPosition(detail, currentX, currentY) {
    for (let y = 0; y < detail.length; y++) {
        for (let x = 0; x < detail[y].length; x++) {
            if (detail[y][x] == 1 && (currentX + x < 0
                || currentY + y >= field.length
                || currentX + x >= field[0].length
                || field[currentY + y][currentX + x])) {
                return false;
            }
        }
    }
    return true;
}

function placeDetail() {
    for (let y = 0; y < currentDetail.view.length; y++) {
        for (let x = 0; x < currentDetail.view[y].length; x++) {
            if (currentDetail.view[y][x] == 1) {
                if (currentDetail.currentY + y <= 0) {
                    return gameOver();
                }
                field[currentDetail.currentY + y][currentDetail.currentX + x] = currentDetail.index + 1;
            }
        }
    }
    let combo = 0;
    for (let y = field.length - 1; y >= 0;) {
        let count = 0;
        for (let x = 0; x < field[y].length; x++) {
            if (field[y][x] == 0) {
                count++;
            }
        }
        if (count == 0) {
            newScore += 100;
            combo++;
            if (newScore >= newLevel * 400) {
                newLevel++;
            }
            for (let newY = y; newY >= 0; newY--) {
                for (let x = 0; x < 10; x++) {
                    field[newY][x] = field[newY - 1][x];
                }
            }
        }
        else {
            y--;
        }
    }
    if (combo > 1) {
        newScore += 25 * (combo - 1);
    }
    score.innerHTML = newScore;
    level.innerHTML = newLevel;
    currentDetail = nextDetail;
    nextDetail = getDetail();
}

function gameOver() {
    cancelAnimationFrame(rAF);
    endFlag = true;
    localStorage['score'] = newScore;
    window.location.href = "end.html"

}

document.addEventListener("keydown", function (event) {
    if (endFlag) return;
    if (event.key == "ArrowDown") {
        if (correctPosition(currentDetail.view, currentDetail.currentX, currentDetail.currentY + 1)) {
            currentDetail.currentY++;
        }
        else {
            placeDetail();
        }
    } else if (event.key == "ArrowUp") {
        if (correctPosition(rotateDetail(currentDetail.view), currentDetail.currentX, currentDetail.currentY)) {
            currentDetail.view = rotateDetail(currentDetail.view);
        }
    } else if (event.key == "ArrowRight") {
        if (correctPosition(currentDetail.view, currentDetail.currentX + 1, currentDetail.currentY)) {
            currentDetail.currentX++;
        }
    } else if (event.key == "ArrowLeft") {
        if (correctPosition(currentDetail.view, currentDetail.currentX - 1, currentDetail.currentY)) {
            currentDetail.currentX--;
        }
    } else if (event.key == " ") {
        let i = 0;
        while (correctPosition(currentDetail.view, currentDetail.currentX, currentDetail.currentY + i)) {
            i++;
        }
        currentDetail.currentY += i - 1;
        placeDetail();
    }
});

function loop() {
    if (!endFlag) {
        rAF = requestAnimationFrame(loop);
        context1.clearRect(0, 0, canvas1.width, canvas1.height);
        context2.clearRect(0, 0, canvas2.width, canvas2.height);
        for (let y = 0; y < field.length; y++) {
            for (let x = 0; x < field[y].length; x++) {
                if (field[y][x]) {
                    context1.fillStyle = colors[field[y][x] - 1];
                    context1.fillRect(x * oneSize, y * oneSize, oneSize - 1, oneSize - 1);
                }
                else {
                    context1.fillStyle = 'rgb(254, 225, 193)';
                    context1.fillRect(x * oneSize, y * oneSize, oneSize - 1, oneSize - 1);
                }
            }
        }
        shot++;
        if (shot > (60 / newLevel)) {
            shot = 0;
            if (correctPosition(currentDetail.view, currentDetail.currentX, currentDetail.currentY + 1)) {
                currentDetail.currentY++;
            }
            else {
                placeDetail();
            }
        }
        for (let y = 0; y < currentDetail.view.length; y++) {
            for (let x = 0; x < currentDetail.view[y].length; x++) {
                if (currentDetail.view[y][x]) {
                    context1.fillStyle = colors[currentDetail.index];
                    context1.fillRect((currentDetail.currentX + x) * oneSize, (currentDetail.currentY + y) * oneSize, oneSize - 1, oneSize - 1);
                }

            }
        }
        let variance = 4 - nextDetail.view.length;
        for (let y = 0; y < 4; y++) {
            for (let x = 0; x < 4; x++) {
                if (y >= variance && x >= variance) {
                    if (nextDetail.view[y - variance][x - variance]) {
                        context2.fillStyle = colors[nextDetail.index];
                        context2.fillRect(x * twoSize, y * twoSize, twoSize - 1, twoSize - 1);
                    }
                    else {
                        context2.fillStyle = 'rgb(254, 225, 193)';
                        context2.fillRect(x * twoSize, y * twoSize, twoSize - 1, twoSize - 1);
                    }
                }
                else {
                    context2.fillStyle = 'rgb(254, 225, 193)';
                    context2.fillRect(x * twoSize, y * twoSize, twoSize - 1, twoSize - 1);
                }
            }
        }
    }
    else {
        game_over();
    }
}

rAF = requestAnimationFrame(loop);