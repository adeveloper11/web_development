command=" "
started=False
while True:
    command=input("Give command:").lower()
    if command=="start":
        if started:
            print("car is already started")
        else:
            started=True
            print("Car Started")
    elif command=="stop":
        if started:
            started=False
            print("car stopped")
        else:
            print("car already stopped")
    elif command=="quit":
        break
    elif command=="help":
        print("""
start - To start the car
stop - To stop the car
quit - To Exit
        """)
    else:
        print("Enterd command is wrong")