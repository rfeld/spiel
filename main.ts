input.onButtonPressed(Button.A, function () {
    BatX += -1
    BatX = Math.max(0, BatX)
    Schlaeger.set(LedSpriteProperty.X, BatX)
})
input.onButtonPressed(Button.AB, function () {
    BatX = 2
    Schlaeger.set(LedSpriteProperty.X, BatX)
})
input.onButtonPressed(Button.B, function () {
    BatX += 1
    BatX = Math.min(4, BatX)
    Schlaeger.set(LedSpriteProperty.X, BatX)
})
let ball: game.LedSprite = null
let ballDa = 0
let Schlaeger: game.LedSprite = null
let BatX = 0
game.setLife(3)
music.setVolume(32)
BatX = 2
Schlaeger = game.createSprite(BatX, 4)
let waittime = 300
basic.forever(function () {
    if (ballDa == 0) {
        ball = game.createSprite(randint(0, 4), 0)
        ballDa = 1
    } else {
        ball.change(LedSpriteProperty.Y, 1)
    }
    if (ball.isTouching(Schlaeger)) {
        music.playTone(262, music.beat(BeatFraction.Eighth))
        game.addScore(1)
        waittime += -1
        ball.delete()
        ballDa = 0
    } else {
        if (ball.get(LedSpriteProperty.Y) >= 4 && !(ball.isDeleted())) {
            music.playTone(131, music.beat(BeatFraction.Eighth))
            ball.delete()
            game.removeLife(1)
            waittime += -1
            ballDa = 0
        }
    }
    if (game.isGameOver()) {
        waittime = 300
    }
    basic.pause(waittime)
})
