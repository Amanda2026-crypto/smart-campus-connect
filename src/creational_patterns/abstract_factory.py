"""
Abstract Factory Pattern
Use Case: Creating related UI components for different platforms
"""

from abc import ABC, abstractmethod


class Button(ABC):
    """Abstract product for Button"""
    
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def click(self) -> str:
        pass


class Checkbox(ABC):
    """Abstract product for Checkbox"""
    
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def check(self) -> str:
        pass


class WindowsButton(Button):
    """Concrete button for Windows"""
    
    def render(self) -> str:
        return "Rendering Windows button"
    
    def click(self) -> str:
        return "Windows button clicked"


class WindowsCheckbox(Checkbox):
    """Concrete checkbox for Windows"""
    
    def render(self) -> str:
        return "Rendering Windows checkbox"
    
    def check(self) -> str:
        return "Windows checkbox checked"


class MacOSButton(Button):
    """Concrete button for MacOS"""
    
    def render(self) -> str:
        return "Rendering MacOS button"
    
    def click(self) -> str:
        return "MacOS button clicked"


class MacOSCheckbox(Checkbox):
    """Concrete checkbox for MacOS"""
    
    def render(self) -> str:
        return "Rendering MacOS checkbox"
    
    def check(self) -> str:
        return "MacOS checkbox checked"


class GUIFactory(ABC):
    """Abstract factory"""
    
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    """Concrete factory for Windows"""
    
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    """Concrete factory for MacOS"""
    
    def create_button(self) -> Button:
        return MacOSButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


def create_ui(factory: GUIFactory):
    """Client code"""
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    return {
        "button_render": button.render(),
        "button_click": button.click(),
        "checkbox_render": checkbox.render(),
        "checkbox_check": checkbox.check()
    }