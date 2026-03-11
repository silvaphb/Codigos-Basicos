# Sistema de criar usuarios em "Banco de Dados" da Seduc

class Usuario():
    def __init__(self, nome: str, idade: int, telefone: str, serie: int, escola: str, cidade: str):
        self.nome = nome.upper()
        self.idade = idade
        self.telefone = telefone
        self.serie = serie
        self.escola = escola
        self.cidade = cidade   
    
    def mudarTelefone(self, telefone: int):
        self.telefone = telefone
        print("Telefone alterado com sucesso!")

    def aprovarDeAno(self):
        if self.serie == 3:
            return print('Aluno terminou o ensino medio!')
        self.serie += 1
        print(f'Aluno aprovado para o {self.serie}º!')

User1 = Usuario('Jefferson Silva Rodrigues', 16, 86994614635, 1, 'Liceu Parnaibano', 'Parnaiba')
User2 = Usuario('João Lucas', 16, 86994614657, 1, 'Liceu Parnaibano', 'Parnaiba')
User3 = Usuario('Valmir Martins', 16, 86994610987, 1, 'Liceu Parnaibano', 'Parnaiba')
users = [User1, User2, User3]

texto_users = 'LISTA DE USUARIOS CADASTRADOS NO SISTEMA:\n\n'
for user in users:
    texto_users += f'{user.nome}:\nIdade: {user.idade}\nTelefone: +55 {user.telefone}\nSerie: {user.serie}\nEscola: {user.escola}\nCidade: {user.cidade}\n'
    texto_users += '----------------------------------------------------------------\n'

print(texto_users)

#||||||||||||||||||||||||||||||||||||||||||||||
#||                                          ||
#||             JEFFERSON SILVA              ||
#||                                          ||
#||||||||||||||||||||||||||||||||||||||||||||||