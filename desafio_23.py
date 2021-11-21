#URI 1051

payment = float(input())

if payment <= 2000.00:
    print('Isento')
elif 2000 < payment <= 3000: # payment > 2000 and payment <= 3000
    tax = (payment - 2000) * 0.08
    print(f'R$ {tax:.2f}') 
elif 3000 < payment <= 4500:
    a = 1000 * 0.08
    b = (payment - 3000) * 0.18
    print(f'R$ {a + b:.2f}')
elif payment > 4500:
    a = 1000 * 0.08
    b = 1500 * 0.18
    c = (payment - 4500) * 0.28
    print(f'R$ {a + b + c:.2f}')