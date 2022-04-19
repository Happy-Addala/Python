print("Welcome to Treasure Island")
direction = input("which direction do u want to go? Left , Right \n")

door = ("red" , "yellow" , "blue")
decision = ("wait" , "swim")

if direction == "Right" :
    print("Fall into hole. Game over")
else :
      desicion = input("Do u want to do ? swim , wait \n")

if decision == "swim":
    print("Attacked by Trout. Game over")  

else :
    door = input("choose a door?")  
     

if door == "red":
    print("Burnt by fire. Game over")
elif door == "yellow":
    print("you win")    
elif door == "blue":
    print("Eaten by beasts. Game over")
else :
    print("Game over")  


           