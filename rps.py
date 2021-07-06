# its a simple game
import random

rock= 1
paper= 2
scice= 3

user =int(input("enter the number:  "))
bot = random.randrange(1,3)

if(user== bot):
    print("its draw")
else:
    if( user==1 and bot==2):
        print("bot have paper")
        print("bot is the winner")
    elif( user==1 and bot==3):
        print("bot have scissors")
        print("you have won")
    elif(user==2 and bot==1):
        print("bot have rock")
        print("you have won")
    elif(user==2 and bot==3):
        print("bot haves scissors")
        print("bot have won")
    elif(user==3 and bot==1):
        print("bot have rock")
        print("bot have won")
    elif( user==3 and bot==2):
        print("bot have paper")
        print("user have won")


