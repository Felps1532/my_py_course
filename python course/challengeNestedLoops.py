'''
I have to use nested loops to do this
'''

numbers = [5, 2, 5, 2, 2]

# first solution
for number in numbers:
    print('x'*number)

print('-'*20)

# second solution - I have to generate a String that contains 5 x's
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += 'x'
    print(output)

print('-'*20)

# I'll make the 'L' now
numbers = [2, 2, 2, 2, 5]

for number in numbers:
    output = ''
    for count in range(number):
        output += 'x'
    print(output)