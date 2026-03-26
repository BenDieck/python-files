# I hate navigating directories. 

##In windows only: This is how you change a directory: 
    ##cd E:\Learning.Coding\Python Script

#Finds out what the current working directory is. 
import os
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

#List of sub directories inside of CWD
print("Files and directories inside the CWD:", os.listdir())

print("Before changing:", os.getcwd())
#os.chdir('E:')

#/Learning.Coding/Python Script
#Changes drive and then moves the working directory. 
os.chdir('E:')
os.chdir("/Learning.Coding/Python Script")
print("After changing:", os.getcwd())

#Use the import command to run scripts once you change the CWD to your file location. 
#import fortune_cookie.py
#NOTE:This only works once per session because Python knows it's already
#been imported.



#I don't understand how this works. 
#  exec(open('hello.py').read())