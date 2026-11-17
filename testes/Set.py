from teste_intrepetador import _Window, _Label

class _Set():

    def window(self, name="White Rectangle", height=600, width=400):
        return _Window(name, height, width)

    def label(self, name: str, content: str, size: int=16):
        return _Label(name, content, size)



set = _Set()