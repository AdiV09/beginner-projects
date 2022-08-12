from datetime import datetime

hour = int(input("Enter alarm hour (24-hour): "))
minute = int(input("Enter alarm minute: "))

print("Alarm successfully activated\n")
while True:
    if datetime.now().hour == hour and datetime.now().minute == minute:
        print("Ring!")
        quit()
