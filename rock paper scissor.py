import random

print("\n")
equaller=119
print("=" *equaller)
print("ROCK PAPER SCISSORS GAME " . center(equaller))
print("=" * equaller)
while True:


    item_list = ("rock", " paper", "scissor")
    user_choice = input("\n enter your move = (rock or paper or scissor) : ".lower())
    if user_choice not in item_list:
        print(" \ninvalid input !! try again ")
        continue
    

    computer_choice = random.choice(item_list)
    print(f"  user choice     : {user_choice}\n computer choice : { computer_choice} \n ")

    # CONDITIONS 

    if user_choice==computer_choice:
        print(" match tie ")
    elif (user_choice== "rock" and computer_choice== "paper" ) or (user_choice=="paper" and computer_choice== "scissor") or (user_choice== "scissor" and computer_choice=="rock"  ):
        print("computer win \n ")
    else:
        print (" user win\n" .center(equaller))

    play_again=input(" \n do you wanna play again....(y/n)\n".center(40))
    if play_again=="y":
        print(" thanks for playing \n".center(equaller))
    elif play_again=="n":
        print(" end game ".center(equaller))    
        break