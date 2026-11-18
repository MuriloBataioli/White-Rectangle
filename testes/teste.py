from Core.Comands.Set import set
from Core.Comands.Mod import mod
from Core.Comands.Name import name
from Core.Comands.Get import get
from Core.Comands.Integrations import integrations





def teste():

    name("homem", "Amém").mod(content="alo")

def teste2():
    conteudo = name("homem", "Amém").get("content")
    print(conteudo)

with set.window(name="homem"):
    set.label(name="Meu Pau", content="HELLO WORLD")
    set.button(name="Amém", content="teste", on_click=teste, on_long_press=teste2)

    texto = integrations("teste_Integrations").name("Mapa", "mapeamento").get("content")

    set.label(name="olha la", content=texto)


