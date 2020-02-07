# We're going to play MASH. Aka, tell fortunes!
# Some background on the game: http://www.liketotally80s.com/2006/12/mash-game/

# You can ignore these import statements for now.
# For future reference, they let us use extra useful functions.
import random
import time

# Nothing to change here. We're just printing a message,
# then waiting a little for dramatic effect.
print('Telling your future...')
time.sleep(1.5)

# STEP 1: Create string variables representing 4 possible professions.
# The first is done for you!
job1 = 'software engineer'
job2 = ____________
job3 = ____________
job4 = ____________

# Nothing to change here! (What do you think it's doing??)
list_of_all_jobs = [job1, job2, job3, job4]
your_job = random.choice(list_of_all_jobs)

# STEP 2: Let's choose 4 possible celebrity spouses.
# The first is done for you!
num_kids1 = 0
num_kids2 = ___
num_kids3 = ___
num_kids4 = __

# Again, nothing to change here!
list_of_num_kids = [num_kids1, num_kids2, num_kids3, num_kids4]
your_num_kids = random.choice(list_of_num_kids)

# STEP 3: Let's choose 4 possible places to live.
# The first is done for you!
location_1 = 'Paris, France'
location_2 = ___________
location_3 = ___________
location_4 = ___________

# Again, nothing to change here!
list_of_all_locations = [location_1, location_2, location_3, location_4]
your_location = random.choice(list_of_all_locations)

# STEP 4: Put it all together into a fortune!
# We might want something like:
# "You will be a software engineer with 0 kids in Paris, France."
# Concatenate the variables: your_job, str(your_num_kids), and your_location.
# str() turns a number into a string.
results = ____________________
print(results)

# STEP 5: If you have time, add another prediction to the fortune.
