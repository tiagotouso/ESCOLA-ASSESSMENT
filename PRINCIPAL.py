
from MENSAGEM import titulocentralizado, linha, mensagemRetornaOpcao
from CORES import corFont
from datetime import datetime, time, date

import pandas as pd
import random as rd
import os

os.system("color")


def tituloprograma():
    linha()
    titulocentralizado(corFont('ASSESSMENT', 'amar'))
    linha()


def importarQuestoes(qtquestoes):

    dados = pd.DataFrame()
    for arquivo in os.listdir('QUESTÕES'):

        if arquivo.find('.csv') > -1:
            dd = pd.read_csv('QUESTÕES//{0}'.format(arquivo), sep='\t', encoding='utf-16')
        elif arquivo.find('.xlsx') > -1:
            dd = pd.read_excel('QUESTÕES//{0}'.format(arquivo))

        dados = pd.concat([dados, dd])



    # SORTEAR NOMENTE XX QUESTÕES DE CADA MODULO
    if qtquestoes != 0:
        lista = []
        for materia in dados['materia'].unique():
            for modulo in dados[dados['materia'] == materia]['modulo'].unique():
                dd = dados[(dados['materia'] == materia) & (dados['modulo'] == modulo)]
                tamanho = len(dd)

                if tamanho >= qtquestoes:
                    lista.extend(rd.sample(list(dd.index), qtquestoes))
                else:
                    lista.extend(list(dd.index))

        dados = dados.query('index in {0}'.format(lista))

    dados.reset_index(inplace=True, drop=True)
    dados.fillna('', inplace=True)

    return dados


def filtrarQuestoes(dados, dic):

    listaindex = []
    for vl in dic.keys():
        dd = dados[dados['materia'] == vl]
        listaindex.extend(rd.sample(list(dd.index), dic[vl]))

    resultado = dados.query('index in {0}'.format(listaindex))
    resultado.to_csv('_questoes_sorteadas.csv', sep='\t', encoding='utf-16')

    return resultado


def filtrarQuestoesModulo(dados, dic):


    listaindex = []
    for mt in dic.keys():
        for md in dic[mt].keys():
            dd = dados[(dados['materia'] == mt) & (dados['modulo'] == md)]
            listaindex.extend(rd.sample(list(dd.index), dic[mt][md]))

    resultado = dados.query('index in {0}'.format(listaindex))

    return resultado


def sortearQuestoes(dados, quantidade):

    listaindex = list(dados.index)
    listasorteada = rd.sample(listaindex, quantidade)
    dados = dados.query('index in {0}'.format(listasorteada))

    return dados


def imprimirquestao(contador, materia, modulo, questao, questaoc = ''):

    print()
    print(materia)
    print(modulo)
    if questao[0] == '\n' and len(questao) > 0:
        questao = questao[1:]

    txtquestao = corFont("{0}) {1}".format(contador, questao), 'amar')
    print(txtquestao)
    # print(questaoc)
    if len(questaoc) > 0:
        print(corFont(questaoc, 'amar'))
    linha()


def corrigirquestao(ce, resposta, correcaotxt):

    pontuacaousuario = 0
    printrespostaacertiva = 'A acertiva está "Errada"'
    if ce == 'C':
        printrespostaacertiva = 'A acertiva está "Correta"'
        if resposta == '1':
            pontuacaousuario = 1
    else:
        if resposta == '0':
            pontuacaousuario = 1

    printrespostausuario = corFont('Que pena, você errou! : (', 'verm')
    if pontuacaousuario == 1:
        printrespostausuario = corFont('Parabéns, você acertou! : )', 'verd')

    linha()
    print(printrespostaacertiva)
    linha()
    print(printrespostausuario)
    linha()
    print(corFont(correcaotxt, 'amar'))
    linha()

    return pontuacaousuario


def desempenho(tabela, tbtemposimulado, tbtempoquestao):

    dados = pd.DataFrame(tabela, columns = ['MATÉRIA', 'MÓDULO', 'PONTOS'])

    tempo = pd.DataFrame(tbtempoquestao, columns=['MATÉRIA', 'MÓDULO', 'TEMPO'])
    tempo['TEMPO'] = tempo['TEMPO'].apply(lambda x: round(x / 60, 2))

    linha()
    print('DESEMPENHO')
    print('DESEMPENHO TEMPO')
    linha()
    print('TEMPO TOTAL')
    print('INÍCIO', tbtemposimulado[0])
    print('FIM', tbtemposimulado[1])
    print('TEMPO TOTAL', tbtemposimulado[2])
    linha()

    ddtempo = tempo.agg(TEMPO=('TEMPO', sum),
                        MÉDIA=('TEMPO', 'mean'))

    print('TEMPO LÍQUIDO')
    print(ddtempo)
    linha()

    ddtempo = tempo.groupby('MATÉRIA').agg(TEMPO=('TEMPO', sum),
                                           MÉDIA=('TEMPO', 'mean'))
    ddtempo.sort_values('MÉDIA', ascending=False, inplace=True)

    print(ddtempo)
    linha()

    ddtempo = tempo.groupby(['MATÉRIA', 'MÓDULO']).agg(TEMPO=('TEMPO', sum),
                                                       MÉDIA=('TEMPO', 'mean'))
    ddtempo.sort_values('MÉDIA', ascending=False, inplace=True)

    print(ddtempo)
    linha()

    input('Pressione uma tecla para continuar!')

    linha()
    print('DESEMPENHO')
    print('DESEMPENHO PONTOS')
    linha()

    tb = [[dados['PONTOS'].count(), dados['PONTOS'].sum(), dados['PONTOS'].sum() / dados['PONTOS'].count() * 100]]
    resultado = pd.DataFrame(tb,
                             columns=['QUATIDADES', 'PONTOS', 'DESEMPENHO'],
                             index=['GERAL'])

    datastr = str(datetime.now())[0:16].replace(':', '')
    resultado.to_csv("GERROT_DESEMPENHO//{0} RESULTADO TOTAL.csv".format(datastr), sep='\t', encoding='utf-16')
    print(resultado)
    print()
    linha()

    resultado = dados.groupby(['MATÉRIA']).agg(QUANTIDADES=('MATÉRIA', 'count'),
                                   PONTOS=('PONTOS', sum),
                                   DESEMPENHO=('PONTOS', lambda x: round(
                                       sum(x) / x.count() * 100)))

    resultado.to_csv("GERROT_DESEMPENHO//{0} RESULTADO TOTAL (MATÉRIA).csv".format(datastr), sep='\t', encoding='utf-16')
    print(resultado)
    print()
    linha()

    resultado = dados.groupby(['MATÉRIA', 'MÓDULO']).agg(QUANTIDADES=('MATÉRIA', 'count'),
                                               PONTOS=('PONTOS', sum),
                                               DESEMPENHO=(
                                               'PONTOS', lambda x: round(
                                                   sum(x) / x.count() * 100)))

    resultado.to_csv("GERROT_DESEMPENHO//{0} RESULTADO TOTAL (MATÉRIA - MÓDULO).csv".format(datastr), sep='\t', encoding='utf-16')
    print(resultado)
    linha()
    input()

def simuladotxt(dados):

    gabaritotxt = '\nGABARITO\n\n'
    provatxt = '\nCADERNO DE PROVAS OBJETIVAS\n\n'
    provatxtcorrigida = '\nCADERNO DE PROVAS OBJETIVAS\n\n'
    contador = 1
    linha = '-' * 40
    tbCE = []
    materia = ''
    for mt, mo, qt, qtc, ce, crr in dados[['materia', 'modulo', 'questao', 'questaocomplemento', 'c-e', 'correcao']].values:
        if mt != materia:
            provatxt += "{0}\n{1}\n".format(mt, linha)
            provatxtcorrigida += "{0}\n{1}\n".format(mt, linha)
            materia = mt

        if len(qtc) > 0:
            provatxt += "{0}) {1}\n{2}\n( ) CORRETO - ( ) ERRADO\n{3}\n".format(contador, qt, qtc, linha)
            provatxtcorrigida += "{0}) {1}\n{2}\n( ) CORRETO - ( ) ERRADO\n\n{3}\n{4}\n{5}\n".format(contador, qt, qtc, ce, crr, linha)
        else:
            provatxt += "{0}) {1}\n( ) CORRETO - ( ) ERRADO\n{2}\n".format(contador, qt, linha)
            provatxtcorrigida += "{0}) {1}\n( ) CORRETO - ( ) ERRADO\n\n{2}\n{3}\n{4}\n".format(contador, qt, ce, crr, linha)

        tbCE.append([contador, ce])
        contador += 1

    metade = int(len(tbCE)/2)
    for n in range(0, metade):
        n1, ce1 = tbCE[n]
        n2, ce2 = tbCE[n + metade]
        gabaritotxt += "{0})\t{1} ___\t\t{2})\t{3} ___\n".format(n1, ce1, n2, ce2)


    narquivo = "SIMULADOS//{0} SIMULADO.txt".format(str(datetime.now().date())[0:10])
    arq = open(narquivo, 'w', encoding='utf-16')
    arq.write(provatxt)
    arq.close()

    narquivo = "SIMULADOS//{0} SIMULADO - CORREÇÃO.txt".format(str(datetime.now().date())[0:10])
    arq = open(narquivo, 'w', encoding='utf-16')
    arq.write(provatxtcorrigida)
    arq.close()

    narquivo = "SIMULADOS//{0} SIMULADO - GABARITO.txt".format(str(datetime.now().date())[0:10])
    arq = open(narquivo, 'w', encoding='utf-16')
    arq.write(gabaritotxt)
    arq.close()


def simulado(dados):

    if input('Deseja salvar o simulado em txt: [s, S] ') in ['s', 'S']:
        simuladotxt(dados)

    linha()
    titulocentralizado('SIMULADO')
    linha()

    dados = dados.copy()
    tbtempoquestoes = []
    tb = []
    contador = 1
    clpontos = []
    his = datetime.now()
    for mt, md, q, qc, ce, c in dados[['materia', 'modulo', 'questao', 'questaocomplemento', 'c-e', 'correcao']].values:
        imprimirquestao(contador, mt, md, q, qc)
        contador += 1
        # HORA INICIAL DA QUESTÃO
        hiq = datetime.now()

        op = mensagemRetornaOpcao('A acertiva está Correta ou Errada ? ', '1, 0')

        # HORA FINAL DA QUESTÃO
        hfq = datetime.now()
        tbtempoquestoes.append([mt, md, (hfq - hiq).seconds])

        ponto = corrigirquestao(ce, op, c)
        tb.append([mt, md, ponto])
        clpontos.append(ponto)

        linha()
        input()

    datastr = str(datetime.now())[0:16].replace(':', '')

    dados['PONTOS'] = clpontos
    dados.to_csv('GERROT_ERROS//{0} ERROS.csv'.format(datastr), sep='\t', encoding='utf-16')

    txterros = 'QUESTÕES ERRADAS\n'
    for mt, md, qt, qtc, ce, c in dados[dados['PONTOS'] == 0][['materia', 'modulo', 'questao', 'questaocomplemento', 'c-e', 'correcao']].values:
        txterros += "\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n\n".format(mt, md, qt, qtc, ce, c)
        txterros += '-' * 50

    arq = open('GERROT_ERROS//{0} ERROS.txt'.format(datastr), 'w', encoding='utf-16')
    arq.write(txterros)
    arq.close()

    hfs = datetime.now()
    ts = hfs - his
    tbtempodesimulado = [his, hfs, ts]

    desempenho(tb, tbtempodesimulado, tbtempoquestoes )

'''-----'''


def menumultipro(dic, titulo):
    linha = '-' * 20
    print(linha)
    print(titulo)
    print(linha)
    print()

    lista = []
    for k, v in dic.items():
        print(k.rjust(2, '0'), '-', v)
        lista.append(k)

    print()
    print(lista)
    print(linha)
    while True:
        opcao = input('Escolha uma opção: ')
        opcao = opcao.split()
        validar = True
        for op in opcao:
            if not op in lista:
                validar = False

        if validar == True:
            break
        else:
            print('Opção inválida!')
            print('Escolha uma opção:', lista)

    valores = []
    for vl in opcao:
        valores.append(dic[vl])

    return valores


def verificarmenu(lista):
    while True:
        op = input('Escolha uma opção: ')
        if op in lista:
            return op
            break
        else:
            print('Opção inválida!')
            print('Escolha uma opção: ', lista)


def gerarmenuopcao(menu):
    menutxt = ''
    menuid = []
    for i in menu:
        menutxt += str(i) + '\n'
        menuid.append(str(int(i.split('-')[0])))
    menuitens = list(menu.keys())

    return menutxt, menuid, menuitens

def menuemconstrucao():
    print('Em construção')
    print('Em construção')
    print('Em construção')
    return True


def gerarmenu(menu, titulo):
    gerarmenuopcao(menu)
    a, b, c = gerarmenuopcao(menu)
    entrar = True

    while entrar:
        print('-' * 20)
        print(titulo)
        print('-' * 20)
        print(a)
        print(b)
        print('-' * 20)
        op = verificarmenu(b)

        opmenu = c[int(op) - 1]

        if str(type(menu[opmenu])) == "<class 'function'>":
            entrar = menu[opmenu]()
        else:
            gerarmenu(menu[opmenu], opmenu.split('-')[1])


def menu01():
    print('Fim do programa!')
    return False


def menu02():

    config = pd.read_excel("CONFIG.xlsx")
    dados = importarQuestoes(20)

    dic = {}
    for mt, qt in config[['MATÉRIA', 'QUESTÕES']].values:
        dic[mt] = qt

    dd = filtrarQuestoes(dados, dic)

    simulado(dd)

    return True


def menu03():

    dados = importarQuestoes(0)

    dic = {}
    contador = 1
    for vl in dados['materia'].unique():
        dic[str(contador)] = vl
        contador += 1

    materias = menumultipro(dic, 'SIMULADO ESCOLHENDO AS MATÉRIAS')

    dic = {}
    for mt in materias:
        linha()
        print(mt)
        opcaoqt = int(input('Informa a quantidade de questões: '))
        dic[mt] = opcaoqt

    dd = filtrarQuestoes(dados, dic)

    simulado(dd)

    return True


def menu04():

    dados = importarQuestoes(0)

    # ESCOLHENDO A MATÉRIA
    dic = {}
    contador = 1
    for vl in dados['materia'].unique():
        dic[str(contador)] = vl
        contador += 1

    materias = menumultipro(dic, 'SIMULADO ESCOLHENDO OS MÓDULOS')

    dic = {}
    for mt in materias:
        linha()
        dicm = {}
        contador = 1
        for vl in dados[dados['materia'] == mt]['modulo'].unique():
            dicm[str(contador)] = vl
            contador += 1
        modulos = menumultipro(dicm, mt)
        dict = {}
        for md in modulos:
            dict[md] = 0
        dic[mt] = dict

    linha()
    titulocentralizado('QUANTIDADE DE QUESTÕES')
    linha()

    for p1 in dic.keys():
        for p2 in dic[p1].keys():
            print('MATÉRIA:', p1)
            print('MÓDULO:', p2)
            opcaoqt = int(input('Informa a quantidade de questões: '))
            dic[p1][p2] = opcaoqt
            linha()

    dd = filtrarQuestoesModulo(dados, dic)

    simulado(dd)

    return True


def menu05():

    config = pd.read_excel("CONFIG - MEIO.xlsx")
    dados = importarQuestoes(20)

    dic = {}
    for mt, qt in config[['MATÉRIA', 'QUESTÕES']].values:
        dic[mt] = qt

    dd = filtrarQuestoes(dados, dic)

    simulado(dd)

    return True


def menu06():

    config = pd.read_excel("CONFIG.xlsx")
    dados = importarQuestoes(20)

    dic = {}
    for mt, qt in config[['MATÉRIA', 'QUESTÕES']].values:
        dic[mt] = qt

    dd = filtrarQuestoes(dados, dic)

    gabaritotxt = '\nGABARITO\n\n'
    provatxt = '\nCADERNO DE PROVAS OBJETIVAS\n\n'
    provatxtcorrigida = '\nCADERNO DE PROVAS OBJETIVAS\n\n'
    contador = 1
    linha = '-' * 40
    tbCE = []
    materia = ''
    for mt, mo, qt, qtc, ce, crr in dd[['materia', 'modulo', 'questao', 'questaocomplemento', 'c-e', 'correcao']].values:
        if mt != materia:
            provatxt += "{0}\n{1}\n".format(mt, linha)
            provatxtcorrigida += "{0}\n{1}\n".format(mt, linha)
            materia = mt

        if len(qtc) > 0:
            provatxt += "{0}) {1}\n{2}\n( ) CORRETO - ( ) ERRADO\n{3}\n".format(contador, qt, qtc, linha)
            provatxtcorrigida += "{0}) {1}\n{2}\n( ) CORRETO - ( ) ERRADO\n\n{3}\n{4}\n{5}\n".format(contador, qt, qtc, ce, crr, linha)
        else:
            provatxt += "{0}) {1}\n( ) CORRETO - ( ) ERRADO\n{2}\n".format(contador, qt, linha)
            provatxtcorrigida += "{0}) {1}\n( ) CORRETO - ( ) ERRADO\n\n{2}\n{3}\n{4}\n".format(contador, qt, ce, crr, linha)

        tbCE.append([contador, ce])
        contador += 1

    metade = int(len(tbCE)/2)
    for n in range(0, metade):
        n1, ce1 = tbCE[n]
        n2, ce2 = tbCE[n + metade]
        gabaritotxt += "{0})\t{1} ___\t\t{2})\t{3} ___\n".format(n1, ce1, n2, ce2)


    narquivo = "SIMULADOS//{0} SIMULADO.txt".format(str(datetime.now().date())[0:10])
    arq = open(narquivo, 'w', encoding='utf-16')
    arq.write(provatxt)
    arq.close()

    narquivo = "SIMULADOS//{0} SIMULADO - CORREÇÃO.txt".format(str(datetime.now().date())[0:10])
    arq = open(narquivo, 'w', encoding='utf-16')
    arq.write(provatxtcorrigida)
    arq.close()

    narquivo = "SIMULADOS//{0} SIMULADO - GABARITO.txt".format(str(datetime.now().date())[0:10])
    arq = open(narquivo, 'w', encoding='utf-16')
    arq.write(gabaritotxt)
    arq.close()

    return True



if __name__ == '__main__':

    tituloprograma()

    menu = {'01 - SAIR DO SISTEMA': menu01,
            '02 - MACRO SIMULADO PRÉ-PROGRAMADO': menu02,
            '03 - MICRO SIMULADO PRÉ-PROGRAMADO': menu05,
            '04 - SIMULADO ESCOLHENDO AS MATÉRIAS': menu03,
            '05 - SIMULADO ESCOLHENDO OS MÓDULOS': menu04,
            '06 - GERADOR DE PROVAS': menu06,
    }

    gerarmenu(menu, 'MENU PRINCIPAL')

    # dados = importarQuestoes()
    # dd = filtrarQuestoes(dados, {'RACIOCÍNIO LÓGICO': 2})
    # simulado(dd)

