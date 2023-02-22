""" 
@Author: Allwina
Last modified:22/02/23
Program to implement Guessing game
"""
import random
low =int(input("enter the lower range"))
high =int(input("enter the lower range"))
mynumber =random.randint(low,high)
count=0
while(1):
    count+=1
    usernumber=int(input("enter the guess within the limit  "))
    if usernumber>mynumber:
        print("Too big !!")
    elif usernumber<mynumber:
        print("Too small !!")
    else:
        print("Congratulations! you got it in",count,"tries")
        break
        

