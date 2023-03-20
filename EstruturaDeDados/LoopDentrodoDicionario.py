aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True }

"""imprime somente as keys"""
""" for x in aluno:
    print(x) """

"""imprime somente os valores """
""" for x in aluno.values():
    print(x) """

"""imprime todas as informações no formato tuple"""
"""for x in aluno.items():
    print(x)"""

""" imprime as informações fora do formato da tuple """
for keys, values in aluno.items():
    print(keys, values)