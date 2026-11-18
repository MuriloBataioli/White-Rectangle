import flet as ft
from Core.Context import state

class _Window():
    def __init__(self, name, height=600, width=400, mode="normal"):
        self.name = name
        self.height = height
        self.width = width
        self.mode = mode

        self.controles = []
        self.elements = {}  # Dicionário local desta janela: {"nome_widget": objeto}

        if self not in state.windows:
            state.windows.append(self)

    def __enter__(self):
        state.pilha.append(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        state.pilha.pop()
        # Removido o ft.run automático daqui! A janela agora é puramente declarativa.

    def _render(self, page: ft.Page):
        self._page = page
        
        page.title = self.name
        page.window.width = self.width
        page.window.height = self.height

        # Configurações de modo (fullscreen, bordeless, windowless, etc.)
        if self.mode == "fullscreen":
            page.window.full_screen = True
        elif self.mode == "bordeless":
            page.window.frameless = True
        elif self.mode == "windowless":
            page.window.visible = False

        # Embrulha os controles no SafeArea automaticamente
        page.add(ft.SafeArea(content=ft.Column(controls=self.controles)))