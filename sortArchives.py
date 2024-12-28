'''
Sort Archives Project- By Paulo Fiuza- 12/28/2024
Projeto Organizador de Arquivos
'''

'''The Python "os" library is used to interact with the operating system in a cross-platform way.
A biblioteca "os" do Python é usada para interagir com o sistema operacional de forma multiplataforma.'''

import os

'''The tkinter.filedialog module is used to display dialog boxes related to file and directory handling in Tkinter, 
which is the standard Python library for creating graphical user interfaces (GUIs). 
It allows users to visually select files or folders.

O módulo tkinter.filedialog é usado para exibir caixas de diálogo relacionadas à manipulação de 
arquivos e diretórios no Tkinter, que é a biblioteca padrão do Python para criar interfaces gráficas (GUIs). 
Ele permite que os usuários escolham arquivos ou pastas de maneira visual.'''

'''
The askdirectory method displays a dialog box that allows the user to select a directory (folder) from their file system.
It returns the full path of the selected directory as a string.

O método askdirectory exibe uma caixa de diálogo que permite ao usuário selecionar um diretório (pasta) em seu 
sistema de arquivos. Ele retorna o caminho completo do diretório escolhido como uma string.'''

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

'''Sort Folders Procedure
Procedimento de Organização em Pastas'''

for archives in archivesList:

    '''The os.path.splitext() method from the os.path module is used to separate a file's name from its extension. 
    It returns a tuple containing two parts:
    The file name without the extension.
    The file extension (including the dot).

    O método os.path.splitext() do módulo os.path é usado para separar o nome de um arquivo de sua extensão. 
    Ele retorna uma tupla contendo duas partes:
    O nome do arquivo sem a extensão.
    A extensão do arquivo (incluindo o ponto).

    Procedure to separate the file extension from the file name.
    Procedimento para separar a extensão do nome do arquivo- Example (exemplo):
    C:/Users/paulo/Documents/Workspaces/Python_Project_SortArchives_OrganizarArquivos/folderExample/1730997221366.jpg'''

    name, extension = os.path.splitext(f"{path}/{archives}")