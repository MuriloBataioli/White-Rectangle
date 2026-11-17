import flet as ft

class _Contexto():
    pilha = []

class _Window():

    def __init__(self, name, height, width):
        self.name = name
        self.height = height
        self.width = width
        self.controles = []

    def __enter__(self):
        # Coloca a janela no topo da pilha como contêiner ativo
        _Contexto.pilha.append(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Remove da pilha ao sair da indentação e inicia o Flet
        _Contexto.pilha.pop()
        if not exc_type:
            ft.run(self._render)

    def _render(self, page: ft.Page):
        page.title = self.name
        page.window.width = self.width
        page.window.height = self.height
        # Embrulha os controles no SafeArea automaticamente
        page.add(ft.SafeArea(content=ft.Column(controls=self.controles)))

class _Label():

    def __init__(self, name: str, content: str, size: int=16):
        
        widget = ft.Text(value=content, size=size)
        # Se houver um bloco 'with' aberto, injeta o widget nele automaticamente
        if _Contexto.pilha:
            _Contexto.pilha[-1].controles.append(widget)
