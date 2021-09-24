
from colored import fg, bg, attr

def corFont(texto, pfont = 'bran', ptipo = 'nor'):

    tstylo = {'bol': 1, 'nor': 2, 'ris': 4, 'blin': 5}

    tfont = {'pret': '16', 'verm': '160', 'verd': '46', 'amar': '184', 'azul': '33',
             'cinz': '250', 'bran': '15'}

    texto = '%s%s%s%s' % (fg(tfont[pfont]), attr(tstylo[ptipo]), texto, attr('reset'))

    return texto



def corT(texto, pcortexto = 'bran', pcorfundo = 'pret', ptfont = 'nor'):
    '''
    FUNÇÃO PARA TROCAR A COR DO TEXTO NA TELA PRETA
    ENTRA
        ENTRA O TEXTO EM TXT (TXT), E A COR DO TEXTO (TXT) E A COR DO FUNDO (TXT) E O ESTILO DO TEXTO (TXT)
    SAI
        SAI O TEXTO FORMATADO (TXT){FORMAT COR}
    '''
    #Padrão de cor do sistema
    #normal negrito underline negative
    tstylo = {'nor': '0', 'bol': '1', 'und': '4', 'neg': '7'}

    tfont = {'pret': '30', 'verm':	'31', 'verd':	'32', 'amar':	'33', 'azul':	'34',
    'mage':	'35', 'cyan':	'36', 'cinc':	'37', 'cine':	'90', 'vermc': '91', 'verdc': '92',
    'amarc': '93', 'azulc': '94', 'magec': '95', 'cyanc': '96', 'bran':	'97'}


    fcor = {'bran': '40','verm': '41','verd': '42','amar': '184','azul': '44','lila': '45','cian': '46','cinz': '47','pret':'0'}

    corpadrao = '\033[0;0m'
    texto = '\033[' + tstylo[ptfont] +';' + tcor[pcortexto] +';' + fcor[pcorfundo] +'m' + texto + corpadrao
    #texto = '\033[' + tstylo[ptfont] +';' + tcor[pcortexto] +';' + fcor[pcorfundo] +'m' + texto + corpadrao

    return texto

def exemplo():
    print('ESTILO')
    txt = ''
    for vl in [1, 2, 4, 5]:
        txt += ('%s %s %s'%(attr(vl), vl, attr('reset')))
    print(txt)
    print()

    print('CORES DA FONTE')
    txt = ''
    for vl in range(1, 255):
        txt += ('%s %s %s'%(fg(vl), vl, attr('reset')))
    print(txt)
    print()

    print('CORES DE FUNDO')
    txt = ''
    for vl in range(1, 255):
        txt += ('%s %s %s'%(bg(vl), vl, attr('reset')))
    print(txt)
    print()


