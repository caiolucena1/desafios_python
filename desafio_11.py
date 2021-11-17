#URI 1010

pc1 = input().split()
cod1 = int(pc1[0])
qtd1 = int(pc1[1])
vl1 = float(pc1[2])

pc2 = input().split()
cod2 = int(pc2[0])
qtd2 = int(pc2[1])
vl2 = float(pc2[2])

vl_total = qtd1*vl1 + qtd2*vl2

print(f'VALOR A PAGAR: R$ {vl_total:.2f}')