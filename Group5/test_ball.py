# test for ball.py
import unittest
import pygame
from ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((550, 600))
        self.ball = Ball(250, 540, self.screen)

    def test_init(self):
        self.assertEqual(self.ball.x, 250)
        self.assertEqual(self.ball.y, 540)

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

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
    
