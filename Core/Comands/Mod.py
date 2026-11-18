# Core/Comands/Mod.py
from Core.Comands.Name import name

class _Mod:
    def __call__(self, target_name, **properties):
        # Permite uso direto ou integrado
        target = name(target_name).resolve()
        for prop, value in properties.items():
            setattr(target, prop, value)
        if hasattr(target, "update"):
            target.update()

mod = _Mod()