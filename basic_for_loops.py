#Intro to for loops in Python
#I am calling all of these things number and for the rest
#of this line they will be considered to be number, and now for every value
#that you are counting thru range ten, have number equal to 'Hello World', and print it out.

for number in range(10):
    print('Hello World!')

    
for value in range(100):
    print(value)

#Idea is to print 40 values where every number is multiplied by two. Problem with this code is that it includes the 0 count. 

for value_2 in range (40):
    print(value_2*2)

#This version does not include the zero count

for value_2 in range (40):
    print((value_2 + 1) *2)

#Here is a new list.  
fav_movie = ['Star Wars', 'Dune','Moana']
#Everything in this list is now called a movie, 
#For each occurance in the list, print the value of the movie in the list. So the name of it. 
for movie in fav_movie:
    print(movie)
    