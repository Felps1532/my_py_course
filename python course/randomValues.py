# random is a built in module, it is already created
import random

members = ['John', 'Mary', 'Bob', 'Mosh']

leader = random.choice(members)
print(leader)

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))
     
