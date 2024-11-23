'''
Loops inside of loops
print this:
(0, 1)
(0, 2)
(0, 3)
(1, 0)
(1, 1)
(1, 2)
(1, 3)
.. until x=3
'''

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')