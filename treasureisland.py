print("Welcome to Treasure Island")
direction = input("which direction do u want to go? Left , Right \n")
decision = input("what do u want to do ? swim or wait \n")


if (direction == "Left") and (decision == "wait"):
    door = input("which color do u want? red , blue , yellow \n")
    
else:
    print("Fall into a hole. Attacked by trout . Game Over")

   

if door == "red":
    print("Burnt by fire. Game over")
elif door == "yellow":
    print("you win")    
elif door == "blue":
    print("Eaten by beasts. Game over")
else :
    print("Game over")        
    


