import unittest

from drivers.gfx import Gfx


class TestGfx(unittest.TestCase):
    def test_screen_dimensions(self):
        screen = Gfx().get_screen_size()
        self.assertEqual(screen["width"], 640)
        self.assertEqual(screen["height"], 320)


if __name__ == "__main__":
    unittest.main()
