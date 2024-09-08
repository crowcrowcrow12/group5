import pygame as pg
from paddle import Paddle
from bricks import Bricks
from ball import Ball
from scores import ScoreBoard
from settings import *


pg.init()


screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Breakout Game")

clock = pg.time.Clock()


# OBJECTS
pad = Paddle(paddle_x, paddle_y)
bricks = Bricks(screen, brick_width, brick_height)
ball = Ball(ball_x, ball_y, screen)
score = ScoreBoard(text_x, color, screen)
score.set_high_score()


sound_played = False
running = True
while running:
    screen.fill(BG_COLOR)
    score.show_scores()
    pad.appear(screen)
    bricks.show_bricks()

    # Check for quit game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # score.record_high_score()
            running = False

    # Check if there are more trials
    if score.is_game_over():
        if not sound_played:
            pg.mixer.Sound.play(game_end)
            sound_played = True
        score.game_over()

    # Check if all bricks are broken
    elif len(bricks.bricks) <= 0:
        if not sound_played:
            pg.mixer.Sound.play(win_game)
            sound_played = True
        score.success()

    else:
        ball.move()

    # Check if ball hits the x-axis above
    ball.check_for_contact_on_x()

    # Check if ball hits y-axis
    ball.check_for_contact_on_y()

    # Check if ball falls off
    if ball.y + ball.radius >= 580:
        pg.mixer.Sound.play(dropping_ball)
        ball.y = pad.y - ball.radius
        pg.time.delay(2000)
        score.lives -= 1
        ball.bounce_y()

    # Check if ball hits paddle
    if (pad.rect.y < ball.y + ball.radius < pad.rect.y + pad.height
            and
            pad.rect.x < ball.x + ball.radius < pad.rect.x + pad.width):

        pg.mixer.Sound.play(pad_hit)
        ball.bounce_y()
        ball.y = pad.y - ball.radius

    # Check if ball hits brick
    for brick in bricks.bricks:
        if brick.collidepoint(ball.x, ball.y - ball.radius) or brick.collidepoint(ball.x, ball.y + ball.radius):
            pg.mixer.Sound.play(brick_breaking)
            bricks.bricks.remove(brick)
            ball.bounce_y()
            score.score += 1

    # Check for key presses
    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        pad.move_right()

    if keys[pg.K_LEFT]:
        pad.move_left()

    # Restart game
    if keys[pg.K_0]:
        if score.is_game_over():
            score.score = 0
            score.lives = 5
            score.sound_played = False
            bricks.bricks.clear()
            bricks.set_values()

    pg.display.flip()
    clock.tick(60)
    