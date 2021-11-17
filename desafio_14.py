# URI 1037

'''
O comando elif verifica a veracidade da informação caso o if anterior tenha retornado falso
e executa a primeira informação verdadeira existente

intervalos do exercicio: ([0,25], (25,50], (50,75], (75,100])

[...] significa que o intervalo é "maior ou igual"
(...] significa que o intervalor é "maior que" e "menor ou igual"
'''


value = float(input())

if 0 <= value <= 25:
    print("Intervalo [0,25]")

elif value > 25 and value <=50:
    print('Intervalo (25,50]')

elif (value > 50) and (value<=75):
    print('Intervalo (50,75]')

elif (value > 75) and (value <= 100):
    print('Intervalo (75,100]')

else:
    print('Fora de intervalo')