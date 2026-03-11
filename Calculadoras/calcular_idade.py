from datetime import datetime

def CalcularIdade(ano: int, mes: int):
    ano_atual = int(datetime.now().strftime('%Y'))
    mes_atual = int(datetime.now().strftime('%m'))
    diff = ano_atual - ano
    diff_mes = mes_atual - mes
    if diff_mes < 0:
        diff = diff - 1
    print('A sua idade é {}'.format(diff))

nascimento_ano = int(input('Insira o ano que você nasceu: '))
nascimento_mes = int(input('Insira o mes que você nasceu: '))
CalcularIdade(nascimento_ano, nascimento_mes)

#||||||||||||||||||||||||||||||||||||||||||||||
#||                                          ||
#||             JEFFERSON SILVA              ||
#||                                          ||
#||||||||||||||||||||||||||||||||||||||||||||||