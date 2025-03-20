import {BINDS} from "./binds.js"

export class EventManager{
    actions = {}
    eventListener = null
    keyDown = null
    keyUp = null

    constructor() {
        this.actions = {
            'up': false,
            'left': false,
            'right': false,
            'down': false
        }

        this.eventListener = ((canvas) => {
            document.body.addEventListener("keydown", this.keyDown)
            document.body.addEventListener("keyup", this.keyUp)
        })

        this.keyDown =((event) => {
            const action = BINDS[event.keyCode]
            if(action)
                this.actions[action] = true
        })

        this.keyUp = ((event) => {
            const action = BINDS[event.keyCode]
            if(action)
                this.actions[action] = false
        })

    }
}

export let eventManager = new EventManager()