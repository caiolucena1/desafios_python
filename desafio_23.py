#URI 1051

payment = float(input())

if payment <= 2000.00:
    print('Isento')
elif 2000 < payment <= 3000: # payment > 2000 and payment <= 3000
    diff = payment - 2000
    tax = diff * 0.08
    print(f'R$ {tax:.2f}')

'''T R A V E I !'''