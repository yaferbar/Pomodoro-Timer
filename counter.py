import time

'''
for minutes in range(5, -1, -1):
    for seconds in range(59, -1, -1):
        print(f"{minutes}:{seconds}")
        time.sleep(0.01) '''

minutes = 5
seconds = 60

while minutes > -1:
    minutes -= 1
    while seconds > -1:
        print(f"{minutes}:{seconds}")
        seconds -= 1
        time.sleep(0.01)


