export let soundManager={
    clips:{},
    context: null,
    gainNode: null,
    loaded: false,

    init: function () {
        this.context = new AudioContext();
        this.context.resume()
        this.gainNode = this.context.createGain ? this.context.createGain() : this.context.createGainNode()
        this.gainNode.connect(this.context.destination);
        this.loadArray(["/sounds/lose.mp3", "/sounds/back.mp3", "/sounds/pobeda.mp3"]);
    },

    load: function (path, callback) {
        if(this.clips[path]) {
            callback(this.clips[path])
            return
        }
        let clip = {path: path, buffer: null, loaded: false}
        clip.play = function (volume, loop) {
            soundManager.play(this.path,{looping: loop? loop: false, volume: volume ? volume : 1})
        }
        this.clips[path] = clip

        let request = new XMLHttpRequest()
        request.open("GET",path,true)
        request.responseType='arraybuffer'
        request.onload = function() {
            soundManager.context.decodeAudioData(request.response, function (buffer) {
                clip.buffer = buffer
                clip.loaded = true
                callback(clip)
            })
        }
        request.send()
    },

    loadArray: function (array) {
        for(let i = 0; i < array.length; i++) {
            soundManager.load(array[i], function () {
                if (array.length === Object.keys(soundManager.clips).length) {
                    for (let sd in soundManager.clips)
                        if (!soundManager.clips[sd].loaded) return
                    soundManager.loaded = true
                }
            })
        }
    },

    play: function (path, setting) {
        if (!soundManager.loaded) {
            setTimeout(function () { soundManager.play(path,setting) }, 1000)
            return
        }

        let looping = false
        let volume = 1

        if(setting) {
            if (setting.looping)
                looping = setting.looping
            if (setting.volume)
                volume = setting.volume
        }

        let sd = this.clips[path]
        if(sd === null)
            return false

        let sound = soundManager.context.createBufferSource()
        sound.buffer = sd.buffer
        sound.connect(soundManager.gainNode)
        sound.loop = looping
        soundManager.gainNode.gain.value = volume
        sound.start(0)
        return true
    }
};