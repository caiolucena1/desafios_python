#URI 1061

from datetime import datetime

start_day = input().split()
start_time = input().split()
end_day = input().split()
end_time = input().split()

start_day = int(start_day[1])
start_hour = int(start_time[0])
start_minutes = int(start_time[2])
start_seconds = int(start_time[4])

end_day = int(end_day[1])
end_hour = int(end_time[0])
end_minutes = int(end_time[2])
end_seconds = int(end_time[4])

start = datetime(2021, 4, start_day, start_hour, start_minutes, start_seconds)
end = datetime(2021, 4, end_day, end_hour, end_minutes, end_seconds)

duration = int((end - start).total_seconds())

days = duration // 86400
rest = duration%86400

hours = rest // 3600
rest = rest%3600

minutes = rest // 60
rest = rest%60

seconds = rest


print(
    f'{days} dia(s)', 
    f'{hours} hora(s)', 
    f'{minutes} minuto(s)', 
    f'{seconds} segundo(s)',
    sep='\n'
    )

'''qualquer = datetime(2011,4, 1, 0, 0, 0)+duration
print(qualquer.day-1)
print(qualquer.hour)
print(qualquer.minute)
print(qualquer.second)'''


