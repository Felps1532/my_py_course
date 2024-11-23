# single quote in the middle of the string
course = "Python's Course for Begginers"
print(course)

course2 = 'Python for "Begginers"'
print(course2)

# 3 quotes for long strings
course3 = '''
Hi, Felps,

Here is my first email for you.

Have a good day!
'''

# get the first character and the last one
course4 = 'Python for Begginers'
print(course4[1])
print(course4[-1])
# it prints "Pyt"
print(course4[0:3])
# "P" is excluded
print(course4[1:])
# it will print until the fifth position
print(course4[:5])

another = course[:]
print(another)

name = 'Felps'

print(name[1:-1])
print(len(name))