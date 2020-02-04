def play():
    import random
    lucky_num = random.randint(1, 10)
    limit = 3
    guess_num = int(input("Enter your guessing number between 1-9.\n ---> "))
    count = 1
    while guess_num != lucky_num and count < limit:
        if count < limit:
            print("Your guess in not right.")
            guess_num = int(input("Enter your another guess number.\n --->   "))
            count += 1
    if guess_num == lucky_num:
        print("\n \n Hurray! you guess a RIGHT NUMBER :) ")
    else:
        print(">>>>>>Gave Over!<<<<<<\n>>>You are out of moves.<<< ")

play()
ask_replay = input("Do you want to play this game again? Y/N \n ---> ")
if ask_replay == "Y":
    play()
else:
    print("Thank you for playing.")

