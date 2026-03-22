

class Pilha():
    def __init__(self):
        self.dados = []
        self.operadores = ['+', '-', '*', '/', '%']
    
    def getDado(self, jumper: int = 0):
        posDado = len(self.dados) -1 - jumper
        dado = self.dados[posDado]
        print(dado)
    
    def addDado(self, value):
        if type(value) is int:
            self.dados.append(value)
        elif type(value) is str:
            if value in self.operadores:
                self.dados.append(value)
        else:
            return print('Value invalido!')
    
    def delDado(self):
        posDado = len(self.dados) -1
        self.dados.pop(posDado)