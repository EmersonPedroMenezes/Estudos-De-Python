aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

#aluno['nome'] = 'Jose'
#print(aluno['nome'])
#print(aluno)

aluno.update({'nome': 'José', 'nota_final': 'B'})

del aluno['idade']
print(aluno)
#aluno.update({'endereco': 'Rua A'})
#print(aluno)
#print(aluno.get('endereco', 'Não existe'))
