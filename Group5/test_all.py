import unittest
import pygame as pg
from ball import Ball
from paddle import Paddle
from bricks import Bricks
from scores import ScoreBoard
from settings import *

class TestBall(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.ball = Ball(ball_x, ball_y, self.screen)

    def test_init(self):
        self.assertEqual(self.ball.x, ball_x)
        self.assertEqual(self.ball.y, ball_y)
        self.assertEqual(self.ball.radius, ball_radius)

    def test_move(self):
        initial_x, initial_y = self.ball.x, self.ball.y
        self.ball.move()
        self.assertNotEqual((self.ball.x, self.ball.y), (initial_x, initial_y))

    def test_bounce_x(self):
        initial_x_speed = self.ball.x_speed
        self.ball.bounce_x()
        self.assertEqual(self.ball.x_speed, -initial_x_speed)

    def test_bounce_y(self):
        initial_y_speed = self.ball.y_speed
        self.ball.bounce_y()
        self.assertEqual(self.ball.y_speed, -initial_y_speed)

    def test_check_for_contact_on_x(self):
        # Test left boundary
        self.ball.x = self.ball.radius
        self.ball.x_speed = -2  # Ensure it's moving left initially
        self.ball.check_for_contact_on_x()
        self.assertTrue(self.ball.x_speed > 0)

        # Test right boundary
        self.ball.x = self.screen.get_width() - self.ball.radius
        self.ball.x_speed = 2  # Ensure it's moving right initially
        self.ball.check_for_contact_on_x()
        self.assertTrue(self.ball.x_speed < 0)

    def test_check_for_contact_on_y(self):
        self.ball.y = self.ball.radius
        self.ball.check_for_contact_on_y()
        self.assertTrue(self.ball.y_speed > 0)

    def tearDown(self):
        pg.quit()

class TestPaddle(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.paddle = Paddle(paddle_x, paddle_y)

    def test_move_right(self):
        initial_x = self.paddle.rect.x
        self.paddle.move_right()
        self.assertEqual(self.paddle.rect.x, initial_x + self.paddle.speed)

    def test_move_left(self):
        self.paddle.rect.x = 100  # Ensure we're not at the left edge
        initial_x = self.paddle.rect.x
        self.paddle.move_left()
        self.assertEqual(self.paddle.rect.x, initial_x - self.paddle.speed)

    def test_move_right_boundary(self):
        self.paddle.rect.right = WIDTH  # Place paddle at right edge
        initial_x = self.paddle.rect.x
        self.paddle.move_right()
        self.assertEqual(self.paddle.rect.x, initial_x)

    def test_move_left_boundary(self):
        self.paddle.rect.left = 0  # Place paddle at left edge
        self.paddle.move_left()
        self.assertEqual(self.paddle.rect.left, 0)

    def tearDown(self):
        pg.quit()

class TestBricks(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.bricks = Bricks(self.screen, brick_width, brick_height)

    def test_init(self):
        self.assertIsNotNone(self.bricks.bricks)
        self.assertIsNotNone(self.bricks.brick_colors)
        self.assertEqual(len(self.bricks.bricks), len(self.bricks.brick_colors))

    def test_set_values(self):
        self.bricks.bricks.clear()
        self.bricks.brick_colors.clear()
        self.bricks.set_values()
        self.assertGreater(len(self.bricks.bricks), 0)
        self.assertGreater(len(self.bricks.brick_colors), 0)

    def test_brick_positions(self):
        for brick in self.bricks.bricks:
            self.assertGreaterEqual(brick.x, 10)
            self.assertLess(brick.x, 550)
            self.assertGreaterEqual(brick.y, 100)
            self.assertLess(brick.y, 200)

    def test_brick_colors(self):
        for color in self.bricks.brick_colors:
            self.assertIn(color, ['navy', 'white', 'light blue'])

    def tearDown(self):
        pg.quit()

class TestScoreBoard(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.scoreboard = ScoreBoard(text_x, color, self.screen)

    def test_init(self):
        self.assertEqual(self.scoreboard.score, 0)
        self.assertEqual(self.scoreboard.lives, 5)

    def test_is_game_over(self):
        self.scoreboard.lives = 1
        self.assertFalse(self.scoreboard.is_game_over())
        self.scoreboard.lives = 0
        self.assertTrue(self.scoreboard.is_game_over())

    def test_set_high_score(self):
        # Write a known high score to the file
        with open("records.txt", "w") as f:
            f.write("100")
        self.scoreboard.set_high_score()
        self.assertEqual(self.scoreboard.high_score, 100)

    def test_record_high_score(self):
        self.scoreboard.high_score = 50
        self.scoreboard.score = 100
        self.scoreboard.record_high_score()
        with open("records.txt", "r") as f:
            recorded_score = int(f.read())
        self.assertEqual(recorded_score, 100)

    def tearDown(self):
        pg.quit()
        # Clean up the test file
        import os
        if os.path.exists("records.txt"):
            os.remove("records.txt")

if __name__ == '__main__':
    unittest.main()
