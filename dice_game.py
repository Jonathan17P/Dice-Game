from numpy import *      #Import everything from the Numpy package 
import random            #Import random for choosing 'n' elements of the two dice array         


def dice_game(target,rolls):                               #Defines the function "dice_game", which is a function of the number the player wishes to roll,'target', as well as, the number of rolls allowed to try and roll the 'target' number.
    #ply1=random.randint(2,12,size=rolls)
    #ply2=random.randint(2,12,size=rolls)
    #Creates a list of possible values a player can roll, given two 6-sided die, where the probabiity of rolling a given number is accounted for. We then randomly choose 'rolls' number of elements from this list and transform the new list into an array, so that we can perform aggregations on this new list. 
    ply1=array([random.sample([2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,11,11,12],rolls)])
    ply2=array([random.sample([2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,10,10,10,11,11,12],rolls)])
    #Defines the ply'm'sum as the sum of the array created above.
    ply1sum=ply1.sum()
    ply2sum=ply2.sum()
    #Conditional statement checking if the 'target' number is in either players array.
    if target in ply1:
     print("Congratulations player 1, you've won!") 
    elif target in ply2:
     print("Congratulations player 2, you've won!")
    #Determines which player has the smallest sum of numbers rolled.
    elif ply1sum > ply2sum:
     print("Congratulations player 2, you've won!")
    elif ply1sum < ply2sum:
     print("Congratulations player 1, you've won!")
    #Accounts for the case in which neither player rolled the 'target' number and the sum of each players array are the same. 
    else: 
     print("Sorry, nobody wins this game")
    #Displays what number each player rolled given some amount of rolls.
    print("Player 1, you rolled:   ",ply1)
    print("Player 2, you rolled:   ",ply2)


