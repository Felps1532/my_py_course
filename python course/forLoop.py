'''
Usually used to iterate through COLLECTIONS!
'''
# for each
for item in "Python":
    print(item)
    
for item in ['A', 'B', 'C']:
    print(item)

# (start number, range and step)
for item in range(5, 10, 2):
    print(item)
    
prices = [10, 20, 100]
total = 0
# sum of the prices
for price in prices:
    total += price
print(f"Total: {total}")