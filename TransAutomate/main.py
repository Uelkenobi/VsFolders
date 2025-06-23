import pyautogui
import pyperclip
import time
from tqdm import tqdm
import datetime
import subprocess
import shutil
import os


# TransAutomate - Automação de Download de DANFE e XML

# Lista dos dados que você quer colar na barra de pesquisa
dados = [
    "35250360837457000187550010003361651178026607",
]

# Coordenadas da tela
barra_pesquisa_x = 509
barra_pesquisa_y = 519
botao_danfe_x = 941
botao_danfe_y = 512
botao_xml_x = 728
botao_xml_y = 287

print("Você tem 5 segundos para organizar a tela...")
time.sleep(10)

# Estimar tempo por item (ajuste se quiser mais preciso)
tempo_por_item = 7  # segundos aproximados por ciclo (2+1+1+2 + margem)

# Barra de progresso
inicio = datetime.datetime.now()

for chave in tqdm(dados, desc="Processando chaves", unit="chave", total=len(dados)):
    t0 = time.time()

    # Clicar na barra de pesquisa
    pyautogui.click(barra_pesquisa_x, barra_pesquisa_y)
    time.sleep(0.3)

    # Colar a chave
    pyperclip.copy(chave)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(3)  # espera o site carregar

    # Baixar DANFE
    pyautogui.click(botao_danfe_x, botao_danfe_y)
    time.sleep(3)

    # Baixar XML
    pyautogui.click(botao_xml_x, botao_xml_y)
    time.sleep(3)

    # Atualiza a página
    pyautogui.press('f5')
    time.sleep(2)

    # Atualiza estimativa (tqdm faz isso automaticamente)

fim = datetime.datetime.now()
duracao = fim - inicio
print(f"Finalizado em {duracao}.")

fim = datetime.datetime.now()
duracao = fim - inicio
print(f"Finalizado em {duracao}.")

# Caminhos
pasta_download = os.path.join(os.path.expanduser("~"), "Downloads")
pasta_destino = r"C:/Users/osgabriel/Documents/Xmls"

# Cria a pasta de destino se não existir
os.makedirs(pasta_destino, exist_ok=True)

# Move os arquivos .xml da pasta Downloads
arquivos_movidos = 0
for arquivo in os.listdir(pasta_download):
    if arquivo.lower().endswith(".xml"):
        origem = os.path.join(pasta_download, arquivo)
        destino = os.path.join(pasta_destino, arquivo)
        try:
            shutil.move(origem, destino)
            print(f"Movido: {arquivo}")
            arquivos_movidos += 1
        except Exception as e:
            print(f"Erro ao mover {arquivo}: {e}")

if arquivos_movidos == 0:
    print("Nenhum arquivo XML encontrado na pasta de Downloads.")
else:
    print(f"{arquivos_movidos} arquivo(s) XML movido(s) para: {pasta_destino}")


# Chama o script Pt.py após terminar o download
print("Iniciando leitura dos arquivos XML...")
subprocess.run(["python", "C:/Users/osgabriel/Desktop/VsFolders/TransAutomate/Pt.py"])