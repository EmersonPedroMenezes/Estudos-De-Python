#Desafio utilizando If, Elif, Else

#Criar um programa que dependendo da temperatura (em Celsius) do steak ele retorna ao ponto de cozimento. O usuário 
#deverá fornecer a temperatura
#Temperatura - Cozimento
#120°F ou 48°C - Rare(selada)
#130°F ou 54°C - Medium rare(Ao ponto para mal)
#140°F ou 60°C - Medium(Ao ponto)
#150°F ou 65°C - Medium well(Ao ponto para bem)
#160°F ou 71°C = Well done(Bem passada)

#Solução
carne = float(input('Informe a temperatura da carne: '))

 
if carne < 48:
    print('Carne abaixo do ponto!')
elif  carne >= 48 and carne < 54:
    print('Carne selada!')
elif carne >= 54 and carne < 60:
    print('Carne ao ponto para mal')
elif carne >= 60 and carne < 65:
    print('Carne ao ponto!')
elif carne >= 65 and carne < 71:
    print('Carne ao ponto para bem!')
else:
    print("Carne bem passada!")
