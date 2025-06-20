import os
import xml.etree.ElementTree as ET
import pandas as pd

# Caminho da pasta com os arquivos XML
pasta = r"C:/Users/osgabriel/Documents/Xmls" \
"" \
"" \
"" \
""

dados = []

for arquivo in os.listdir(pasta):
    if arquivo.endswith(".xml"):
        caminho_arquivo = os.path.join(pasta, arquivo)
        print(f"Lendo: {caminho_arquivo}")
        
        try:
            tree = ET.parse(caminho_arquivo)
            root = tree.getroot()

            # Procura a chave de acesso (tag chNFe)
            chNFe = root.find(".//{*}chNFe")
            chave = chNFe.text if chNFe is not None else "Chave não encontrada"

            # Procura o nome da transportadora (tag xNome dentro de transporta)
            xNome = root.find(".//{*}transporta/{*}xNome")
            transportadora = xNome.text if xNome is not None else "Transportadora não encontrada"

            print(f"Chave: {chave}")
            print(f"Transportadora: {transportadora}")
            print("-" * 40)

            # Adiciona no dados
            dados.append({
                "Chave de Acesso": chave,
                "Transportadora": transportadora
            })

        except ET.ParseError as e:
            print(f"Erro ao ler {arquivo}: {e}")

# Depois de ler todos os XMLs, cria DataFrame e salva em Excel
df = pd.DataFrame(dados)
saida = os.path.join(pasta, "transportadoras.xlsx")
df.to_excel(saida, index=False)

print(f"Arquivo Excel salvo em: {saida}")