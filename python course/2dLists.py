matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# It will print the second value of the first list
print(matrix[0][1])

print('-'*20)

for row in matrix:
    for item in row:
        print(item)
        