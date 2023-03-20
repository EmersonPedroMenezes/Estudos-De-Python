# criar a classe

class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
    
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
        

# criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionarios('Emerson', 'Pedro', '07/09/2002')

# print
print(Funcionarios.nome_completo(usuario1))



