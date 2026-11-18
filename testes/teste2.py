import flet as ft
from Core.Comands.Set import set
from Core.Comands.Mod import mod
from Core.Comands.Get import get
from Core.Comands.Open import open
from Core.Comands.Close import close
from Core.Comands.Start import start
from Core.Comands.Stop import stop

# Ação do botão na Home que abre a janela do Formulário
def abrir_formulario():
    open("Formulario")

# Ação de salvar dentro do formulário (simula processamento e fecha sozinho)
def salvar_e_sair():
    print("[Engine] Processando dados do formulário...")
    # Aqui você poderia ler os campos, ex: get("Formulario", "CampoNome")
    print("[Engine] Dados salvos com sucesso! Fechando janela atual...")
    
    # Fecha esta view de forma programática e retorna para a Home
    close("Formulario")

# --- JANELA PRINCIPAL (HOME) ---
with set.window(name="Home"):
    set.label(name="TituloHome", content="Painel Principal - White Rectangle")
    set.button(name="BtnAbrir", content="Abrir Formulário de Cadastro", on_click=abrir_formulario)

# --- JANELA SECUNDÁRIA (FORMULÁRIO) ---
with set.window(name="Formulario"):
    set.label(name="TituloForm", content="Cadastro de Registro")
    
    # Simula um campo ou botão de ação de salvamento
    set.button(
        name="BtnSalvar", 
        content="Salvar e Sair Automaticamente", 
        on_click=salvar_e_sair
    )
    

# Inicia a aplicação na janela raiz
start("Home", height=800, width=800)