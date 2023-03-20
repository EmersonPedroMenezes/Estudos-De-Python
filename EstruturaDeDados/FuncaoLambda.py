# Lambda é uma função pequena e sem nome
# Pode ter vários argumentos mas somente 1 expreção
# É muito utilizada dentro de outras funções 
# E deixa o código mais "clean"

""" def somar(x):
    return x + 10

print(somar(2)) """

""" somar10 = lambda x: x + 10
print(somar10(2)) """

somar10 = lambda x,y: x + y + 10
print(somar10(2, 4))