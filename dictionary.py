#Dictionaries
# A dictionary is a type of set. A set can hold data of multiple types.
# A dictionary is different from a set because the information can follow a specific order, and is changeable.  
#Sets are UNORDERED, UNCHANGEABLE, and no NOT ALLOW DUPLICATES
# Dictionary: The Left side is known as the key, the right is the value; or output of the key when indexed
#
cats = {"Jane":6, "Tom":14, 'Sara':8}

#Just like a list or set you slice a dictionary to index the entry. Must use exact spelling. 
# Only key values will produce a result. Values will not reverse produce a key. 
print(cats['Jane'])

#Yooooooo.... Why are these in brackets for an append and not the swirly bullshit. Is this like, 
#I am slicing into it? There is not indexable value, so it knows I want it to create one?  
cats["Wilson"] = 2

print(cats)
#This is a delete command
del(cats['Tom'])

print(cats)

#How many entries are in cats
print(len(cats))

#I'm watching a tutorial, they want me to make a dictionary that has integer keys, and boolean values...
#I feel like this is making a transitional statement. Like lookup the result of a statement and if ever it 
#returns a certain value then run that particular code....



Integer = {1:False, 2:True, 3:False,4:True, 5:False, 6:True}