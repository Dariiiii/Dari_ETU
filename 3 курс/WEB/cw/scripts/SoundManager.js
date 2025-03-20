export class SoundManager {
    constructor() {
        this.clips = {}
        this.context = null;
        this.gainNode = null;//главный узел(громкость)
        this.loaded = false;
    }

    init() {
        this.context = new AudioContext();
        this.context.resume();
        this.gainNode = this.context.createGain() ? this.context.createGain() : this.context.createGainNode();
        this.gainNode.connect(this.context.destination)//подключение к динамикам
        this.loadArray(["../sound/damage.mp3", "../sound/eat.mp3", "../sound/coin.mp3"])
    }

    load(path, callback) {
        if (this.clips[path]) {//проверяем что загружены
            callback(this.clips[path]);
            return;
        }
        let clip = { path: path, buffer: null, loaded: false };
        clip.play = ((volume, loop) => {
            this.play(path, { looping: loop ? loop : false, volume: volume ? volume : 1 });
        });
        this.clips[path] = clip;
        let request = new XMLHttpRequest();
        request.open("GET", path, true);
        request.responseType = "arraybuffer"
        request.onload = (() => {
            this.context.decodeAudioData(request.response,
                ((buffer) => {
                    clip.buffer = buffer
                    clip.loaded = true
                    callback(clip)
                }))
        })
        request.send()
    }

    loadArray(array) {
        for (let i = 0; i < array.length; i++) {
            this.load(array[i], () => {
                const loadedSounds = Object.keys(this.clips)
                if (array.length === loadedSounds.length && loadedSounds.every(sd => this.clips[sd].loaded)) {
                    this.loaded = true;
                }
            })
        }
    }

    play(path, setting) {
        if (!this.loaded) {
            setTimeout(() => { this.play(path, setting) }, 1000)
            return;
        }
        let looping = false;
        let volume = 1;
        if (setting) {
            if (setting.volume)
                volume = setting.volume
        }
        let sd = this.clips[path];
        if (sd === null)
            return false;
        let sound = this.context.createBufferSource();
        sound.buffer = sd.buffer;
        sound.connect(this.gainNode);
        sound.loop = looping;
        this.gainNode.gain.value = volume;
        sound.start(0);
        // console.log("true")
        return true;
    }
}

export let soundManager = new SoundManager();
