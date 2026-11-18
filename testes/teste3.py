import flet as ft
from Core.Comands.Set import set
from Core.Comands.Open import open
from Core.Comands.Close import close
from Core.Comands.Start import start

# Funções de navegação em cascata
def abrir_etapa_1():
    open("Etapa1")

def abrir_etapa_2():
    open("Etapa2")

def salvar_e_voltar_tudo():
    print("[Engine] Salvando fluxo completo em cascata...")
    # Fecha tudo de uma vez só e retorna limpo para a Home raiz (all=True)
    close(all=True)

# --- JANELA RAIZ (HOME) ---
with set.window(name="Home"):
    set.label(name="TitHome", content="Painel Raiz - Início do Fluxo")
    set.button(name="Btn1", content="Abrir Etapa 1", on_click=abrir_etapa_1)

# --- ETAPA 1 ---
with set.window(name="Etapa1"):
    set.label(name="TitEtapa1", content="Estamos na Etapa 1")
    set.button(name="Btn2", content="Avançar para Etapa 2", on_click=abrir_etapa_2)

# --- ETAPA 2 (FIM DO FLUXO) ---
with set.window(name="Etapa2"):
    set.label(name="TitEtapa2", content="Etapa Final - Conclusão")
    set.button(
        name="BtnSalvarTudo", 
        content="Salvar Tudo e Retornar ao Início", 
        on_click=salvar_e_voltar_tudo
    )

# Inicia a aplicação na raiz
start("Home", height=800, width=800)