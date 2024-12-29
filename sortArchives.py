'''
Sort Archives Project- By Paulo Fiuza- 12/28/2024
Projeto Organizador de Arquivos
'''

import os
from tkinter.filedialog import askdirectory as askd

'''Create a Path
Criar um caminho'''

path = askd(title="Select A Folder")
print(f"Path= {path}")

'''Create an archives list
Criar uma lista de arquivos'''

archivesList = os.listdir(path)
print(f"Archives List= {archivesList}")

'''Create a dictionary of paths
Criar um dicionário de caminhos'''

dictPaths = {
    "images" : [".png", ".jpg", ".jpeg", ".bmp"],
    "sheets" : [".xls", ".xlsx"],
    "pdfs" : [".pdf"],
    "csvs" : [".csv"],
    "txts" : [".txt"],
    "videos" : [".mp4", ".webm"],
    "MSWordDocs" : [".doc", ".docx"],
    "Presentations" : [".ppt", ".pptx"],
    "webPages" : [".html"]  
}

for archives in archivesList:
    name, extension = os.path.splitext(f"{path}/{archives}")

    for folder in dictPaths:
        if extension in dictPaths[folder]:
            if not os.path.exists(f"{path}/{folder}"):
                os.mkdir(f"{path}/{folder}")
            os.rename(f"{path}/{archives}",f"{path}/{folder}/{archives}")
            
