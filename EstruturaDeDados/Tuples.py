#É um tipo de lista com a diferença de que é imutável


cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(type(cores_list))
print(type(cores_tuple))


cores_list.append('roxo')

print(cores_list)