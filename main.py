print("~Tunnels~")

print()

start = input("Wanna play? (y/n): ")

if start == "y" or start == "Y":
  print()
  
  print("Okay, let's start!")
  
  print()
  
  print("You are in a dark tunnel. You can go left or right.") 
  
  print()
  
  direction = input("Which way do you go? (l/r): ")

  if direction == "l" or direction == "L":
    print()
    
    print("You chose the right path!")
    
    print()
    
    direction_2 = input("There's two more paths which will you go through? (l/r): ")
    
    if direction_2 == "l" or direction_2 == "L":
      print()
      
      print("You walk into a man eating spider! It wraps you in its web and you are are eaten alive.")
      
      print("Game Over!")
      
    else: 
      print()
      
      print("You chose the right path!")
      
      print()
      print("You see the world full of live and run home!")
      
      print()
      
      print("You win!")

  else: 
    print()
    
    print("You got to the left and a huge snake wraps around you and squeezes til your eyes pop out of its sockets. You died.")





else: 
  print("Okay, bye!")