from numpy import * 
import random


def dice_game(target,rolls):
    #ply1=random.randint(2,12,size=rolls)
    #ply2=random.randint(2,12,size=rolls)
    ply1=array([random.sample([2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,11,11,12],rolls)])
    ply2=array([random.sample([2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,11,11,12],rolls)])
    ply1sum=ply1.sum()
    ply2sum=ply2.sum()
    if target in ply1:
     print("Congratulations player 1, you've won!") 
    elif target in ply2:
     print("Congratulations player 2, you've won!")
    elif ply1sum > ply2sum:
     print("Congratulations player 2, you've won!")
    elif ply1sum < ply2sum:
     print("Congratulations player 1, you've won!")
    else: 
     print("Sorry, nobody wins this game")
    print("Player 1, you rolled:   ",ply1)
    print("Player 2, you rolled:   ",ply2)


