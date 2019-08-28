#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                 # output a string.
colors = ['red','orange','yellow','green','blue','violet','purple'] # set up an list with 7 colors in it.
play_again = ''                     # set up an variable to store string which will be use to quit the while loop.
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'):   # get into the while loop if the variable play_again is not 'n' and 'no',
                                                    # which also mean it will quit the loop if play_again is 'n' or 'no'.
    match_color = random.choice(colors)    # randomly choose a color from the list 'colors' and store it into match_color.
    count = 0   # Set up and initialize a variable count.
    color = ''  # Set up and initialize a variable color.
    while (color != match_color):   # run the while loop while color is not equal to match_color.
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
                                                        # ask user to input a string of color and store it into variable color.
        color = color.lower().strip()                   # convert the string in the variable color to lower case and remove the
                                                        # spaces before and after the word.
        count += 1  # add one to count itself.
        if (color == match_color): # an if statement.
            print('Correct!')   # run and output the string if the condition is true.
        else:   # else statement.
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # run and output the string
                                                                                               # if the condition is false.
    print('\nYou guessed it in {0} tries!'.format(count))   # print out how many time the user guessed by using format.
    if (count < best_count):    # if statement with condition (count < best_count)
        print('This was your best guess so far!')   # print the string if the condition is true.
        best_count = count  # store the value of count into best_count if the condition is ture.
    play_again = input("\nWould you like to play again? ").lower().strip() # ask the user to play again or not by using input and convert
                                                                           # it into lower case and clear the spaces.
                                                                           # if the user enter 'n' or 'no', quit the while loop.
                                                                           # if the user enter other string, it will loop the while loop.
print('Thanks for playing!') # output a string.