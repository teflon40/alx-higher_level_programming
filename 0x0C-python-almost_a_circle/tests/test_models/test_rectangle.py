#!/usr/bin/python3
"""Test suite for the Rectangle class."""
import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(TestCase):
    """Tests the functionality of the derived Base class, Rectangle."""

    def test_rectangle_w_h(self):
        """Test case for initializing width and height attributes."""
        r1_obj = Rectangle(1, 2)
        self.assertEqual(r1_obj.width, 1)
        self.assertEqual(r1_obj.height, 2)

    def test_x_cordinates(self):
        """Test case for initializing x coordinate."""
        r1_obj = Rectangle(1, 2, 3)
        self.assertEqual(r1_obj.x, 3)

    def test_y_cordinates(self):
        """Test case for initializing y coordinate."""
        r1_obj = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1_obj.y, 4)

    def test_width_validation(self):
        """Test case for validating width attribute."""
        with self.assertRaises(TypeError):
            r1_obj = Rectangle("1", 2)
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(0, 2)

    def test_height_validation(self):
        """Test case for validating height attribute value."""
        with self.assertRaises(TypeError):
            r1_obj = Rectangle(1, "2")
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(10, 0)

    def test_x_validation(self):
        """Test case for validating x coordinate value."""
        with self.assertRaises(TypeError):
            r1_obj = Rectangle(1, 3, "2")
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(1, 3, -1)

    def test_y_validation(self):
        """Test case for validating y coordinate value."""
        with self.assertRaises(TypeError):
            r1_obj = Rectangle(1, 3, 4, "2")
        with self.assertRaises(ValueError):
            r1_obj = Rectangle(1, 3, 4, -2)

    def test_complete_args(self):
        """Test case for initializing all attributes including ID."""
        r1_obj = Rectangle(2, 3, 4, 5, 8)
        self.assertEqual(r1_obj.id, 8)

    def test_area_method(self):
        """tests for the existence of this method() in the class"""
        r1_obj = Rectangle(2, 3)
        self.assertEqual(r1_obj.area(), 6)
        self.assertTrue(r1_obj.area, True)
        self.assertTrue(callable(r1_obj.area))

    def test_str_method(self):
        """test for the existence of __str__()"""
        r1_obj = Rectangle(2, 1)
        self.assertEqual(r1_obj.__str__(), '[Rectangle] (14) 0/0 - 2/1')
        self.assertTrue(callable(r1_obj.__str__))
        self.assertTrue(hasattr(r1_obj, '__str__'))

    def test_display(self):
        """tests the existence of this method() in the class instance"""
        r1_obj = Rectangle(2, 2)
        self.assertTrue(r1_obj.display, True)
        self.assertEqual(r1_obj.display(), None)
        self.assertTrue(callable(r1_obj.display))

    def test_display_stdout(self):
        """ tests for correct character display to stdout (without x & y)"""
        with self.subTest():
            r1_obj = Rectangle(2, 2)
            with patch('sys.stdout', new=StringIO()) as to_stdout:
                r1_obj.display()
                self.assertEqual(to_stdout.getvalue(), '##\n##\n')

        with self.subTest():
            """ tests for correct character display to stdout (without y)"""
            r1_obj = Rectangle(2, 2, 2)
            with patch('sys.stdout', new=StringIO()) as to_stdout:
                r1_obj.display()
                self.assertEqual(to_stdout.getvalue(), '  ##\n  ##\n')

    def test_to_dictionary(self):
        """tests for the existence of this class method()"""
        r1_obj = Rectangle(2, 2)
        self.assertTrue(hasattr(r1_obj, 'to_dictionary'))
        self.assertTrue(callable(r1_obj.to_dictionary))

    def test_update(self):
        """tests for the existence of update method()"""
        r1_obj = Rectangle(2, 2)
        self.assertTrue(hasattr(r1_obj, 'update'))
        self.assertTrue(callable(r1_obj.update))


    def test_update_args(self):
        """ tests for correct update of attr values based on the passed args"""
        with self.subTest():
            r1_obj = Rectangle(2, 2)
            r1_obj.update(90)
            self.assertEqual(r1_obj.id, 90)

        with self.subTest():
            """tests for correct assigning of width argument"""
            r1_obj.update(90, 99)
            self.assertEqual(r1_obj.width, 99)

        with self.subTest():
            """tests for correct assigning of height argument"""
            r1_obj.update(90, 33, 99)
            self.assertEqual(r1_obj.height, 99)

        with self.subTest():
            """tests for correct assigning of x argument"""
            r1_obj.update(90, 33, 99, 44)
            self.assertEqual(r1_obj.x, 44)

        with self.subTest():
            """tests for correct attr assinging (argument for y)"""
            r1_obj.update(90, 33, 99, 44, 55)
            self.assertEqual(r1_obj.y, 55)

    def update_kwargs(self):
        """tests update() method with key-word arguments (id obj attr)"""
        with self.subTest():
            r1_obj = Rectangle(2, 2)
            r1_obj.update(**{'id': 99})
            self.assertEqual(r1_obj.id, 99)

        with self.subTest():
            """tests update() method with key-word arguments (width obj attr)"""
            r1_obj = Rectangle(2, 2)
            r1_obj.update(**{'id': 99, 'width': 2})
            self.assertEqual(r1_obj.width, 2)

        with self.subTest():
            """tests update() method with key-word arguments (height obj attr)"""
            r1_obj = Rectangle(2, 2)
            r1_obj.update(**{'id': 99, 'width': 2, 'height': 6})
            self.assertEqual(r1_obj.height, 6)

        with self.subTest():
            """tests update() method with key-word arguments (x obj attr)"""
            r1_obj = Rectangle(2, 2)
            r1_obj.update(**{'id': 99, 'width': 2, 'height': 6, 'x': 22})
            self.assertEqual(r1_obj.x, 22)

        with self.subTest():
            """tests update() method with key-word arguments (y obj attr)"""
            r1_obj = Rectangle(2, 2)
            r1_obj.update(**{'id': 99, 'width': 2, 'height': 6, 'x': 22, 'y': 4})
            self.assertEqual(r1_obj.y, 4)
