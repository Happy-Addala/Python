height = int(input("what is your height?\n"))
bill = 0
if height >= 120 :
    print("Welcome to the rollercoaster")
    age = int(input("what is your age?\n"))
    if age < 12:
        bill = 5
        print("chile ticket is $5: ")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7:")
    else:
        bill = 12
        print("adult tickets are $12: ")
    wants_photo = input("Do u want a photo? Y or N \n")  
    if wants_photo == "Y":
        bill +=3
        print(f"your final bill is {bill}")
else:
    print("you need to grow ")





