# Core/Comands/Name.py
from Core.Context import state

class _NameResolver:
    def __init__(self, *args):
        self.selectors = args

    def resolve(self):
        if not self.selectors:
            raise ValueError("Nenhum identificador fornecido no name()")

        # Se passou 1 argumento (ex: name("homem") ou name("Amém"))
        if len(self.selectors) == 1:
            target_name = self.selectors[0]
            for window in state.windows:
                if window.name == target_name:
                    return window
                if target_name in window.elements:
                    return window.elements[target_name]
            raise KeyError(f"Elemento ou Janela '{target_name}' não encontrado.")

        # Se passou múltiplos argumentos (ex: name("homem", "Amém"))
        window_name, element_name = self.selectors[0], self.selectors[1]
        for window in state.windows:
            if window.name == window_name:
                if element_name in window.elements:
                    return window.elements[element_name]
                raise KeyError(f"Elemento '{element_name}' não encontrado na janela '{window_name}'.")

        raise KeyError(f"Janela '{window_name}' não encontrada.")

    def mod(self, **properties):
        """Modifica as propriedades do elemento resolvido pelo name"""
        target = self.resolve()
        
        # Mapeia 'content' para 'value' se o componente usar value
        if "content" in properties and hasattr(target, "value") and not hasattr(target, "content"):
            properties["value"] = properties.pop("content")

        for prop, value in properties.items():
            setattr(target, prop, value)
        if hasattr(target, "update"):
            target.update()

    def get(self, prop):
        """Resgata a propriedade do elemento resolvido pelo name"""
        target = self.resolve()
        
        # Se pedirem 'content' mas o Flet usa 'value', traduzimos na hora
        if prop == "content" and not hasattr(target, "content") and hasattr(target, "value"):
            prop = "value"

        if hasattr(target, prop):
            return getattr(target, prop)
        raise AttributeError(f"O alvo não possui a propriedade '{prop}'.")

def name(*args):
    return _NameResolver(*args)