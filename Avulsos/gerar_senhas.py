# Gerador de senhas
import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeros = ['0', '1', '2', '4', '5', '6', '7', '8', '9']
especiais = ['!', '@', '#', '$', '%', '&', '*', 'ç', '/', '~']

print('GERADOR DE SENHAS')
tamSenha = int(input('Informe o tamanho da senha a ser gerada: '))
senha = ''

for i in range(tamSenha):
    l = random.choice(letras)
    n = random.choice(numeros)
    e = random.choice(especiais)
    senha += f'{l}{n}{e}'

print(f'Senha gerada: {senha}')

#||||||||||||||||||||||||||||||||||||||||||||||
#||                                          ||
#||             JEFFERSON SILVA              ||
#||                                          ||
#||||||||||||||||||||||||||||||||||||||||||||||