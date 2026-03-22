import time


def Play(file, interval):
    print('Iniciando musica...\n')
    with open(file, 'r', encoding='utf-8') as f:
        music = f.readlines()
        
    for l in music:
        for i in l:
            print(i, end='', flush=True)

            print(f'|', end='', flush=True)
            time.sleep(interval)

            print('\b \b', end='', flush=True)