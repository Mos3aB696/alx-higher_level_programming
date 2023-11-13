#!/usr/bin/python3
import unittest
from models.base import Base
"""This Is Testing Class"""


class TestBase(unittest.TestCase):
    """Test Base Class"""

    def test_if_id_provided(self):
        userOne = Base(12)
        self.assertEqual(userOne.id, 12)

    def test_if_not_provided(self):
        userOne = Base()
        userTwo = Base()
        userThree = Base()

        self.assertEqual(userOne.id, 1)
        self.assertEqual(userTwo.id, 2)
        self.assertEqual(userThree.id, 3)


if __name__ == '__main__':
    unittest.main()
