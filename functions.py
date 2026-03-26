info#We are going to try to make some functions.
#Def is define, define a function. 
def bark():
    print("Bark bark bitch!")
    print("Woof, I'm a dog!")
    
#This says what the function does, now you need to call the function. 
bark()


def bark():
    print("Bark bark bitch!")
    print("Woof, I'm a dog!")
    
#For every object in the range of 0 to 100, which those objects are now called x... 
#Run the bark function.
for x in range(100):
    bark()

#Explanation of parameters.
#These  parentheses that follow Hello are the parameter that you are trying to 
#get the function to utilize. The Hello function, is a function of name.     
def Hello(name):
    print(f"Hello {name}!")
#In this instance we make an f string that says where the variable name should
#be looked for in the function Hello, and what should be done to in.

#Now when we call Hello down here, we can input whatever variable we want to run
#the function for.     
Hello("Sam")

#Multiple parameters

def add_numbers(num1,num2):
    print(num1 + num2)

add_numbers(1,2)

#F string output of a function. 
def dog_info(name,age,plural):
    print(f"My dog\'s name is {name} and it is {age} {plural} old.")
#I tried to make it so that pural was conditional, but I can't figure it out.
#Moving on
dog_info("Spot",1,"year")

#In order to make the output of a function a piece of information to 
#work with we have to use the return function. 
#The return function turns the output into a usable integer so that we
#can perform another process with the result of the function. 
def double(number):
    return number * 2

print(double(50))

new_variable = double(5)

print(new_variable)

def yell(string):
    #Make sure you include these ending parenthesis on this. It made
    #my code run, but not error out. The two after "upper".
    return string.upper()

print(yell("Go fuck yourself!"))

#Now make it run with a for loop. 

curses = ['Shit!','Fuck!','piss!','cunt!','motherfucker!']

for item in curses:
    print(yell(item))
