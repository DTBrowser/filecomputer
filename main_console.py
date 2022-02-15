import os
import sys
from pathlib import Path
def get_extension(caminho):
    ultimo = len(str(caminho)) - 4
    final_ultimo = len(str(caminho))
    return str(caminho)[ultimo:final_ultimo]
def ordenar_arquivos(caminho):
    numero = 1
    ordem = sorted(Path(caminho).iterdir(), key=os.path.getmtime)
    arquivo = str(ordem[0])
    for arquivo in ordem:
        os.rename(arquivo, caminho + "\\" + str(numero) + get_extension(arquivo))
        numero += 1
arguments = sys.argv
try:
    ordenar_arquivos(arguments[1])
    print("Finished ;)")
except Exception as erro:
    print("How to use:")
    print("./console.py <directory>")







