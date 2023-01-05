# Exercise 4.12

import random
def tortoise_move():
    move=random.randrange(1,10)
    pace=0
    if move>=1 and move<=5:
        pace=3
    elif move>=6 and move<=7:
        pace=-6
    else:
        pace=1
    return(pace)
        
def hare_move():
    move=random.randrange(1,10)
    pace=0
    if move>=1 and move<=2:
        pace=0
    elif move>=3 and move<=4:
        pace=9
    elif move==5:
        pace=-12
    elif move>=6 and move<=8:
        pace=1
    else:
        pace=-2
    return(pace)

print("BANG!!!!\nAND THEY'RE OF!!!!!")
toroise_position=0
hare_position=0    
for i in range(1,71):
    toroise_position+=tortoise_move()
    hare_position+=hare_move()
    if toroise_position <1:
        toroise_position=1
    if hare_position <1:
        hare_position=1
    if toroise_position==hare_position:
        print(f'{"OUCH!":>{toroise_position}}')
    else:
        print(f'{"T":>{toroise_position}}\n{"H":>{hare_position}}')
    if toroise_position>=70:
        break
    if hare_position>=70:
        break
    
if toroise_position>=70 and hare_position<70:
    print("TORTOISE WINS!!!YAY!!!")
elif hare_position>=70 and toroise_position<70:
    print("Hare wins. Yuch")
elif toroise_position>=70 and hare_position>=70:
    print('Its a tie')
    


    












