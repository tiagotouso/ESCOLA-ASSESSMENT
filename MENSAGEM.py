from datetime import date

tamanholinha = 50

def linha():
    global tamanholinha
    linha = '-' * tamanholinha
    print(linha)
    
def titulocentralizado(vltitulo):
    global tamanholinha
    print(vltitulo.center(tamanholinha))

def titulo(vltitulo):
    linha()
    titulocentralizado(vltitulo.center(tamanholinha))
    linha()
    print('')
    
def separador():
    print('')
    linha()
    linha()

def mensagem(vlmensagem):
    print('')
    print(vlmensagem)
    print('')

def mensagemInformacao(vlmensagem):
    linha()
    print('')
    titulocentralizado('INFORMAÇÃO')
    print('')
    print(vlmensagem)
    print('')
    linha()

def mensagemErro(vlmensagem):
    linha()
    print('')
    titulocentralizado('ERRO')
    print('')
    print(vlmensagem)
    print('')
    linha()

def verificarsair(valor):
    if valor in ['quit', 'QUIT']:
        return True
    else:
        return False

def mensagemSimNao(vlmensagem):
    reps = input(vlmensagem + ' (S) ')
    sair = verificarsair(reps)
    if sair == False:
        if reps in ['S', 's']:
            return 1
        else:
            return 0
    else:
        return True

def mensagemRetornaInteiro(vlmensagem):
    codigo = -1
    while codigo == -1:
        cdg = input(vlmensagem + ' - (0 - SAI) ')
        sair = verificarsair(cdg)
        if sair == False:
            if cdg.isalnum() == True and cdg.isalpha() == False:
                codigo = int(cdg)
                return codigo
            else:
                mensagemErro('VALOR DIGITADO NÃO É NUMÉRICO!')
        else:
            codigo = 0
            return True

def mensagemRetornaReal(vlmensagem):
    codigo = -1.0
    while codigo == -1.0:
        cdg = input(vlmensagem)
        sair = verificarsair(cdg)
        if sair == False:
            cdg = cdg.replace(',', '.')
            try:
                codigo = float(cdg)
                return codigo
            except:
                mensagemErro('VALOR DIGITADO NÃO É NOMETÁRIO!')
        else:
            codigo = 0
            return True


def mensagemRetornaData(vlmensagem):
    data = '20200101'
    while len(str(data)) == 8:
        dt = input(vlmensagem)
        sair = verificarsair(dt)
        if sair == False:
            dt = dt.replace('-', '')
            dt = dt.replace('/', '')
            if len(dt) == 4:
                ano = 2021
                mes, dia = dt[0:2], dt[2:]
            elif len(dt) == 8:
                ano, mes, dia = dt[0:4], dt[4:6], dt[6:]
            else:
                ano, mes, dia = 0, 0, 0
            try:
                data = date(int(ano), int(mes), int(dia))
                print((str(data)))
                return data
            except:
                mensagemErro('DATA INVÁLIDA!')
        else:
            data = '2020/01/01'
            return True

def mensagemRetornaOpcao(vlmensagem, lista):
    valor = ''
    lista = lista.split(',')
    for n, v in enumerate(lista):
        lista[n] = str(v).strip()
    while valor == '':
        vl = input(vlmensagem + str(lista))
        sair = verificarsair(vl)
        if sair == False:
            vl = str(vl).upper()
            if vl in lista:
                valor = vl
                return valor
            else:
                mensagemErro('DIGITE UM VALOR VÁLIDO! ' + str(lista))
        else:
            valor ='sair'
            return True

def mensagemRetornaString(vlmensagem):
    msg = input(vlmensagem)
    msg = str(msg).upper()
    return msg