import random

# trial() is equivalent to:
# randomly selecting 200 integers between 0 and 500,
# mixing the bag,
# sampling 40 numbers from the bag, and
# finding how many numbers from sample that are divisible 3
def trial():
    # numbers_in_bag consists of 200 randomly selected integers between 0 and 500
    numbers_in_bag = [random.randint(0, 500) for i in range(200)]

    # random.shuffle mixes up the 200 numbers in the bag
    random.shuffle(numbers_in_bag)
    
    # sample without replacement 40 numbers from the bag
    sample = random.sample(numbers_in_bag, 40)

    # take all numbers in the sample and count how many are divisble by 3
    divisible_by_three = len([i for i in sample if i % 3 == 0])

    # return the number counted (# of numbers divisible by 3 in the sample of 4)
    return(divisible_by_three)

# simulation(num_trials) runs the trial() a given number times  
# and returns the average of all trials
def simulation(num_trials):
    average = 0
    num_eleven_mult_three = 0
    
    # run trial num_trials times,
    # num_eleven_mult_three counts the number of times that
    # the given trial had 11 multiples of three 
    for i in range (num_trials):
        current_trial = trial()
        if(current_trial == 11):
            num_eleven_mult_three += 1
        average += current_trial
        

    # average all the trials
    else:
        average /= num_trials

    # return the average
    return(average, num_eleven_mult_three)

# run one simulation() with 10000 trials 
num_trials = 10000
current_simulation = simulation(num_trials)

# outputs the results
print("On average, " + str(current_simulation[0])
      + " of the 40 sampled numbers were multiples of 3 \nand in "
      + str(current_simulation[1]) + " of the 10000 trials there were" 
      + " exactly 11 multiples of 3\nin the sample of 40 numbers.")

# I tested the simulation 3 times:
# Results:
# On average, 13.3344 of the 40 sampled numbers were multiples of 3 
# and in 1003 of the 10000 trials there were exactly 11 multiples of 3
# in the sample of 40 numbers.
#
# On average, 13.3327 of the 40 sampled numbers were multiples of 3 
# and in 1021 of the 10000 trials there were exactly 11 multiples of 3
# in the sample of 40 numbers.
#
# On average, 13.2817 of the 40 sampled numbers were multiples of 3 
# and in 1006 of the 10000 trials there were exactly 11 multiples of 3
# in the sample of 40 numbers.
#
