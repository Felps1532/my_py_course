'''
I need to type the right commands for the car : start, stop and quit
otherwise, it won't understand!
'''
answer = ""

while True:
    answer = input("> ").lower()

    if answer == "help":
        print("""
commands:
start - to start the car
stop  - to stop the car
quit  - to exit
        """)
    elif answer == "start":
        print("Car started... Ready to go!")
    elif answer == "stop":
        print("Car stopped.")
    elif answer == "quit":
        break
    else:
        print("I don't understand that...")

    '''
    DRY = Don't Repeat Yourself
    
    I am repeating the method "lower()" too many times!
    Let's decrease it
    
    I can use a tripple quote for long strings, instead of this:
    print("commands:\n"
            + "start - to start the car\n"
            + "stop  - to stop the car\n"
            + "quit  - to exit")

    I've changed "answer.lower() != "quit" to "True"
    cause now there's a break point in our code!
    
    when we use """""" to print, the text will be printed EXACTLY the way we wrote!
    '''
