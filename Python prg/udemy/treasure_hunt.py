print('''
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888  
                                                             
''')
print("""Welcome to Treasure Island.
Your mission is to find the treasure. """)
step1=input("left or right?").lower()
if(step1=='left'):
    step2=input("swim or wait?").lower()
    if(step2=='wait'):
        step3=input("Which door.. red,blue or yellow? ").lower()
        if(step3=='red'):
            print("Burned by fire.Game Over.")
        elif(step3=='blue'):
            print("Eaten by beasts.Game Over.")
        elif(step3=='yellow'):
            print("You win!!")
        else:
            print("GAME OVER!!")

    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole.Game Over.")
    
