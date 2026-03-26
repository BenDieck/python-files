#I like to put my variables at the top like a big boy. 

day = 21 

weight = 190.4

month = 'October'

temp = 25

age = 17


#I am creating a shorthand for my boolean values. 
T = True
F = False

light_is_on = F
front_door_open = F
#Anything single tabbed under the if statement is associated with the if statement
#It will run if the conditions of the if statement are met.
if light_is_on:
    print("The Light is On!")
    print("You're paying money for this!")
#This else statement is associated with the previous if statement. 
#Do not have the else statement tabbed over or it will not read as part of the if statement. 
else:
    print("I can't fucking see!")
    
    #This statement flush to the next line is not associated with the previous if statement. It will run regardless.
print("A lot of fuss over some lights.")
#This is a conditional like object permenance. It's saying does front_door_open exist as a reality in this environment.
#If it does at the moment then the condition of the argument has been met. 
if front_door_open:
    print("Dog's gonna get out.")
    print("Toooooooooom!")
#This is a more specified condition statement giving the condition that you are looking to be met. 
if temp <38:
    print('It\'s cold as hell outside!')
#This is an example from a tutorial that I am working with...kinda... 
#Ooh, this creates a space in coding if you need to add a gap between printed lines. 
print('')
print('There is a person.')   
if age >= 18:
    print('This is a voting adult.')
else:
    print('This is not a person yet. But they could be if they practice.')