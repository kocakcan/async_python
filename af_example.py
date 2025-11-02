from abc import ABC, abstractmethod


# Abstract Products
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


# Concrete Products for Light Theme
class LightButton(Button):
    def paint(self):
        return "Rendering a light button"


class LightCheckbox(Checkbox):
    def paint(self):
        return "Rendering a light checkbox"


# Concrete Products for Dark Theme
class DarkButton(Button):
    def paint(self):
        return "Rendering a dark button"


class DarkCheckbox(Checkbox):
    def paint(self):
        return "Rendering a dark checkbox"


# Abstract Factory
class ThemeFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class LightThemeFactory(ThemeFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()


class DarkThemeFactory(ThemeFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()


# Client code
def create_ui(factory: ThemeFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.paint())
    print(checkbox.paint())


if __name__ == "__main__":
    print("Creating UI with Light Theme:")
    create_ui(LightThemeFactory())

    print("\nCreating UI with Dark Theme:")
    create_ui(DarkThemeFactory())
