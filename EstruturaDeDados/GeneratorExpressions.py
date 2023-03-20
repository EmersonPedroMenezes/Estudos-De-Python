from sys import getsizeof


#Uma forma mais rápida para as listas, dicionários e etc
#Menos memória alocada
#Valores em bytes



numeros = (x * 10 for x in range(1000000))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))