# RIGHT toggle

def on_button_pressed_a():
    global rightOn, leftOn, hazardOn
    rightOn = not (rightOn)
    leftOn = False
    hazardOn = False
input.on_button_pressed(Button.A, on_button_pressed_a)

# LEFT toggle

def on_button_pressed_b():
    global leftOn, rightOn, hazardOn
    leftOn = not (leftOn)
    rightOn = False
    hazardOn = False
input.on_button_pressed(Button.B, on_button_pressed_b)

# HORN

def on_logo_pressed():
    global hazardOn, leftOn, rightOn
    hazardOn = not (hazardOn)
    leftOn = False
    rightOn = False
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

hazardOn = False
leftOn = False
rightOn = False
wait = 350
music.set_built_in_speaker_enabled(True)
# Start LOW
pins.digital_write_pin(DigitalPin.P2, 0)
pins.digital_write_pin(DigitalPin.P1, 0)

def on_forever():
    if hazardOn:
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P1, 1)
        music.play_tone(650, music.beat(BeatFraction.SIXTEENTH))
        basic.pause(wait)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
        music.play_tone(550, music.beat(BeatFraction.SIXTEENTH))
        basic.pause(wait)
    elif leftOn:
        pins.digital_write_pin(DigitalPin.P2, 1)
        music.play_tone(650, music.beat(BeatFraction.SIXTEENTH))
        basic.pause(wait)
        pins.digital_write_pin(DigitalPin.P2, 0)
        music.play_tone(550, music.beat(BeatFraction.SIXTEENTH))
        basic.pause(wait)
    elif rightOn:
        pins.digital_write_pin(DigitalPin.P1, 1)
        music.play_tone(650, music.beat(BeatFraction.SIXTEENTH))
        basic.pause(wait)
        pins.digital_write_pin(DigitalPin.P1, 0)
        music.play_tone(550, music.beat(BeatFraction.SIXTEENTH))
        basic.pause(wait)
    else:
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
basic.forever(on_forever)
