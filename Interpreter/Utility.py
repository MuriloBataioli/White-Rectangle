import flet as ft

from Core.Context import state

class _Window():

    def __init__(self, name, height, width):
        self.name = name
        self.height = height
        self.width = width

        self.controles = []
        self.elements = {}  # Dicionário local desta janela: {"nome_widget": objeto}

        if self not in state.windows:
            state.windows.append(self)
    def __enter__(self):
        state.pilha.append(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        state.pilha.pop()
        # Só renderiza se NÃO estiver carregando via integrations
        if not exc_type and not getattr(state, 'loading_integration', False):
            ft.run(self._render)

    def _render(self, page: ft.Page):
        page.title = self.name
        page.window.width = self.width
        page.window.height = self.height
        # Embrulha os controles no SafeArea automaticamente
        page.add(ft.SafeArea(content=ft.Column(controls=self.controles)))