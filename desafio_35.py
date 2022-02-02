#URI 1113

def input_int():
    a,b = input().split()
    a,b = int(a), int(b)
    return a,b

x,y = input_int()

while x != y:
    if x > y:
        print('Decrescente')
    else:
        print('Crescente')
    x,y =  input_int()


