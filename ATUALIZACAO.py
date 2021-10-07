import wget
import requests
import os
from MENSAGEM import titulocentralizado, linha

def AtualizarSistema():

    def lerArquivo():
        arquivo = open('archives.txt', 'r')
        texto = arquivo.read()
        arquivo.close()

        return texto

    acessointernet = False

    if str(requests.get('https://www.google.com.br')) == "<Response [200]>":
        linha()
        print("Sistema com acesso à internet")
        linha()
        acessointernet = True
    else:
        linha()
        print("Sistema sem acesso à internet")
        linha()


    if acessointernet == True:

        arquivoDisco = lerArquivo()
        os.remove('archives.txt')

        arquivo = "https://raw.githubusercontent.com/tiagotouso/ESCOLA-ASSESSMENT/main/archives.txt"
        wget.download(arquivo)

        arquivoDownload = lerArquivo()

        if arquivoDisco != arquivoDownload:

            for arquivo in arquivoDownload:
                link = "https://raw.githubusercontent.com/tiagotouso/ESCOLA-ASSESSMENT/main/{}".format(arquivo)
                wget.download(arquivo)

            linha()
            print('Sistema atualizado com sucesso')
            input('Finalize o Sistema para atualizar')
            linha()
        else:
            linha()
            print("Sistema já está atualizado")
            linha()

