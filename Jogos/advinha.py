# Jogo de adivinhar numero
import random

numeros = []
for n in range(101):
    numeros.append(n)

nCerto = random.choice(numeros)
chances = 0
print('JOGO DO ADIVINHA\n')
while True:
    print('Eu escolhi um numero! Tente adivinhar!')
    nPlayer = int(input('Digite um numero: '))

    if (nPlayer < nCerto):
        print('É um numero maior!')
    elif (nPlayer > nCerto):
        print('É um numero menor!')
    else:
        print(f'\nVocê acertou após {chances} tentativas!')
        break
    
    chances += 1