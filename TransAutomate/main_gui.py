import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext, messagebox
import pyautogui
import pyperclip
import time
import datetime
import subprocess
import shutil
import os

def iniciar_processo():
    chaves = entrada_chaves.get("1.0", "end").strip().splitlines()
    chaves_validas = [c.strip() for c in chaves if len(c.strip()) == 44 and c.strip().isdigit()]

    if not chaves_validas:
        messagebox.showerror("Erro", "Nenhuma chave válida foi inserida.")
        return

    messagebox.showinfo("Organize o navegador", "Você tem 5 segundos para organizar a tela do navegador.")
    app.update()
    time.sleep(5)

    barra_pesquisa_x = 509
    barra_pesquisa_y = 519
    botao_danfe_x = 941
    botao_danfe_y = 512
    botao_xml_x = 728
    botao_xml_y = 287

    inicio = datetime.datetime.now()

    for chave in chaves_validas:
        log(f"🔑 Processando: {chave}")
        pyautogui.click(barra_pesquisa_x, barra_pesquisa_y)
        time.sleep(0.3)
        pyperclip.copy(chave)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.click(botao_danfe_x, botao_danfe_y)
        time.sleep(3)
        pyautogui.click(botao_xml_x, botao_xml_y)
        time.sleep(3)
        pyautogui.press('f5')
        time.sleep(2)

    duracao = datetime.datetime.now() - inicio
    log(f"✅ Download concluído em {duracao}.")

    mover_xmls()
    gerar_planilha()

def mover_xmls():
    pasta_download = os.path.join(os.path.expanduser("~"), "Downloads")
    pasta_destino = r"C:/Users/osgabriel/Documents/Xmls"
    os.makedirs(pasta_destino, exist_ok=True)

    movidos = 0
    for arquivo in os.listdir(pasta_download):
        if arquivo.lower().endswith(".xml"):
            origem = os.path.join(pasta_download, arquivo)
            destino = os.path.join(pasta_destino, arquivo)
            try:
                shutil.move(origem, destino)
                log(f"📁 Movido: {arquivo}")
                movidos += 1
            except Exception as e:
                log(f"❌ Erro ao mover {arquivo}: {e}")

    if movidos == 0:
        log("⚠️ Nenhum XML encontrado.")
    else:
        log(f"📦 {movidos} arquivo(s) XML movido(s).")

def gerar_planilha():
    log("📄 Gerando planilha de transportadoras...")
    subprocess.run(["python", "C:/Users/osgabriel/Desktop/VsFolders/TransAutomate/Pt.py"])
    log("✅ Planilha criada com sucesso!")

def log(msg):
    texto_log.insert("end", msg + "\n")
    texto_log.see("end")
    app.update()

app = ttk.Window(themename="darkly")
app.title("TransAutomate - NF-e")
app.geometry("700x600")

ttk.Label(app, text="Cole as chaves das notas fiscais (uma por linha):", font=("Segoe UI", 11)).pack(pady=10)
entrada_chaves = scrolledtext.ScrolledText(app, height=8, font=("Consolas", 10))
entrada_chaves.pack(fill="both", padx=20)

ttk.Button(app, text="Iniciar Processo", command=iniciar_processo, bootstyle="success").pack(pady=15)
ttk.Label(app, text="Log do processo:", font=("Segoe UI", 10)).pack()
texto_log = scrolledtext.ScrolledText(app, height=12, font=("Consolas", 9))
texto_log.pack(fill="both", padx=20, pady=10)

app.mainloop()
