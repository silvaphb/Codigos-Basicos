# Cronometro
import time

print('--> CRONOMETRO <---')
clock = int(input('Insira o tempo a ser cronometrado (segundos): '))

for s in range(clock + 1):
    print(s)
    time.sleep(1)

print('--> FINALIZADO <--')