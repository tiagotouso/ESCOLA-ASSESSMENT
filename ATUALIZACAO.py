import wget
import requests
import os

def AtualizarSistema():

    def lerArquivo():
        arquivo = open('archives.txt', 'r')
        texto = arquivo.read()
        arquivo.close()

        return texto

    acessointernet = False

    if str(requests.get('https://www.google.com.br')) == "<Response [200]>":
        print("Acesso a internet")
        acessointernet = True
    else:
        print("Sem acesso a internet")


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

            print('Programa atualizado com sucesso')
            input('Finalize o programa para atualizar')
        else:
            print("Sistema já está atualizado")

