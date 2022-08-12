from random import randint


def get_index(char, word):
    indexes = []
    index = 0
    for character in word:
        if char == character:
            indexes.append(index)

        index += 1

    return indexes


def list_to_string(p_list):
    r_string = ""
    for item in p_list:
        r_string += item

    return r_string


def hangman(enter_word):
    # Enter the word as a parameter. Don't let your opponent see!
    used_letters = []
    word = []
    list_word = []
    lives = 10
    for letter in enter_word:
        word.append("_")
        list_word.append(letter)

    while word != list_word and lives > 0:
        print(f"Word: {list_to_string(word)}")
        print(f"Used letters: {used_letters}")
        print(f"Lives: {lives}")
        guess = input("Enter a letter: ")
        if guess in used_letters:
            print("You already used that letter!\n")
            continue
        print()

        for letter in list_word:
            if letter == guess:
                for index in get_index(letter, list_word):
                    word[int(index)] = guess

        if guess not in list_word:
            lives -= 1
        used_letters.append(guess)

    if "_" not in word:
        print(f"Congrats! The word was '{enter_word}'!")

    else:
        print(f"You lost. The word was '{list_to_string(list_word)}'.")


#
# rock_paper_scissors()
hangman("houses")
