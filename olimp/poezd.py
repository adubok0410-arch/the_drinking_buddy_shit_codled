n = int(input())
path_length = 650
highest_speed = 0
fastest_train = ''
d = []
c = []
for i in range(n):
    info = input().split()
    name, departure_time, arrival_time = info
    departure_hour, departure_minute = map(int, departure_time.split(':'))
    arrival_hour, arrival_minute = map(int, arrival_time.split(':'))
    if arrival_hour < departure_hour:
        arrival_hour += 24
    departure_minutes = departure_hour * 60 + departure_minute
    arrival_minutes = arrival_hour * 60 + arrival_minute
    minutes = arrival_minutes - departure_minutes
    hours = minutes / 60
    speed = path_length // hours 
    d.append(speed)
    c.append(name)
print('The fastest train is', c[d.index(max(d))], '.')
print('Its speed is', max(d), 'km/h, approximately.')
