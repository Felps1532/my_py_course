'''
Now I need to improve the previous "carGame". The program need to print a message alerting me when I type the same command as above.
'''

answer = ""
previous_answer = ""

while True:
    answer = input(">>> ").lower()

    if answer == "help":
        print("""
commands:
start - to start the car
stop  - to stop the car
quit  - to exit
        """)
    elif answer == "start" and answer == previous_answer:
        print("The car has already started.")
    elif answer == "stop" and answer == previous_answer:
        print("The car is already stopped.")
    elif answer == "start":
        print("Car started...")
    elif answer == "stop":
        print("Car stopped.")
    elif answer == "quit":
        print("Bye!")
        break
    else:
        print("Sorry... I didn't understand.\nYou can type 'help'.")
    previous_answer = answer
