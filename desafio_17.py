#URI 1042

#tentativa nº 7635
#codigo feito com a Iris

entrada = input().split()
n1 = int(entrada[0])
n2 = int(entrada[1])
n3 = int(entrada[2])

lista = [n1, n2, n3]
lista.sort()

for i in lista:
    print(i)

print('')

print(n1, n2, n3, sep='\n')

