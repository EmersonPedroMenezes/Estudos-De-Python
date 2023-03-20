# Exelente para testes
# Não realiza 'stop' no programa
# Pode costumizar uma mensagem para ser mostrada quando encontrar um erro

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe')