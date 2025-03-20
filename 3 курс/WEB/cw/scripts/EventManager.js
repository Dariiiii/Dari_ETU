import { physicsManager } from "./PhisycsManager.js"
export class EventManager {
    bind = {
        87: 'up',
        83: 'down',
        65: 'left',
        68: 'right'
    }
    actions = {
        'up': false,
        'left': false,
        'right': false,
        'down': false,
    }
    setup(canvas) {
        canvas.addEventListener("mousedown", this.onMouseDown)
        document.body.addEventListener("keydown", this.onKeyDown.bind(this));
        document.body.addEventListener("keyup", this.onKeyUp.bind(this));
    }
    onKeyDown(event) {
        const action = this.bind[event.keyCode]
        if (action)
            this.actions[action] = true
    }
    onKeyUp(event) {
        const action = this.bind[event.keyCode]
        if (action)
            this.actions[action] = false
    }
    onMouseDown(event) {
        const x = event.offsetX - 16
        const y = event.offsetY - 16
        physicsManager.attackEnemies(x, y)

    }


}

export let eventManager = new EventManager()