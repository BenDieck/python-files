fav_movies = ['Sandlot', 'Dune','Starwars','Hamilton']
#Length of a list
print(len(fav_movies))
#Add a file to the list
fav_movies.append('Iron Man')

print(len(fav_movies))
#Put it in the middle of the list, use 0 based counting to count over positions.
#This is the second position and insert Batman into the list. 
fav_movies.insert(1,"Batman")

#Delete an item indexed at a specific location within the list.
#This is everything through that range.
del(fav_movies[0:5])
