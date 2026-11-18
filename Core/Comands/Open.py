# Core/Comands/Open.py
import flet as ft
from Core.Context import state

class _Open:
    def __call__(self, window_name: str, mode: str = None, **kwargs):
        target_window = None
        for win in state.windows:
            if win.name == window_name:
                target_window = win
                break
        
        if not target_window:
            raise KeyError(f"Janela '{window_name}' não foi encontrada ou declarada.")

        if mode:
            target_window.mode = mode
        if "height" in kwargs:
            target_window.height = kwargs["height"]
        if "width" in kwargs:
            target_window.width = kwargs["width"]

        print(f"[Engine] [Vértice] Abrindo conexão nativa com a janela: {target_window.name}")
        
        current_page = None
        if state.pilha:
            current_page = getattr(state.pilha[-1], '_page', None)
        
        if not current_page:
            for win in state.windows:
                if hasattr(win, '_page') and win._page:
                    current_page = win._page
                    break

        if current_page:
            route_name = f"/{target_window.name.lower()}"
            
            # Remove se já existir na pilha para evitar duplicatas
            for v in current_page.views[:]:
                if v.route == route_name:
                    current_page.views.remove(v)

            new_view = ft.View(
                route=route_name,
                controls=[
                    ft.AppBar(title=ft.Text(target_window.name)),
                    ft.SafeArea(content=ft.Column(controls=target_window.controles))
                ]
            )
            
            # Intercepta o evento de fechar a view nativamente pela página
            def view_pop(e):
                if current_page.views:
                    current_page.views.pop()
                current_page.update()

            current_page.on_view_pop = view_pop

            current_page.views.append(new_view)
            current_page.update()
        else:
            print(f"[Engine] [Vértice] Erro: Nenhuma página ativa encontrada para abrir o vértice {window_name}.")

open = _Open()