aluno = {'nome': 'Ana', 
'idade': 16, 
'nota_final': 'A', 
'aprovação': True, 
'materias':['Fisica', 'Matematica', 'Inglês'] }

""" o get('materias') imprime o resultado ['Fisica', 'Matematica', 'Inglês']  """
print(aluno.get('materias'))

""" mostra o numero de keys """
print(len(aluno))

""" dicionario de itens """
print(aluno.items()) 
""" dicionairo de keys """
print(aluno.keys()) 
""" dicionario de valores """
print(aluno.values()) 