import random
def play():
    """
    This function starts the game if numanser = 1
    """
    num = random.randint(0,11)
    guess = int(input(">"))
    if guess == num:
        print("you win")
        exit()
    else:
        print("you lose")
        exit()



print("what is your name")
name = input(">")
print(f"welcome to Numbers",str(name))
print("[1]play")
print("[2] quit")
numanser = input(">")


if numanser == "1":
    play()