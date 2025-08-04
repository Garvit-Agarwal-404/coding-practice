name_1=input("Enter your name: ").capitalize()
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
if(4>=hour<12):
    print(f"Good Morning {name_1}")
elif(12>=hour<18):
    print(f"Good Afternoon {name_1}")
else:
    print(f"Good Night {name_1}")