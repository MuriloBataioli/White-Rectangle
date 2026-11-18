# Core/Comands/Integrations.py
import importlib.util
import sys
from pathlib import Path
from Core.Context import state
from Core.Comands.Name import _NameResolver

class _Integrations:
    def __call__(self, module_name: str):
        if not module_name:
            raise ValueError("Você precisa informar o módulo no integrations()")
        
        if module_name not in state.modules:
            caminho_arquivo = None
            for path in Path(".").rglob(f"{module_name}.py"):
                caminho_arquivo = path
                break
            
            if not caminho_arquivo or not caminho_arquivo.exists():
                raise ImportError(f"Arquivo '{module_name}.py' não encontrado.")

            try:
                # Seta a flag dizendo que estamos carregando uma integração (não renderiza visualmente)
                state.loading_integration = True
                
                spec = importlib.util.spec_from_file_location(module_name, str(caminho_arquivo))
                mod = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = mod
                spec.loader.exec_module(mod)
                
                state.modules[module_name] = mod
            except Exception as e:
                raise ImportError(f"Erro ao carregar módulo '{module_name}': {e}")
            finally:
                # Reseta a flag
                state.loading_integration = False

        return _IntegrationSelector(module_name)

class _IntegrationSelector:
    def __init__(self, module_name):
        self.module_name = module_name

    def name(self, *args):
        return _NameResolver(*args)

integrations = _Integrations()