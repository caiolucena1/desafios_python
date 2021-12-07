#URI 1117

entrada = float(input())

if 0 <= entrada >= 10:
    entrada_2 = float(input())

while entrada < 0 or entrada > 10:
    print('nota invalida')
    entrada = float(input())
    if 0 <= entrada <= 10:
        entrada_2 = float(input())
while entrada_2 < 0 or entrada_2 > 10:
    print('nota invalida')
    entrada_2 = float(input())
if 0 < entrada_2 <= 10:
    media = (entrada + entrada_2)/2
print(f'media = {media:.2f}')


'''
cont=0 
soma=0 

while cont<2:
    n1 = float(input())
    if(n1<0 or n1>10):
        print("nota invalida")
    else:
        soma+=n1
        cont+=1
    n2 = float(input())
    if(n2<0 or n2>10):
        print("nota invalida")
    else:
        soma+=n2
        cont+=1

    if(n1>=0 and n1<=10 and n2>=0 and n2<=10):
        cont+=2  
        break
print(f"media = {soma/2:.2f}")
    '''