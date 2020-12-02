def on_button_pressed_a():
    global BatX
    BatX += -1
    BatX = max(0, BatX)
    Schlaeger.set(LedSpriteProperty.X, BatX)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global BatX
    BatX = 2
    Schlaeger.set(LedSpriteProperty.X, BatX)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global BatX
    BatX += 1
    BatX = min(4, BatX)
    Schlaeger.set(LedSpriteProperty.X, BatX)
input.on_button_pressed(Button.B, on_button_pressed_b)

ball: game.LedSprite = None
Schlaeger: game.LedSprite = None
BatX = 0
game.set_life(3)
basic.show_icon(IconNames.HAPPY)
music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
    MelodyOptions.ONCE)
music.set_volume(32)
ballDa = 0
BatX = 2
Schlaeger = game.create_sprite(2, 4)

def on_forever():
    global ball, ballDa
    if ballDa == 0:
        ball = game.create_sprite(randint(0, 4), 0)
        ballDa = 1
    else:
        ball.change(LedSpriteProperty.Y, 1)
    if ball.is_touching(Schlaeger):
        music.play_tone(262, music.beat(BeatFraction.EIGHTH))
        game.add_score(1)
    if ball.get(LedSpriteProperty.Y) >= 4:
        ball.delete()
        game.remove_life(1)
        ballDa = 0
    if game.score() >= 5:
        game.game_over()
    basic.pause(300)
basic.forever(on_forever)
