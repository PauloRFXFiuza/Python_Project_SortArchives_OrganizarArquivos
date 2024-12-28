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
Procedimento de Organização em Pastas

General Context: 
This code organizes files into different directories based on their extensions. 
It goes through a list of files, checks the extension of each one, and moves them to specific folders depending on the extension.

Detailed Explanation:
for archives in archivesList:

This loop goes through all the files present in the archivesList. The variable archives stores the name of each file during the iterations.
Example: If archivesList = ['file1.txt', 'file2.jpg', 'file3.pdf'], the loop will go through each of these files.

name, extension = os.path.splitext(f"{path}/{archives}")

The os.path.splitext() function splits the full file path (which includes the name and the extension) into two parts: the file name and its extension.
path is a variable that contains the directory where the files are located, and archives is the file name. 
The string f"{path}/{archives}" creates the full path to the file.
The result of the os.path.splitext() function is a tuple, where name receives the file name (without the extension) 
and extension receives the extension (with the dot).
Example:

If archives = 'file1.txt' and path = '/home/user/files', then:
name = '/home/user/files/file1'
extension = '.txt'
for folder in dictPaths:

This loop goes through the directories listed in dictPaths. dictPaths is a dictionary where the keys are folder names and the 
values are lists of file extensions that should be moved to those folders.

Example:

If dictPaths = {'Documents': ['.txt', '.pdf'], 'Images': ['.jpg', '.png']}, the code will go through the folders Documents and Images.
if extension in dictPaths[folder]:

This conditional checks if the file extension (obtained in step 2) is present in the list of extensions associated with the current directory (folder) 
in dictPaths.
In other words, it checks if the file should be moved to the folder folder.
Example:

If extension = '.txt' and dictPaths = {'Documents': ['.txt', '.pdf'], 'Images': ['.jpg', '.png']}, the condition extension in dictPaths[folder] 
will be true when folder = 'Documents'.
if not os.path.exists(f"{path}/{folder}"):

This conditional checks if the directory where the file should be moved (indicated by folder) does not exist yet. If it does not exist, the 
directory is created.
os.path.exists() checks if the directory exists, and if it returns False, the os.mkdir() function is called to create the directory.
os.mkdir(f"{path}/{folder}")

If the directory does not exist yet (as determined by the previous condition), the code creates the directory with the name specified 
by folder in the path directory.
Example:

If folder = 'Documents' and path = '/home/user/files', it will create the directory /home/user/files/Documents (if it does not exist yet).
os.rename(f"{path}/{archives}", f"{path}/{folder}/{archives}")

The os.rename() function is used to move the file from its original location (f"{path}/{archives}") 
to the new directory (f"{path}/{folder}/{archives}").
It effectively "renames" the file, moving it to the folder specified by folder.
Example:

If archives = 'file1.txt', path = '/home/user/files' and folder = 'Documents', the file file1.txt will be moved 
from /home/user/files/file1.txt to /home/user/files/Documents/file1.txt.

Summary of the Procedure:
The code goes through all the files in the archivesList.
For each file, it separates the file name and the extension.
Then, it goes through the dictPaths dictionary, which contains pairs of folders and associated extensions.
For each extension, if it matches the file's extension, the code checks if the corresponding directory exists. 
If it does not exist, it creates it.
The file is then moved to the corresponding directory.
Example Scenario:
Considering a scenario with the following data:

archivesList = ['file1.txt', 'file2.jpg', 'file3.pdf']
path = '/home/user/files'
dictPaths = {
    'Documents': ['.txt', '.pdf'],
    'Images': ['.jpg', '.png']
}
Step 1: file1.txt will be moved to the Documents folder (because .txt is in Documents).
Step 2: file2.jpg will be moved to the Images folder (because .jpg is in Images).
Step 3: file3.pdf will be moved to the Documents folder (because .pdf is in Documents).
This procedure is useful for automatically organizing files into directories based on their extensions. 

Contexto Geral:
Esse código organiza arquivos em diretórios diferentes com base em suas extensões. 
Ele percorre uma lista de arquivos, verifica a extensão de cada um e move-os para pastas específicas, dependendo da extensão.

Explicação Detalhada:
for archives in archivesList:

Este loop percorre todos os arquivos presentes na lista archivesList. A variável archives armazena o nome de cada arquivo durante as iterações.
Exemplo: Se archivesList = ['file1.txt', 'file2.jpg', 'file3.pdf'], o loop irá passar por cada um desses arquivos.

name, extension = os.path.splitext(f"{path}/{archives}")

A função os.path.splitext() divide o caminho completo do arquivo (que inclui o nome e a extensão) em duas partes: o nome do arquivo e sua extensão.
path é uma variável que contém o diretório onde os arquivos estão localizados, e archives é o nome do arquivo. 
A string f"{path}/{archives}" cria o caminho completo para o arquivo.
O resultado da função os.path.splitext() é uma tupla, onde name recebe o nome do arquivo (sem a extensão) 
e extension recebe a extensão (com o ponto).
Exemplo:

Se archives = 'file1.txt' e path = '/home/user/files', então:
name = '/home/user/files/file1'
extension = '.txt'
for folder in dictPaths:

Este loop percorre os diretórios listados em dictPaths. dictPaths é um dicionário onde as chaves são nomes de pastas e os 
valores são listas de extensões de arquivos que devem ser movidos para essas pastas.

Exemplo:

Se dictPaths = {'Documents': ['.txt', '.pdf'], 'Images': ['.jpg', '.png']}, o código irá percorrer as pastas Documents e Images.
if extension in dictPaths[folder]:

Esse condicional verifica se a extensão do arquivo (obtida na etapa 2) está presente na lista de extensões associada ao diretório atual (folder) 
em dictPaths.
Ou seja, verifica se o arquivo deve ser movido para a pasta folder.
Exemplo:

Se extension = '.txt' e dictPaths = {'Documents': ['.txt', '.pdf'], 'Images': ['.jpg', '.png']}, a condição extension in dictPaths[folder] 
será verdadeira quando folder = 'Documents'.
if not os.path.exists(f"{path}/{folder}"):

Este condicional verifica se o diretório onde o arquivo deve ser movido (indicando por folder) não existe ainda. Se não existir, o 
diretório é criado.
os.path.exists() verifica a existência do diretório e, se retornar False, a função os.mkdir() é chamada para criar o diretório.
os.mkdir(f"{path}/{folder}")

Caso o diretório ainda não exista (determinando pela condição anterior), o código cria o diretório com o nome especificado 
por folder no caminho path.
Exemplo:

Se folder = 'Documents' e path = '/home/user/files', isso criará o diretório /home/user/files/Documents (se ainda não existir).
os.rename(f"{path}/{archives}", f"{path}/{folder}/{archives}")

A função os.rename() é usada para mover o arquivo de seu local original (f"{path}/{archives}") 
para o novo diretório (f"{path}/{folder}/{archives}").
Isso efetivamente "renomeia" o arquivo, movendo-o para a pasta especificada por folder.
Exemplo:

Se archives = 'file1.txt', path = '/home/user/files' e folder = 'Documents', o arquivo file1.txt será movido 
de /home/user/files/file1.txt para /home/user/files/Documents/file1.txt.

Resumo do Procedimento:
O código percorre todos os arquivos na lista archivesList.
Para cada arquivo, ele separa o nome do arquivo e a extensão.
Depois, ele percorre o dicionário dictPaths, que contém pares de pastas e extensões associadas.
Para cada extensão, se ela corresponder à do arquivo, o código verifica se o diretório correspondente existe. 
Se não existir, ele o cria.
O arquivo é então movido para o diretório correspondente.
Exemplo Prático:
Imaginando um cenário com os seguintes dados:


archivesList = ['file1.txt', 'file2.jpg', 'file3.pdf']
path = '/home/user/files'
dictPaths = {
    'Documents': ['.txt', '.pdf'],
    'Images': ['.jpg', '.png']
}
Passo 1: file1.txt será movido para a pasta Documents (porque .txt está em Documents).
Passo 2: file2.jpg será movido para a pasta Images (porque .jpg está em Images).
Passo 3: file3.pdf será movido para a pasta Documents (porque .pdf está em Documents).
Esse procedimento é útil para organizar arquivos em diretórios baseados em suas extensões de forma automática. 
'''

for archives in archivesList:
    name, extension = os.path.splitext(f"{path}/{archives}")

    for folder in dictPaths:
        if extension in dictPaths[folder]:
            if not os.path.exists(f"{path}/{folder}"):
                os.mkdir(f"{path}/{folder}")
            os.rename(f"{path}/{archives}",f"{path}/{folder}/{archives}")
            
