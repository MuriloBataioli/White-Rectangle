import flet as ft

from Core.Context import state

class _Text():

    def __init__(self, name: str, content: str, size: int=16, **Kwargs):
        self.name = name

        self.widget = ft.Text(value=content, size=size, **Kwargs)

        # Se houver um bloco 'with' aberto, injeta o widget nele automaticamente
        if state.pilha:

            windown = state.pilha[-1]

            if self.name:
                windown.elements[self.name] = self.widget

            windown.controles.append(self.widget)