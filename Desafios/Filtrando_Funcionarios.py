#Desafio com 'Sets'

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:
Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia 
Lista3 = Funcionários que não tem carro 

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = [Ana, Marcos, Alice, Melissa]
turno_noite = [Pedro, Sophia, Bruno]
tem_carro = [Marcos, Alice, Bruno, Melissa]

'''

#Solução
funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

num1 = set(funcionarios)
num2 = set(turno_dia)
num3 = set(turno_noite)
num4 = set(tem_carro)

print('Funcionários que tem carro e trabalham a noite: ', num4 & num3)
print('Funcionários que tem carro e trabalham durante o dia: ', num2 & num4)
print('Funcionários que não tem carro: ', num4 ^ num1)

#Correção
#lsta1
#lista1 = set(tem_carro).intersection(turno_noite)
#print(lista1)
#lista2
#lista2 = set(tem_carro).intersection(turno_dia)
#print(lista2)
#lista3
#lista3 = set(funcionarios).difference(tem_carro)
#print(lista3)
