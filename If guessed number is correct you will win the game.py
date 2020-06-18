win=44
guess=1
user_no=int(input("guess no b/w 1 to 100:"))
game_over=False
while not game_over:
    if user_no == win:
        print(f"you win in no of {guess} times")
        game_over=True
    else:
        if user_no < win:
            print("guess smaller no.")
            guess+=1
            user_no=int(input("guess again"))
        else:
                print("guess greater no.")
                guess+=1
                user_no=int(input("guess again"))
