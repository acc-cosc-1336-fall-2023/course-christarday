import unittest
from src.homework.j_classes.class_a import die  # Import the die class

class tests_classes(unittest.TestCase):
    def test_roll(self):
        my_die = die()
        my_die.roll()
        rolled_value = my_die.get_rolled_value()
        self.assertTrue(1 <= rolled_value <= 6)

    def test_multiple_rolls(self):
        my_die = die()
        for _ in range(3):
            my_die.roll()
            rolled_value = my_die.get_rolled_value()
            self.assertTrue(1 <= rolled_value <= 6)

if __name__ == '__main__':
    unittest.main()





