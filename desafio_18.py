#URI 1046

hours = input().split()
start = int(hours[0])
end = int(hours[1])

if start < end:
    time = end - start
    
elif start >= end:
    time = (24 - start) + end

print(f'O JOGO DUROU {time} HORA(S)')

