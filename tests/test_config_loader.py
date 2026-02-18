import unittest
from config_loader import load_config

class TestConfigLoader(unittest.TestCase):
    def test_load_config(self):
        cfg = load_config("config.yml")
        self.assertIn("input", cfg)
        self.assertIn("output", cfg)
        self.assertIn("table", cfg)

if __name__ == "__main__":
    unittest.main()