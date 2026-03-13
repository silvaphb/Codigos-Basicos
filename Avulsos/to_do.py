# Lista de tarefas to-do

class ToDo():
    def __init__(self):
        self.tarefas = []
    
    def addTask(self, nome: str):
        self.tarefas.append(nome)
        print('Tarefa adicionada com sucesso!\n')
    
    def delTask(self, index: int):
        for i, v in enumerate(self.tarefas):
            if index == i:
                self.tarefas.pop(i)
        print(f'Tarefa de Nº {index} removida!\n')
    
    def getTasks(self):
        text = ''
        for i, t in enumerate(self.tarefas):
            text += f'{i}. {t}\n'
        print(text)

lista = ToDo()

print('LISTA DE TAREFAS')
while True:
    print('1. Adicionar tarefa\n2. Deletar tarefa\n3. Listar tarefas\n4. Fechar')
    user = int(input('Selecione uma opção: '))
    match user:
        case 1:
            nome = input('Insira o nome da nova tarefa: ')
            lista.addTask(nome)
        case 2:
            index = int(input('Insira o numero da tarefa que deseja remover: '))
            lista.delTask(index)
        case 3:
            lista.getTasks()
        case 4:
            break
        case _:
            print('Opção invalida!')

#||||||||||||||||||||||||||||||||||||||||||||||
#||                                          ||
#||             JEFFERSON SILVA              ||
#||                                          ||
#||||||||||||||||||||||||||||||||||||||||||||||