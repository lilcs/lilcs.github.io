# Week 2 Activity 2
# This is a (simple) game to let the user guess a number.
# Like the MASH game, some of the provided code uses concepts
# you aren't familiar with -- but you can still complete it!

import random

secret_num = random.randint(1, 10)

# STEP ONE: Prompt the user to guess a number between 1 and 10 using input()
users_guess = ...

# This makes the computer treat users_guess as a number rather than a string
users_guess = int(users_guess)

# Now we'll tell the user if their guess was too high or too low

# While this condition is true, run the indented code. At the end of running it,
# go back to the condition and check it again...
while users_guess != secret_num:

    # STEP TWO: Write if statements to print whether users_guess is high or low
    # Hint: instead of using == for equals, use > for greater or < for less
    if...
    else...

    # STEP THREE: Then ask for another guess!
    users_guess = ...
    users_guess = int(users_guess)

    # Now the while loop goes back and checks its condition again.

print('Congrats! ' + str(users_guess) + ' was the secret number.')
