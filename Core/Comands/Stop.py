# Core/Comands/Stop.py
from Core.Context import state

class _Stop:
    def __call__(self, window_name: str):
        target_window = None
        for win in state.windows:
            if win.name == window_name:
                target_window = win
                break
        
        if not target_window:
            raise KeyError(f"Janela '{window_name}' não foi encontrada para ser encerrada.")

        if hasattr(target_window, '_page') and target_window._page:
            page = target_window._page
            # O run_task agenda e executa a corrotina de fechamento de forma segura na thread do Flet
            page.run_task(page.window.close)
            print(f"[Engine] [Face] Janela '{window_name}' encerrada.")
        else:
            print(f"[Engine] [Face] A janela '{window_name}' não está ativa.")

stop = _Stop()