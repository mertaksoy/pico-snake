import unittest
from snake import Snake


class SnakeTest(unittest.TestCase):
    def test_move(self):
        snake = Snake()
        self.assertEqual(snake.llist.head.x, 2)
        snake.move()
        self.assertEqual(snake.llist.head.x, 3)


if __name__ == '__main__':
    unittest.main()
