from random import randint


def rock_paper_scissors():
    choices = ["r", "p", "s"]
    player = input("Choose r, p or s: ").lower()

    computer = choices[randint(0, 2)]

    if player == "r":
        if computer == "r":
            print("It's a tie!")

        if computer == "p":
            print("Computer wins!")

        if computer == "s":
            print("Player wins!")

    if player == "p":
        if computer == "r":
            print("Player wins!")

        if computer == "p":
            print("It's a tie!")

        if computer == "s":
            print("Computer wins!")

    if player == "s":

        if computer == "r":
            print("Computer wins!")

        if computer == "p":
            print("Player wins!")

        if computer == "s":
            print("It's a tie!")

    print(computer)


rock_paper_scissors()


