#This is how to create a user input in python

#spyder hates running this. 
#I haven't really tried it yet, but it will allow a user input as a variable
#into a function or command. All inputs come in as a string. 
#You have to tell the input to treat it as a different data type.

user_text = input('Enter some text: ')

upper_or_lower = input("Enter 1 to uppercase, and 2 to lowercase: ")

if upper_or_lower == '1':
    print(user_text.upper())
else:
    print(user_text.lower())


