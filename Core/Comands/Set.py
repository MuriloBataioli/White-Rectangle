from Interpreter.Utility import _Window
from Interpreter.Display import _Text
from Interpreter.Buttons import _Button


class _Set():

    def window(self, name="White Rectangle", height=600, width=400):
        return _Window(name, height, width)

    def label(self, name: str, content: str, size: int=16):
        return _Text(name, content, size)

    def button(self, name, content, on_click, **Kwargs):
        return _Button(name, content, on_click, **Kwargs)



set = _Set()