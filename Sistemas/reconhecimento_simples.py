# "Reconhecimento facial" ao entrar em sala de aula

class Aluno():
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

class SalaDeAula():
    def __init__(self, curso: str, qntAlunos: int, alunos: list):
        self.curso = curso.upper()
        self.qntAlunos = qntAlunos
        self.alunos = alunos
        self.presentes = 0
        self.faltas = 0
    
    def confirmarPresenca(self, aluno: int):
        self.presentes += 1
        print(f'Presença do(a) {self.alunos[aluno].nome} confirmada!\nTotal: {self.presentes}\nFaltas: {self.faltas}\n----------------')
    
    def fecharEntrada(self):
        self.faltas = self.qntAlunos - self.presentes
        print(f'Porta fechada!\nAlunos presentes em sala: {self.presentes}\nQnt. Faltas: {self.faltas}')
    
    def listarAlunos(self):
        texto_alunos = 'LISTA DE ALUNOS CADASTRADOS NA SALA:\n\n'
        for aluno in self.alunos:
            texto_alunos += f'{aluno.nome}\n'
        print(texto_alunos)

alunos = [
    Aluno('Jefferson', 16),
    Aluno('João Lucas', 16),
    Aluno('Valmir', 16),
    Aluno('Jose Vinicius', 16),
    Aluno('Cicrilo', 16)
]
sala = SalaDeAula('Desenvolvimento de Sistemas', 10, alunos)
#sala.listarAlunos()
sala.confirmarPresenca(0)
sala.fecharEntrada()


#||||||||||||||||||||||||||||||||||||||||||||||
#||                                          ||
#||             JEFFERSON SILVA              ||
#||                                          ||
#||||||||||||||||||||||||||||||||||||||||||||||