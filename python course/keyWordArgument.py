def greet_user(first_name, last_name):
    print(f'Hi, {first_name} {last_name}!')
    print('Welcome aboard')


# the print() function has a parameter/argument
print('parameter')
# using keywords doesn't matter the order of the arguments
greet_user(last_name='Smith', first_name='John')

# it might be more useful when we are dealing with numbers, cause, unlike words, we don't know exactly what they are
# dummy (fictícia) function
calc_cost(total=50, shipping=5, discount=0.1)

greet_user('Mary', 'Anna')