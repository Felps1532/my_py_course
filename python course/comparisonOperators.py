temp = 30

if temp == 30:
    print(f"It's a hot day! {temp}ºC")
else:
    print("It's not a hot day!")
    
'''
exercise:
'''
name = input("Type your full name: ")

if len(name) < 3:
    print("Name must be at least 3 charactrers long!")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters!")
else:
    print("Name looks good!")