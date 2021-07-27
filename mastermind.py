# mastermind program
# by Auzmyn, 2021

import random

if __name__ == '__main__':
    # build guessing sequence by crating four random numbers in between 1 and 9
    guessing_sequence = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]
    turn_counter = 0

    # starting text of game
    print("------------------------------------------------------------------------------------")
    print("Welcome to Mastermind!")
    print("------------------------------------------------------------------------------------")
    print("Guess a sequence of numbers")
    print(f"The sequence is {len(guessing_sequence)} digits (1-9) long. Duplicates are allowed!")
    print("------------------------------------------------------------------------------------")
    print("Enter your guesses:")

    while True:
        # start while loop and allow user input
        player_input_sequence = input()
        # check for input length, if too small or too big get new input
        if len(player_input_sequence) < len(guessing_sequence):
            print("Your input has not enough numbers!")
            continue
        elif len(player_input_sequence) > len(guessing_sequence):
            print("Your input has too much numbers!")
            continue
        # build a list of the user input
        string_input_sequence = [number for number in player_input_sequence]
        # convert user input into an integer
        try:
            input_sequence = list(map(int, string_input_sequence))
        except ValueError:
            print("One or more inputs are not a number!")
            continue
        # if sequence is guessed, break out of loop
        if guessing_sequence == input_sequence:
            break
        # build a dictionary of the amount of numbers in the guessing sequence to check for matches on wrong position
        sequence_dic = {}
        for i in guessing_sequence:
            if i in sequence_dic.keys():
                sequence_dic[i] += 1
            else:
                sequence_dic[i] = 1
        # build variables for match in right position and match in wrong position
        match_right_position = 0
        match_wrong_position = 0
        # compare every digit with guessing sequence to get matches
        for index, number in enumerate(input_sequence):
            # check for right position match. if found, reduce dic by one, increase right position counter, and remove
            # number from input sequence to not count it a second time later
            if number == guessing_sequence[index]:
                sequence_dic[number] -= 1
                match_right_position += 1
                input_sequence[index] = None
        for number in input_sequence:
            # if number in sequence, but on a different position, reduce dic by one and increase wrong position counter
            if number in sequence_dic.keys() and sequence_dic[number] > 0:
                sequence_dic[number] -= 1
                match_wrong_position += 1
            # if number can't be found it will simply be ignored
        # print results to player
        print(f"Amount of right numbers in right position: {match_right_position}")
        print(f"Amount of right numbers in wrong position: {match_wrong_position}")
        turn_counter += 1
    # if player found sequence congratulate them and end game
    print("You guessed correct, congratulations!")
    print(f"It took you {turn_counter} turns")
