#URI 1038

info = input().split()
codigo = int(info[0])
qtd = int(info[1])

if codigo == 1:
    total = 4.00*qtd
elif codigo == 2:
    total = 4.50*qtd
elif codigo == 3:
    total = 5.00*qtd
elif codigo == 4:
    total = 2.00*qtd
elif codigo == 5:
    total = 1.50*qtd

print(f'Total: R$ {total:.2f}')

'''
Código feito com a Iris

valor = input().split()
cod = int(valor[0])
qtd = int(valor[1])

if cod == 1:
    print(f'Total: R$ {qtd*4.00:.2f}')
elif cod == 2:
    print(f'Total: R$ {qtd*4.5:.2f}')
elif cod == 3:
    print(f'Total: R$ {qtd*5.00:.2f}')
elif cod == 4:
    print(f'Total: R$ {qtd*2.00:.2f}')
elif cod == 5:
    print(f'Total: R$ {qtd*1.50:.2f}')
    '''