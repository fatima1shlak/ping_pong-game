from pygame import *
from os import curdir
from random import uniform
from libs.classes.game import Game
from libs.classes.player import Player
from libs.classes.object import Object

font.init()
game = Game()

game.create_window(_width=800, _height=500)
game.set_background("res/sprites/bg.jpg")

paddle = Player(
    _img_path="res/sprites/pixil-frame-0.png",
    _img_width=100,
    _img_height=100,
    _img_col=(255, 255, 255),
    _x=0,
    _y=0
)
game.objects.append(paddle)

padding = 150
paddle_start_x = (game.win_width) - (game.win_height/2) + padding
paddle_start_y = (game.win_width/2) - (paddle.img_height/2)

paddle.set_x(paddle_start_x)
paddle.set_y(paddle_start_y)


paddle2 = Player(
    _img_path="res/sprites/pixil-frame-0.png",
    _img_width=100,
    _img_height=100,
    _img_col=(255, 255, 255),
    _x=0,
    _y=0
)

game.objects.append(paddle2)

paddle2_start_x = game.win_width/2 - game.win_height/2 -padding
paddle2_start_y = (game.win_width/2) - (paddle.img_height/2)

paddle2.set_x(paddle2_start_x)
paddle2.set_y(paddle2_start_y)

balls = []

def add_ball():
    ball = Object(
        _img_path="res/sprites/ball.png",
        _img_width=50,
        _img_height=50,
        _img_col=(255, 255, 255),
        _x=game.win_width / 2,
        _y=game.win_height / 2
    )

    ball.vx = uniform(-5, 5)
    ball.vy = uniform(-5, 5)
    game.objects.append(ball)
    balls.append(ball)
add_ball()

score = 0

def game_loop():
    global paddle, paddle2, add_ball, score

        
    paddle.set_limit_x(1, game.win_width - paddle.img_width)
    paddle.set_limit_y(1, game.win_height - paddle.img_height)

        
    paddle2.set_limit_x(1, game.win_width - paddle2.img_width)
    paddle2.set_limit_y(1, game.win_height - paddle2.img_height)


    if game.is_pressed(K_UP):
        paddle.set_y(paddle.get_pos_y() - 5)

    if game.is_pressed(K_DOWN):
        paddle.set_y(paddle.get_pos_y() + 5)

    paddle.update()

    if game.is_pressed(K_UP):
        paddle2.set_y(paddle2.get_pos_y() - 5)

    if game.is_pressed(K_DOWN):
        paddle2.set_y(paddle2.get_pos_y() + 5)

    paddle2.update()

    for ball in balls:
        ball.set_x(ball.get_pos_x() + ball.vx)
        ball.set_y(ball.get_pos_y() + ball.vy)

        if ball.get_pos_y() <= 0 or ball.get_pos_y() >= game.win_height - ball.img_height:
            ball.vy *= -1

        if ball.get_rect().colliderect(paddle.get_rect()) or ball.get_rect().colliderect(paddle2.get_rect()):
            ball.vx *= -1
            score +=1

        if ball.get_pos_x() <= 0 or ball.get_pos_x() >= game.win_width - ball.img_width:
            ball.set_x(game.win_width / 2)
            ball.set_y(game.win_height / 2)
            score = 0

        if ball.get_pos_x() <= 0 or ball.get_pos_x() >= game.win_width - ball.img_width:
            ball.set_x(game.win_width / 2)
            ball.set_y(game.win_height / 2)
            # ball.vx = uniform(-3, 3)
            # ball.vy = uniform(-3, 3)

    game.draw_text(f"Score: {score}")
   

    for obj in game.objects:
        obj.draw(game.window)

game.run(game_loop)