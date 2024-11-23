secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
    # a WHILE loop can also have an ELSE! Else will be executed if the while loop is completely completed.
else:
    print("Sorry, you failed. Try again!")