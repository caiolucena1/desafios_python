#URI 1180

n = int(input())

values = list(map(int, input().split()))
smaller = min(values)
position = 0

for i in range(n):
    if values[i] == smaller:
        position = i

print(f'Menor valor: {smaller}')
print(f'Posicao: {position}')