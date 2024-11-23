weight = float(input("Weight: "))
choose = input("(L)bs or (K)g: ")

if choose == "L" or choose == "l":
    print(f"You are {round(weight*0.453592, 2)} kilos")
elif choose == "K" or choose == "k":
    print(f"You are {round(weight/0.453592, 2)} pounds")
else:
    print("Please, try a valid character!") 
    
'''
teacher solution:
if choose.upper() == "L":
'''