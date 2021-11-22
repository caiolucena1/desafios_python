#URI 1047

entrada = input().split()
h_start = int(entrada[0])
m_start = int(entrada[1])
h_end = int(entrada[2])
m_end = int(entrada[3])

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
print(f'O JOGO DUROU {hours} HORA(S) E {min} MINUTO(S)')


#Nere, eu não me dei bem com datetime

'''
import datetime

entrada = input().split()
h_start = int(entrada[0])
m_start = int(entrada[1])
h_end = int(entrada[2])
m_end = int(entrada[3])

a = datetime.time(h_start, m_start)
b = datetime.time(h_end, m_end)
c= b - a

print(a, b, sep='\n')
'''