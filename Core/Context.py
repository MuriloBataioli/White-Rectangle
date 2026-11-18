# Core/Context.py
class _EngineState:

    def __init__(self):
        self.pilha = []
        self.windows = []          # Lista de instâncias de _Window ativas
        self.modules = {}          # Módulos/arquivos registrados via integrations
        self.active_module = None  # Contexto de arquivo atual

state = _EngineState()