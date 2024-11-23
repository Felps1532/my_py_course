try:
    age = int(input('Age: '))
    print(age)
    income = 20000
    risk = income / age
# Instead of crashing the program, print this message!
except ZeroDivisionError:
    print('Age can not be zero!')
except ValueError:
    print('Invalid value!')
    