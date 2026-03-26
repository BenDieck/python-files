#This is a random number generator.
import random
#Random Integer between (a,b)
random_10 = random.randint(1, 10)

#Now I am making a making 8 ball thing that seems to have skewed results.
random_3 = random.randint(1, 3)

if random_3 == 1:
    print("Yes.")
if random_3 == 2:
    print("No.")
if random_3 == 3:
    print("Maybe.")