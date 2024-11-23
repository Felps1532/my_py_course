numbers = [5, 2, 2, 7, 4]

# This method add a number in the end of the list
numbers.append(13)
print(numbers)

# This method inserts a number in our list at the position '0'
numbers.insert(0, 10)
print(numbers)

# This method removes a specific number from the list
numbers.remove(2)
print(numbers)

# It removes the LAST item of our list
numbers.pop()
print(numbers)

# It clears, remove all items, the entire list
numbers.clear()
print(numbers)

# It doesn't return an error, just a Boolean value
print(50 in numbers)

# It will count how many times the number 5 appears on the list
print(numbers.count(5))

# It will organize our list in ascending order
numbers.sort()
print(numbers)

# We can reverse the sort() for a descending list
numbers.sort()
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers2 = numbers

print(numbers.index(50))
