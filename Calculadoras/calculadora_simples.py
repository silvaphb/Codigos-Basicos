# Calculadora

def calcular_imc():
    print('\nCALCULAR IMC:\n')
    peso = float(input('Informe seu peso (Kg): '))
    altura = float(input('Informe sua altura (Cm): '))
    imc = peso / (altura * 2)
    status = 'Obeso' if imc > 25 else 'Dentro do padrão'
    print(f'Seu IMC: {imc}')
    print(f'Status: {status}')
    
def calcular_adicao():
    print('\nCALCULAR ADIÇÃO:\n')
    n1 = float(input('Informe o primeiro numero: '))
    n2 = float(input('Informe o segundo numero: '))
    soma = n1 + n2
    print(f'Resultado da soma: {soma}')
    
def calcular_subtracao():
    print('\nCALCULAR SUBTRAÇÃO:\n')
    n1 = float(input('Informe o primeiro numero: '))
    n2 = float(input('Informe o segundo numero: '))
    result = n1 - n2
    print(f'Resultado da subtração: {result}')
    
def calcular_multiplicacao():
    print('\nCALCULAR MULTIPLICAÇÃO:\n')
    n1 = float(input('Informe o primeiro numero: '))
    n2 = float(input('Informe o segundo numero: '))
    result = n1 * n2
    print(f'Resultado da multiplicação: {result}')
    
def calcular_divisao():
    print('\nCALCULAR DIVISÃO:\n')
    n1 = float(input('Informe o primeiro numero: '))
    n2 = float(input('Informe o segundo numero: '))
    result = n1 / n2
    resto = n1 % n2
    print(f'Resultado da divisão: {result}')
    print(f'Resto da divisão: {resto}')


print('CALCULADORA RAPIDA\n\n1. CALCULAR IMC\n2. CALCULAR ADIÇÃO\n3. CALCULAR SUBTRAÇÃO\n4. CALCULAR MULTIPLICAÇÃO\n5. CALCULAR DIVISÃO\n')
opcao = int(input('Informe a opção desejada: '))
match opcao:
    case 1:
        calcular_imc()
    case 2:
        calcular_adicao()
    case 3:
        calcular_subtracao()
    case 4:
        calcular_multiplicacao()
    case 5:
        calcular_divisao()
    case _:
        print('Opção invalida!')

#||||||||||||||||||||||||||||||||||||||||||||||
#||                                          ||
#||             JEFFERSON SILVA              ||
#||                                          ||
#||||||||||||||||||||||||||||||||||||||||||||||