#Escrita simples
#Utilizado para criar uma lista apartir de uma existente
#Expressão for item in item

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
#frutas2 = []

#for iten in frutas1:
#    if 'b' in iten:
#       frutas2.append(iten)

#print(frutas2)"""

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

frutas2 = [iten for iten in frutas1 if 'b' in iten]

print(frutas2)