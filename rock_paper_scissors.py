import random
choices=['rock','paper','scissors']
user_choice=input("Enter rock,paper,scissors: ")
computer_choice=random.choice(choices)
if user_choice==computer_choice:
    print("Tie")
elif(
    (user_choice=="rock" and computer_choice=="scissors") or
    (user_choice=="paper"and computer_choice=="rock")or
    (user_choice=="scissors"and computer_choice=="paper")
    ):
        print("You Win!")
else:
    print("Computer Wins")
    
