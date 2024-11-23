# Write a program to remove the DUPLICATES in a list
numbers = [1, 14, 2, 14, 14, 1, 15, 14, 30]
# It must exclude the 1 and 14

print(numbers)

# My solution doesn't work properly!
for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)
print(numbers)

print('-'*20)

# Teacher solution:
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
