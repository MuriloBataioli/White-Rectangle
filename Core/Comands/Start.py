# Core/Comands/Start.py
import flet as ft
from Core.Context import state

class _Start:
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

        print(f"[Engine] [Face] Iniciando janela: {target_window.name}")
        ft.run(target_window._render)

start = _Start()