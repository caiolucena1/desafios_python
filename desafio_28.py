#URI1073

entrada = int(input())
if 5 < entrada < 2000:
     for i in range(2,entrada+1,2):
         saida = i**2
         print(f'{i}^2 = {saida}')

'''for i in range(6,1999,2):
    entrada = int(input())

    print(i)'''