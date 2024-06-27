import unittest
from src.main import model

class TestModel(unittest.TestCase):
    def test_model_structure(self):
        self.assertEqual(len(model.layers), 4)
        self.assertEqual(model.layers[0].output_shape, (None, 60, 50))

if __name__ == '__main__':
    unittest.main()
