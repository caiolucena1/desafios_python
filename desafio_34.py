#URI 1114

password = int(input())

while password != 2002:
    print('Senha Invalida')
    password = int(input())
if password == 2002:
    print('Acesso Permitido')