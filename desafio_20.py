#URI 1048

sal = float(input())

if sal >= 0 and sal <= 400.00:
    n_sal = sal * 1.15
    reaj = n_sal - sal
    print(f'Novo salario: {n_sal:.2f}')
    print(f'Reajuste ganho: {reaj:.2f}')
    print(f'Em percentual: 15 %')
elif sal > 400.00 and sal <= 800.00:
    n_sal = sal * 1.12
    reaj = n_sal - sal
    print(f'Novo salario: {n_sal:.2f}')
    print(f'Reajuste ganho: {reaj:.2f}')
    print(f'Em percentual: 12 %')
elif sal > 800.00 and sal <= 1200.00:
    n_sal = sal * 1.10
    reaj = n_sal - sal
    print(f'Novo salario: {n_sal:.2f}')
    print(f'Reajuste ganho: {reaj:.2f}')
    print(f'Em percentual: 10 %')
elif sal > 1200.00 and sal <= 2000.00:
    n_sal = sal * 1.07
    reaj = n_sal - sal
    print(f'Novo salario: {n_sal:.2f}')
    print(f'Reajuste ganho: {reaj:.2f}')
    print(f'Em percentual: 7 %')
elif sal > 2000:
    n_sal = sal * 1.04
    reaj = n_sal - sal
    print(f'Novo salario: {n_sal:.2f}')
    print(f'Reajuste ganho: {reaj:.2f}')
    print(f'Em percentual: 4 %')