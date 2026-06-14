import random

while True:
    equaller = 90
    print("=" * equaller)
    print("ROCK PAPER SCISSORS GAME ".center(equaller))
    print("=" * equaller)

    item_list = ("rock", "paper", "scissors")
    user_choice = (
        input("\n enter your move = (rock or paper or scissors) : ").lower().strip()
    )
    if user_choice not in item_list:
        print(" \ninvalid input !! try again ")
        continue

    computer_choice = random.choice(item_list)
    print(
        f"  user choice     : {user_choice}\n computer choice : { computer_choice} \n "
    )

    # CONDITIONS

    if user_choice == computer_choice:
        print(" match tie ")
    elif (
        (user_choice == "rock" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "rock")
    ):
        print("computer win \n ")
    else:
        print(" user win\n".center(equaller))

    play_again = (
        input(" \n do you wanna play again....(y/n)\n".center(40)).strip().lower()
    )
    if play_again == "y":
        print(" thanks for playing \n".center(equaller))

    elif play_again == "n":
        print("=" * equaller)

        print(" end game ~".center(equaller))
        print(" ~thanks for playing".center(equaller))
        print("=" * equaller)
        break
    elif play_again != "n" or "y":
        print(" ~".center(equaller))
        break
