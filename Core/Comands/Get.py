# Core/Comands/Get.py
from Core.Comands.Name import name

class _Get:
    def __init__(self, resolved_target):
        self.target = resolved_target

    def get(self, prop):
        if hasattr(self.target, prop):
            return getattr(self.target, prop)
        return self.target.get(prop) if hasattr(self.target, "get") else None

def get(target_name, prop):
    target = name(target_name).resolve()
    if hasattr(target, prop):
        return getattr(target, prop)
    raise AttributeError(f"O alvo não possui a propriedade '{prop}'.")