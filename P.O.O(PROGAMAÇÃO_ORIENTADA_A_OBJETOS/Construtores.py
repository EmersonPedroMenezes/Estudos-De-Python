

# criar a classe

class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        

# criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionarios('Emerson', 'Pedro', '07/09/2002')

# print
print(usuario1.nome)
print(usuario2.nome)
print(usuario3.nome)
