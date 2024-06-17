#Instructions for user
print("INSTRUCTIONS \n 1. Use R for Rock. \n 2. Use P for Paper. \n 3.Use S for Scissors. \n 4.In case you want to exit Use E for quiting the game.")
#Modules
import random
import time

#Loading screen
print('LOADING....') 
time.sleep(3)

#Variables
c_score = 0
u_score = 0
lst = ['rock', 'paper', 'scissors']

#functioning of game
while True: 
    u_choice = input("Enter your choice: ")
    c_choice = random.choice(lst)
    if u_choice == 'R':
        if c_choice == 'paper':
            print("You Lose!")
            c_score += 1
            print(f"Your score = {u_score} \n Computer's score = {c_score}")
        elif c_choice == 'scissors':
            print("You won!")
            u_score += 1
            print(f"Your score = {u_score} \n Computer's score = {c_score}")
             
        else: 
            print("It's a draw!")
            print(f"Your score = {u_score} \n Computer's score = {c_score}")
             
    elif u_choice == 'P':
        if c_choice == 'scissors':
            print("You Lose!")
            c_score += 1
            print(f"Your score = {u_score} \n Computer's score = {c_score}")
             
        elif c_choice == 'rock':
            print("You won!")
            u_score += 1
            print(f"Your score = {u_score} \n Computer's score = {c_score}")
             
        else: 
            print("It's a draw!")
            print(f"Your score = {u_score} \n Computer's score = {c_score}")
             
    elif u_choice == 'S':
        if c_choice == 'rock':
            print("You Lose!")
            c_score += 1
            print(f"Your score = {u_score} \n Computer's score = {c_score}")
             
        elif c_choice == 'paper':
            print("You won!")
            u_score += 1
            print(f"Your score = {u_score} \n Computer's score = {c_score}")
             
        else: 
            print("It's a draw!")
            print(f"Your score = {u_score} \n Computer's score = {c_score}")
             
    elif u_choice == 'E':
        print('good bye..')
        break
    else:
        print('You entered the wrong choice Please re-enter your choice.')
         
        