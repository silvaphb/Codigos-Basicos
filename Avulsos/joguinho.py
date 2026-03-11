# Pedra, papel, tesoura!
import random

opcoes = ['pedra', 'tesoura', 'papel']

while True:
    print('Pedra, Papel, Tesoura game!\n')
    player = input('Escolha, Pedra, Papel ou Tesoura: ').lower()
    npc = random.choice(opcoes)
    print(f'O computador escolheu: {npc}')
    if player == npc:
        print('EMPATE!')
    elif (player == 'pedra' and npc == 'tesoura') or \
         (player == 'papel' and npc == 'pedra') or \
         (player == 'tesoura' and npc == 'papel'):
        print('Você venceu! 🎇')
    elif player in opcoes:
        print('Você perdeu! 🎃')
    else:
        print('Opção invalida!')
    
    restart = input('Quer jogar novamente? (y/n) > ')
    if restart != 'y':
        break

#||||||||||||||||||||||||||||||||||||||||||||||
#||                                          ||
#||             JEFFERSON SILVA              ||
#||                                          ||
#||||||||||||||||||||||||||||||||||||||||||||||