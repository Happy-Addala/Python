print("leap year")
a = int(input("Which year do you want to check?\n"))
if(a%4==0):
    if a % 100 == 0:
        if a % 400 == 0:
           print("Leap year")
        else:
          print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap Year.")              
       