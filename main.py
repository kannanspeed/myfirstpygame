print("Welcome to kannan py game")
name=input("enter your name: ")
helth=100
age=int(input("enter your age: "))
print( "hello", name, "you'r age is", age)

if age >=18:
  print("Now you are ready to play the game, Let's Start")

  qus=input("first choice left or right(left/right)? ").lower()


  if  qus ==  "left":
    qus =input("Nice you follow the path and reach the lake.....Do you Swim across or go around(across/around)? ")


    if qus=="around":
      print("you went around and reached the other side if the lake")

    elif qus=="across":

      print("you managed to get across, but were bit  a fish and lost 50 health.")   
      helth-=5
    qus=input("you notice a house and a river? Which do you go to (river/house)")

    if qus == "house":
        print("You go to the house and are greeted my the owner.... He doesn't like you and lose 5 health")
        helth-=50

        if helth <=0:
          print("you now have 0 health and lost the game.....!")
        else:
          print("you have survived ... and  win the Game!")  



  else:
   print("you lost")




else:
 print("You are not allowed to play the Game")
