seconds = int(input())
hour = (seconds // 3600) % 24
minutes = (seconds // 60) % 60
sec = seconds % 60
if len(str(minutes)) < 2:
    minutes = '0' + str(minutes)
if len(str(sec)) < 2:
    sec = '0' + str(sec)
print(f'{hour}:{minutes}:{sec}')
