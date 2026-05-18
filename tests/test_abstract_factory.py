import unittest
from src.creational_patterns.abstract_factory import (
    WindowsFactory, MacOSFactory, create_ui
)


class TestAbstractFactory(unittest.TestCase):
    
    def test_windows_factory(self):
        factory = WindowsFactory()
        ui = create_ui(factory)
        
        self.assertIn("Windows", ui["button_render"])
        self.assertIn("Windows", ui["button_click"])
        self.assertIn("Windows", ui["checkbox_render"])
        self.assertIn("Windows", ui["checkbox_check"])
    
    def test_macos_factory(self):
        factory = MacOSFactory()
        ui = create_ui(factory)
        
        self.assertIn("MacOS", ui["button_render"])
        self.assertIn("MacOS", ui["button_click"])
        self.assertIn("MacOS", ui["checkbox_render"])
        self.assertIn("MacOS", ui["checkbox_check"])
    
    def test_ui_components_are_different(self):
        windows_ui = create_ui(WindowsFactory())
        macos_ui = create_ui(MacOSFactory())
        
        self.assertNotEqual(windows_ui["button_render"], macos_ui["button_render"])
        self.assertNotEqual(windows_ui["checkbox_render"], macos_ui["checkbox_render"])


if __name__ == '__main__':
    unittest.main()