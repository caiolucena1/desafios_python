#URI 1047

'''entry = input().split()
h_start = int(entry[0])
m_start = int(entry[1])
h_end = int(entry[2])
m_end = int(entry[3])

total_minutes_start = h_start*60 + m_start #transformando horas em minutos e somando aos minutos ja existentes
total_minutes_end = h_end*60 + m_end #vale o comentário de cima

if total_minutes_start < total_minutes_end:
    dur = total_minutes_end - total_minutes_start
    hours = dur//60 #transformando os minutos em hora
    min = dur % 60 #pegando os minutos do resto da divisão

elif total_minutes_start >= total_minutes_end:
    dur = (1440 - total_minutes_start) + total_minutes_end #1440 minutos equivalem a 24h
    hours = dur//60
    min = dur % 60
print(f'O JOGO DUROU {hours} HORA(S) E {min} MINUTO(S)')'''


#Nere, eu não me dei bem com datetime


from datetime import datetime

entry = input()
entries = entry.split()
start_h = int(entries[0])
start_m = int(entries[1])
end_h = int(entries[2])
end_m = int(entries[3])

#day_end = 26 if end_h <= start_h else 25

day_end = 25
if start_h == end_h and start_m == end_m:
    day_end += 1
if end_h < start_h:
    day_end += 1
start = datetime(2021, 12, 25, start_h, start_m)
end = datetime(2021, 12, day_end, end_h, end_m)
c = end - start
total_seconds = int(c.total_seconds())
hours = total_seconds // 60 // 60
minutes = int(total_seconds / 60 % 60)
if hours < 0:
    hours = hours + 24

print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')
