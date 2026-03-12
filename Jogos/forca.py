# Jogo da forca
import random

palavras = {
    'baunilha': 'sabor',
    'predio': 'construção'
}

print('|||| JOGO DA FORCA ||||')
text = ''
tentativas = 5
print('Sorteando palavra...')
palavra = random.choice(list(palavras.keys()))
progresso = ['_'] * len(palavra)

while True:
    if tentativas == 0:
        print('Não foi dessa vez!')
        break

    texto = ' '.join(progresso)
    print(texto)

    dica = palavras[palavra]
    print(f'Dica: {dica} | Tentativas: {tentativas}\n\n')
    letra = input('Digite uma letra: ')

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                progresso[i] = letra.upper()
                print('\nVocê acertou!')
    else:
        print('\nVocê errou!')
        tentativas -= 1

    if not '_' in progresso:
        print('Você ganhou!')
        break

    
#||||||||||||||||||||||||||||||||||||||||||||||
#||                                          ||
#||             JEFFERSON SILVA              ||
#||                                          ||
#||||||||||||||||||||||||||||||||||||||||||||||   