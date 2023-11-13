#!/usr/bin/python3
"""Test suit for the square class"""
import os
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square

class TestSquare(TestCase):
    """ Testing the Square class and its methods"""

    def test_square(self):
        """Test the area() method of the Square class"""
        sq = Square(5)
        self.assertEqual(sq.area(), 25)

    def test_square_create(self):
        """ Test creating Square instances from dictionaries"""
        with self.subTest():
            sq = Square.create(**{'id': 33})
            self.assertIsInstance(sq, Square)
            self.assertEqual(sq.id, 33)

        with self.subTest():
            sq = Square.create(**{'id': 89, 'size': 1})
            self.assertEqual(sq.size, 1)

        with self.subTest():
            sq = Square.create(**{'id': 89, 'size': 1, 'x': 11})
            self.assertEqual(sq.x, 11)

        with self.subTest():
            sq = Square.create(**{'id': 89, 'size': 1, 'x': 11, 'y': 44})
            self.assertEqual(sq.y, 44)

    def test_square_save_to_file(self):
        """ Test saving Square instances to a JSON file"""
        with self.subTest():
            Square.save_to_file(None)
            with open("Square.json", "r") as file:
                self.assertEqual(file.read(), '[]')

        with self.subTest():
            Square.save_to_file([Square(1)])
            with open("Square.json", "r") as file:
                self.assertEqual(file.read(), '[{"id": 33, "size": 1, "x": 0, "y": 0}]')

        with self.subTest():
            Square.save_to_file([])
            with open("Square.json", "r") as file:
                self.assertEqual(file.read(), '[]')

    def test_load_from_file(self):
        """Test loading from a non-existent file"""
        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 3)
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_load_from_file_file_exists(self):
        """Test loading from an existing file"""

        # Create a Square instance, save it to a JSON file, and load it
        r1 = Square(5, 0, 0, 3)
        Square.save_to_file([r1])
        instances = Square.load_from_file()

        # Assert that the loaded instance matches the original instance
        self.assertEqual(len(instances), 1)
        self.assertEqual(instances[0].id, r1.id)
