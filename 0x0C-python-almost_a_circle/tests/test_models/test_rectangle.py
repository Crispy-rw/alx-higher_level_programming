"""
Contains the definition of the test class for the Rectangle class.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """Unittest test class for Rectangle class"""

    def setUp(self):
        """Set up resources required to run the tests"""
        self.rectangle_1 = Rectangle(2, 3)
        self.rectangle_2 = Rectangle(1, 3, 2, 1, 3)

    def tearDown(self):
        """Tear down resources that had been set up to run tests"""
        del self.rectangle_1
        del self.rectangle_2

    def test_width_height_assignment(self):
        """Test assignment of width and height attributes"""
        self.assertEqual(self.rectangle_1.width, 2)
        self.assertEqual(self.rectangle_1.height, 3)

    def test_x_y_assignment(self):
        """Test assignment of x and y attributes"""
        self.assertEqual(self.rectangle_1.x, 0)
        self.assertEqual(self.rectangle_1.y, 0)
        self.assertEqual(self.rectangle_2.x, 2)
        self.assertEqual(self.rectangle_2.y, 1)

    def test_exceptions_type_str(self):
        """Test whether TypeError is raised for str arguments"""
        args = ['h', 2, 3, 4]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 'h', 2, 3]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 2, 'h', 3]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 2, 3, 'h']
        self.assertRaises(TypeError, Rectangle, *args)

    def test_exceptions_type_float(self):
        """Test whether TypeError is raised for float arguments"""
        args = [4.2, 2, 3, 4]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 4.2, 2, 3]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 2, 4.2, 3]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 2, 3, 4.2]
        self.assertRaises(TypeError, Rectangle, *args)

    def test_exceptions_type_list(self):
        """Test whether TypeError is raised for list arguments"""
        args = [[1, 2], 2, 3, 4]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, [1, 2], 2, 3]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 2, [1, 3], 3]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 2, 3, [1, 2]]
        self.assertRaises(TypeError, Rectangle, *args)

    def test_exceptions_type_set(self):
        """Test whether TypeError is raised for set arguments"""
        args = [{1, 2}, 2, 3, 4]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, {1, 2}, 2, 3]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 2, {1, 3}, 3]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 2, 3, {1, 2}]
        self.assertRaises(TypeError, Rectangle, *args)

    def test_exceptions_type_tuple(self):
        """Test whether TypeError is raised for tuple arguments"""
        args = [(1, 2), 2, 3, 4]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, (1, 2), 2, 3]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 2, (1, 3), 3]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 2, 3, (1, 2)]
        self.assertRaises(TypeError, Rectangle, *args)

    def test_exceptions_type_dict(self):
        """Test whether TypeError is raised for str arguments"""
        args = [{"one": 2}, 2, 3, 4]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, {"two": 2}, 2, 3]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 2, {"three": 3}, 3]
        self.assertRaises(TypeError, Rectangle, *args)
        args = [4, 2, 3, {"two": 2}]
        self.assertRaises(TypeError, Rectangle, *args)

    def test_type_exception_message(self):
        """Tests whether the correct exception message is printed"""
        args = ['One', 5, 1, 3]
        self.assertRaisesRegex(TypeError, "width", Rectangle, *args)
        args = [4, 'Two', 4, 7]
        self.assertRaisesRegex(TypeError, "height", Rectangle, *args)
        args = [4, 5, 'Three', 7]
        self.assertRaisesRegex(TypeError, "x", Rectangle, *args)
        args = [4, 1, 4, "Four"]
        self.assertRaisesRegex(TypeError, "y", Rectangle, *args)

    def test_value_exception_message(self):
        """Tests whether the correct exception message is printed"""
        args = [-5, 5, 1, 3]
        self.assertRaisesRegex(ValueError, "width", Rectangle, *args)
        args = [0, 5, 1, 3]
        self.assertRaisesRegex(ValueError, "width", Rectangle, *args)
        args = [4, -4, 4, 7]
        self.assertRaisesRegex(ValueError, "height", Rectangle, *args)
        args = [4, 0, 4, 7]
        self.assertRaisesRegex(ValueError, "height", Rectangle, *args)
        args = [4, 5, -1, 7]
        self.assertRaisesRegex(ValueError, "x", Rectangle, *args)
        args = [4, 1, 4, -2]
        self.assertRaisesRegex(ValueError, "y", Rectangle, *args)

    def test_exceptions_value(self):
        """Test whether ValueError is raised for unacceptable arguments"""
        args = [0, 1, 2, 3]
        self.assertRaises(ValueError, Rectangle, *args)
        args = [1, 0, 3, 4]
        self.assertRaises(ValueError, Rectangle, *args)
        args = [4, 2, -5, 3]
        self.assertRaises(ValueError, Rectangle, *args)
        args = [4, 2, 3, -3]
        self.assertRaises(ValueError, Rectangle, *args)

    def test_area(self):
        """Test the area method of the Rectangle class"""
        self.assertEqual(self.rectangle_1.area(), 6)

    def test_str(self):
        """Test the __str__ magic method of the Rectangle class"""
        self.assertEqual(str(self.rectangle_2), "[Rectangle] (3) 2/1 - 1/3")

    def test_update(self):
        """Test the update method of the Rectangle class"""
        self.rectangle_1.update(1, 1, 1, 1, 1)
        self.assertEqual(str(self.rectangle_1), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_kwargs(self):
        """Test the update method of the Rectangle class using *kwargs"""
        self.rectangle_1.update(height=1, width=2, id=5)
        self.assertEqual(str(self.rectangle_1), "[Rectangle] (5) 0/0 - 2/1")
        kwargs = {"width": 5, "height": 4, "x": 3, "y": 2, "id": 1}
        self.rectangle_1.update(**kwargs)
        self.assertEqual(str(self.rectangle_1), "[Rectangle] (1) 3/2 - 5/4")

    def test_update_args_kwargs(self):
        """Test the update method of the Rectangle class with args and kwargs"""
        args = [1, 1, 1, 1, 1]
        kwargs = {"width": 5, "height": 4, "x": 3, "y": 2, "id": 1}
        self.rectangle_1.update(*args, **kwargs)
        self.assertEqual(str(self.rectangle_1), "[Rectangle] (1) 1/1 - 1/1")
