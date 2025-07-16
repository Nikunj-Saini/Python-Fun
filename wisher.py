import time
a = 12
b = 24
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))
if hour < a:
    print("GOOD MORNING")
elif hour >= a and hour < b:
    print("GOOD AFTERNOON")
else:
    print("GOOD NIGHT")


