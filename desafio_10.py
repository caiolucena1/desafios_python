#URI 1009

nome = input()
salario = float(input())
vendas = float(input())
comissao = (vendas*0.15)
salario = (salario+comissao)
print(f"TOTAL = R$ {salario:.2f}")

'''vendedor = input()
sal_fixo = float(input())
total_vendas = float(input())

sal_comissao = total_vendas*0.15 + sal_fixo

print(f'TOTAL = R$ {sal_comissao:.2f}')
'''