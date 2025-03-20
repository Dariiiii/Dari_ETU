const canvas = document.getElementById('table');
const context = canvas.getContext('2d');

context.font = '23px Comic Sans MS ';
context.fillStyle = 'white';
context.shadowColor = 'gray';
context.shadowBlur = 5;

if (localStorage.getItem('tableOfRecords') == null) {
    let arr = [];
    for (let i = 0; i < 11; i++) {
        arr.push({
            score: 0,
            name: " "
        });
    }
    localStorage.setItem('tableOfRecords', JSON.stringify(arr));
}

let newRecord = {
    score: localStorage.getItem('score'),
    name: localStorage.getItem('username')
};

let tableOfRecords = JSON.parse(localStorage.getItem('tableOfRecords'));

if (newRecord.score > tableOfRecords[9].score && newRecord.score != null) {
    tableOfRecords[10] = newRecord;
    tableOfRecords.sort((a, b) => b.score - a.score);
    localStorage.setItem('tableOfRecords', JSON.stringify(tableOfRecords));
}
let i = 0;
while (i < 10) {
    context.fillText((i + 1) + ' место : ' + tableOfRecords[i].score + ' очков,  игрок ' + tableOfRecords[i].name + ';', 0, (i + 1) * 25);
    i++;
}
localStorage.removeItem('score');
localStorage.setItem('tableOfRecords', JSON.stringify(tableOfRecords));
