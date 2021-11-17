
days = int(input())

years = int(days/365)
days %= 365

months = int(days/30)
days %= 30

print(
    f'{years} ano(s)',
    f'{months} mes(es)',
    f'{days} dia(s)',
    sep='\n'
    )
'''print(f'{months} mes(es)')
print(f'{days} dia(s)')'''

'''
#resolução encontrada no google

dias = int(input())

anos = int(dias/365)
dias -= anos*365 # dias passa a ter este valor: dias (inputado) - (anos*365)

meses = int(dias/30)
dias -= meses*30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)') '''