phone = input('Phone: ')

# MY SOLUTION:
phoneStr = ''

for i in range(len(phone)):
    if phone[i] == '1':
        phoneStr += 'one '
    elif phone[i] == '2':
        phoneStr += 'two '
    elif phone[i] == '3':
        phoneStr += 'three '
    elif phone[i] == '4':
        phoneStr += 'four '
    elif phone[i] == '5':
        phoneStr += 'five '
    elif phone[i] == '6':
        phoneStr += 'six '
    elif phone[i] == '7':
        phoneStr += 'seven '
    elif phone[i] == '8':
        phoneStr += 'eight '
    elif phone[i] == '9':
        phoneStr += 'nine '

print(phoneStr)

print('-'*20)

# Teacher solution:
# Using a dictionary
phone = '4441'

digits_mapping = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}

# since we can't change each character in the string, like we do in arrays using its index, we create a new one to receive the values!
output = ''

# we do a for each, and increment the 'output' with the digits. With get() we compare the name of the field and get its value!
for ch in phone:
    output += digits_mapping.get(ch, "!") + ' '
print(output)