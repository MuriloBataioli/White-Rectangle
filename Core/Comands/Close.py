# Core/Comands/Close.py
from Core.Context import state

class _Close:
    def __call__(self, window_name: str = None, all: bool = False):
        current_page = None
        if state.pilha:
            current_page = getattr(state.pilha[-1], '_page', None)
        
        if not current_page:
            for win in state.windows:
                if hasattr(win, '_page') and win._page:
                    current_page = win._page
                    break

        if not current_page:
            print(f"[Engine] [Vértice] Erro: Nenhuma página ativa encontrada para fechar.")
            return

        if len(current_page.views) > 1:
            if all:
                # Mantém apenas a primeira view (a Raiz/Home) e descarta todas as secundárias
                current_page.views = [current_page.views[0]]
                current_page.update()
                print(f"[Engine] [Vértice] Pilha limpa. Retornado direto à raiz.")
            elif window_name:
                route_name = f"/{window_name.lower()}"
                found = False
                for v in current_page.views[:]:
                    if v.route == route_name:
                        current_page.views.remove(v)
                        found = True
                
                if found:
                    current_page.update()
                    print(f"[Engine] [Vértice] Vértice '{window_name}' fechado com sucesso.")
                else:
                    print(f"[Engine] [Vértice] Aviso: A janela '{window_name}' não estava ativa na pilha.")
            else:
                # Comportamento padrão: desempilha apenas o topo
                current_page.views.pop()
                current_page.update()
                print(f"[Engine] [Vértice] Desconectando e retornando ao vértice anterior.")
        else:
            print(f"[Engine] [Vértice] Não há views suficientes para fechar (raiz atingida).")

close = _Close()