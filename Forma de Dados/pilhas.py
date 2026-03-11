# Conceito de pilha de dados

class Pilha():
    def __init__(self):
        self.pilha = []
    
    def adicionar(self, valor):
        self.pilha.append(valor)
        print(f'Foi adicionado {valor} na lista!')
        return self.pilha
    
    def remover(self):
        qnt = len(self.pilha) - 1
        self.pilha.pop(qnt)
        print(f'Foi removido o {qnt}º item da lista')
        return self.pilha
    
    def ver(self):
        print(f'Lista: {self.pilha}')

dados = Pilha()
dados.adicionar('Suco de Caju')
dados.adicionar('Sanduiche')
dados.adicionar('Celular')
dados.remover()
dados.ver()

#||||||||||||||||||||||||||||||||||||||||||||||
#||                                          ||
#||             JEFFERSON SILVA              ||
#||                                          ||
#||||||||||||||||||||||||||||||||||||||||||||||