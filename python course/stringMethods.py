course = 'Python for Begginers'
print(course)
print(course.lower())
print(course.upper())
# length
print(len(course))
# find method -> return the index of a character
# it is case sensitive
print(course.find('p'))
print(course.find('Begginers'))
# replace method
print(course.replace('Begginers', 'Absolute Begginers'))

# it returns a boolean value. Remember, it is case sensitive
print('python' in course)
len()