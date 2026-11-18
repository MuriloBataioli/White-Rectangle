import flet as ft

from Core.Context import state

class _Button():

    def __init__(self, name: str, content: str, on_click=None, **Kwargs):

        self.name = name

        self.widget = ft.Button(content=content, on_click=on_click, **Kwargs)

        if state.pilha:

            windown = state.pilha[-1]

            if self.name:
                windown.elements[self.name] = self.widget

            windown.controles.append(self.widget)