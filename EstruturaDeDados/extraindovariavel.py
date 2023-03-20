produtos = ['Arroz', 'Feijão', 'Laranja', 'Banana']

item1, item2, item3, item4 = produtos

item1, item2, item3, *outros = produtos   
"""imprime somente os três primeiros itens e os outros itens a mais da lista"""

"""item1 = produtos[0]
item2 = produtos[1]
item3 = produtos[2]
item4 = produtos[3]"""


print(item1)
print(item2)
print(item3)
print(item4)
