#This is our random number gen
import random
#This is a time function.
import time


print("Alright, so you want to guess some numbers.")
print("")
#This is putting in a pause in the program so that the system will count down
#prior to executing.
time.sleep(2)
print("Sounds...stupid...")
time.sleep(1)
print("Alright, fine... give me a second...")
time.sleep(4)
print("I'm a little hungover...")
time.sleep(2)
print("Alright, pick a number between 1 and 100...")
time.sleep(3)
print("Or leave, I don't give a shit.")
print("")
time.sleep(2)
print("")
guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guess_count = 1

time.sleep(1)

while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
        guess = int(input("You suck, you're shooting low. What is your guess?: "))
    else:
        guess = int(input("Wrong, you're aiming high. What is your guess?: "))
 

    
print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")