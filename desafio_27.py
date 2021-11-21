#URI 1064

count_positive = 0
sum_positive = 0

for i in range(6):
    a = float(input())
    if a > 0:
        count_positive = count_positive + 1
        sum_positive += a
        average = sum_positive/count_positive
print(
    f'{count_positive} valores positivos',
    f'{average:.1f}',
    sep = '\n'
    )
