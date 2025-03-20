import express from 'express';
const app = express()
import { readFileSync } from "fs";
import {createReadStream} from "fs";
import { createServer } from "https";

const PORT = 228;
let paths = ["./first_map2.json","./second_map2.json","./first_tower2.json","./second_tower2.json"];
let jsons = ["./sprites_h.json","./sprites_tools.json","./sprites_treasure.json","./sprites_v.json","./sprites_hl.json", "./sprites_tp.json"];
const map1 = readFileSync(paths[0]);
const map1_j = JSON.parse(map1);
const map2 = readFileSync(paths[1]);
const map2_j = JSON.parse(map2);
const tower1 = readFileSync(paths[2]);
const tower1_j = JSON.parse(tower1);
const tower2 = readFileSync(paths[3]);
const tower2_j = JSON.parse(tower2);

const sprites_h = readFileSync(jsons[0]);
const sprites_hj = JSON.parse(sprites_h);
const sprites_tools = readFileSync(jsons[1]);
const sprites_toolsj = JSON.parse(sprites_tools);
const sprites_treasure = readFileSync(jsons[2]);
const sprites_treasurej = JSON.parse(sprites_treasure);
const sprites_v = readFileSync(jsons[3]);
const sprites_vj = JSON.parse(sprites_v);
const sprites_hl = readFileSync(jsons[4]);
const sprites_hlj = JSON.parse(sprites_hl);
const sprites_tp = readFileSync(jsons[5]);
const sprites_tpj = JSON.parse(sprites_tp)
app.use(express.json());

app.use("/scripts", express.static('./scripts'));
app.use("/styles", express.static('./stylesheets'));
app.use("/images",express.static('./images'));
app.use("/sounds", express.static('./sounds'));
app.set("views", "./pages");

let key  = readFileSync('./example.key', 'utf8');
let cert = readFileSync('./example.crt', 'utf8');

const httpsServer = createServer({key, cert}, app);

app.get("/", (req, res) => {
    res.sendFile("C:/WEB/course_work/pages/index.html")
})

app.get("/lose",(req,res) => {
    res.sendFile("C:/WEB/course_work/pages/game_over.html");
})

app.get("/game", (req, res) => {
    res.sendFile("C:/WEB/course_work/pages/mainpage.html")
})
app.get("/paths", (req,res) =>{
    res.json({map1_j,map2_j,tower1_j,tower2_j});
})

app.get("/jsons", (req,res) => {
    res.json({sprites_hj,sprites_toolsj,sprites_treasurej, sprites_vj, sprites_hlj,sprites_tpj});
})
app.get("/sounds/lose.mp3",(req,res) => {
    const filePath = req.path;
    const stream = createReadStream(filePath);
  
    stream.on('error', (err) => {
        console.error('Ошибка чтения файла:', err);
        res.status(500).send('Ошибка сервера');
  });
  
  res.set('Content-Type', 'audio/mpeg'); // Устанавливаем тип контента как аудио MPEG
  stream.pipe(res); // Передаем содержимое файла в ответ клиенту
})

app.get("/sounds/back.mp3",(req,res) => {; // Получаем путь к файлу из параметра запроса
    const filePath = req.path;
    const stream = createReadStream(filePath);
  
    stream.on('error', (err) => {
        console.error('Ошибка чтения файла:', err);
        res.status(500).send('Ошибка сервера');
  });
  
  res.set('Content-Type', 'audio/mpeg'); // Устанавливаем тип контента как аудио MPEG
  stream.pipe(res); // Передаем содержимое файла в ответ клиенту
})

app.get("/sounds/pobeda.mp3",(req,res) => {
    const filePath = req.path;
    const stream = createReadStream(filePath);
  
    stream.on('error', (err) => {
        console.error('Ошибка чтения файла:', err);
        res.status(500).send('Ошибка сервера');
  });
  
  res.set('Content-Type', 'audio/mpeg'); // Устанавливаем тип контента как аудио MPEG
  stream.pipe(res); // Передаем содержимое файла в ответ клиенту
})

app.get('*',(req,res) =>{
    res.status(404);
    res.end("Page not found");
  });

httpsServer.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
})