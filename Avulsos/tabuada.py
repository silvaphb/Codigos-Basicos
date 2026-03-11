# Exibe toda a tabuada de um número informado pelo usuário

num = 0
tabuada = ''

print(r"\\\ TABUADA RAPIDA ///")
num = int(input('Insira o numero na qual deseja fazer a tabuada: '))
tabuada += f'TABUADA DO {num}:\n\n'
mults = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in mults:
    tabuada += f'{num}x{n} = {num * n}\n'
print(tabuada)

#||||||||||||||||||||||||||||||||||||||||||||||
#||                                          ||
#||             JEFFERSON SILVA              ||
#||                                          ||
#||||||||||||||||||||||||||||||||||||||||||||||