'''                                        USING A MATRIX                                             '''
import random
import time
# start=time.time()
def input_check(a):
    if str(a).upper()=="S":
        return 0
    elif str(a).upper()=="W":
        return 1
    elif str(a).upper()=="G":
        return 2
    else:
        print("enter one of the given options")
        return 3

def game(a):
    if a==3:
        return 0
    outcomes=[["D","W","L"],["L","D","W"],["W","L","D"]]
    b=random.randrange(3)
    if b==0:
        print("computer chose snake")
    elif b==1:
        print("computer chose water")
    else:
        print("computher chose gun") 
    outcome=outcomes[a][b]
    if outcome == "D":
        print("Draw")
    elif outcome == "L":
        print("Loose")
    elif outcome == "W":
        print("Win")
        
while True:
    e=int(input("enter 1 to play the game and 0 exit "))
    if e!=1:
        break
    # start=time.time()
    user_input=input("Enter s for snake,w for water and g for gun ")
    game(input_check(user_input))
print("thanks for playing the game")
# stop=time.time()
# print(stop-start)