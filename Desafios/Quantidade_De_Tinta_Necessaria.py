#Desafio com Funções 

''''
Criar um programa que calcula a quantidade de tinta necessária para 
pintar uma parede. O usuário deverá fornecer as seguintes informações:
Redimento, altura e largura.O programa deve mostrar na tela a mensagem
'Você necessita de x latas de tintas'
'''''
#Solução

#rendimento = float(input('Informe o rendimento: '))
#altura = float(input('Informe a altura da parede: '))
#largura = float(input('Informe a largura da parede: '))

#print('Você necessita de ', altura * largura / rendimento, 'latas de tinta')

#Correção
rendimento = float(input('Informe o rendimento: '))
altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))

def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f'Você precisa de {total} latas de tinta')

calculo_tinta()