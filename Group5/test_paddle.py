import unittest
from paddle import Paddle

class TestPaddle(unittest.TestCase):
    def test_initial_position(self):
        pad = Paddle(100, 200)
        self.assertEqual(pad.x, 100)
        self.assertEqual(pad.y, 200)


if __name__ == '__main__':
    unittest.main()