print("welcome to swiggy")
brunch = input("what do you want to order? idly,dosa , vada \n ")
lunch = input("what do u like to have ? biryani, souththali, norththali \n")

bill = 0
if brunch == "idly":
    bill += 20
elif brunch == "dosa":
    bill += 30
else:
    bill += 40

if lunch == "biryani":
    bill += 100
elif lunch == "souththali":
    bill += 150
else :
    bill += 175
print(f"your final bill is {bill}")           

