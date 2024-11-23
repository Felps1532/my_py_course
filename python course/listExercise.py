# Write a program to find the largest number in a list
numbers = [12, 50, 7, 3050]
biggestNumber = 0
for number in numbers:
    if number >= biggestNumber:
        biggestNumber = number
print(biggestNumber)