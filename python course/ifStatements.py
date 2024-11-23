is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day!")
    print("Drink plenty of water!")
elif is_cold:
    print("It's a cold day!")
    print("Wear warm clothes!")
else:
    print("It's a lovely day!")
    
print("Enjoy your day! :)")

'''
EX:
Price of a house is $1M.

If buyer has good credit,
    they need to put down 10%
Otherwise
    they need to put down 20%
Print the down payment
'''

house_price = 1000000
good_credit  = True

if good_credit:
    print(f"Pay: ${house_price*.10}")
else:
    print(f"Pay: ${house_price*.20}")