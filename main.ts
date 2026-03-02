// RIGHT toggle
input.onButtonPressed(Button.A, function () {
    rightOn = !(rightOn)
    leftOn = false
    hazardOn = false
})
// LEFT toggle
input.onButtonPressed(Button.B, function () {
    leftOn = !(leftOn)
    rightOn = false
    hazardOn = false
})
// HORN
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    hazardOn = !(hazardOn)
    leftOn = false
    rightOn = false
})
let hazardOn = false
let leftOn = false
let rightOn = false
let wait = 350
music.setBuiltInSpeakerEnabled(true)
// Start LOW
pins.digitalWritePin(DigitalPin.P2, 0)
pins.digitalWritePin(DigitalPin.P1, 0)
basic.forever(function () {
    if (hazardOn) {
        pins.digitalWritePin(DigitalPin.P2, 1)
        pins.digitalWritePin(DigitalPin.P1, 1)
        music.playTone(650, music.beat(BeatFraction.Sixteenth))
        basic.pause(wait)
        pins.digitalWritePin(DigitalPin.P2, 0)
        pins.digitalWritePin(DigitalPin.P1, 0)
        music.playTone(550, music.beat(BeatFraction.Sixteenth))
        basic.pause(wait)
    } else if (leftOn) {
        pins.digitalWritePin(DigitalPin.P2, 1)
        music.playTone(650, music.beat(BeatFraction.Sixteenth))
        basic.pause(wait)
        pins.digitalWritePin(DigitalPin.P2, 0)
        music.playTone(550, music.beat(BeatFraction.Sixteenth))
        basic.pause(wait)
    } else if (rightOn) {
        pins.digitalWritePin(DigitalPin.P1, 1)
        music.playTone(650, music.beat(BeatFraction.Sixteenth))
        basic.pause(wait)
        pins.digitalWritePin(DigitalPin.P1, 0)
        music.playTone(550, music.beat(BeatFraction.Sixteenth))
        basic.pause(wait)
    } else {
        pins.digitalWritePin(DigitalPin.P2, 0)
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
})
