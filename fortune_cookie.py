#This is a random number generator.
import random
#Random Integer between (a,b)
# Here are some variables that might be able to be worked into shit later...But
fortune_10 = random.randint(1, 10)

my_day20 = random.randint(1, 10)

lucky_number = random.randint(1, 999)
#I was going to make this long ass list of variables and then use a bunch of if statements. But now I just have a 
#List of fortunes and adjectives that I can index by slicing. This is waaaaay more better than what my first idea was.
#Mostly I'm stoked that I did this before the tutorial told me how to do this, or explained what a tuplo or list, or slicing
#was, so I'm feeling pretty good about myself. 
fortune = ('0',
           'No one is trying to kill you.',
           'The horses are going to get out.',
           'You will have many fat children.',
           'You are about to get PAID!',
           'Be wary of your next fart.',
           'Never trust a dude in high heels.',
           'Epstein did it.',
           'Do you ever wonder where the stars go in the morning?',
           'You are going to go on a trip; probably.',
           'Don\'t eat blueberries.')

days = ('0','good','great','shit','fucking awesome','really kinda stabby','murderous','orgasmic','heroic','legendary','parent-life kind of')
#I made this as my_day is equal to a slice of the days tuplo, and the slice value is the variable equal to the random
#number generator. This is the first time I did this. Shut up. 
my_day = days[my_day20]

my_fortune = fortune[fortune_10]

print(f'You will have a {my_day} day. {my_fortune} Lucky Number:{lucky_number}')

