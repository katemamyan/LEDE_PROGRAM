# Katya Mamyan
# 06 Jun 2025
# Homework 3, Part 1

# %% LISTS
# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
lst=[22, 90, 0, -10, 3, 22, 48]
# Display the number of elements in the list. When I say display, I just mean 'print'
print(f'the number of elements in the list: {len(lst)}')
# Display the 4th element of this list.
print(f'the 4th element of this list: {lst[3]}')
# Display the sum of the 2nd and 4th element of the list.
print(f'the sum of the 2nd and 4th element of the list: {lst[1]+lst[3]}')
# Display the 2nd-largest value in the list.
print(f'the 2nd-largest value in the list: {sorted(lst)[-2]}')
print(sorted(lst,reverse=True)[1])
# Display the last element of the original unsorted list
print(f'the last element of the original unsorted list: {lst[-1]}')
# Display the sum of all of the numbers divided by two.
print(f'the sum of all of the numbers divided by two: {sum(lst) / 2}')
# %%
# Print whether the median or the mean of the numbers is higher
if len(lst) % 2 == 1:
    median = sorted(lst)[len(lst) // 2]
else:
    median = (sorted(lst)[len(lst) // 2 - 1] + sorted(lst)[len(lst) // 2]) / 2
print(f'the median: {median}')

mean = sum(lst) / len(lst)
print(f'the mean: {mean}')



# %% LISTS

# Sometimes dictionaries are used to describe multiple aspects of a single object. 
# Like, say, a movie. Define a dictionary called movie that works with the following code.

movie = {"title":"The Lion King", "year":1994, "director":"Roger Allers"} 
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
# %%
# On the lines after that, add keys to the movie dictionary for budget and revenue 
# (you'll use code like movie['budget'] = 1000), and print out the difference between the two.

movie['budget'] = 45
movie['revenue'] = 978.8
# %%
print(f"The difference between revenue and budget is USD {movie['revenue'] - movie['budget']} million")
# %%
# If the movie cost more to make than it made in theaters, print "That was a bad investment". 
# If the film's revenue was more than five times the amount it cost to make, 
# print "That was a great investment." Otherwise print "That was an okay investment."
if movie['budget']>movie['revenue']:
    print("That was a bad investment")
elif movie['budget']<movie['revenue']:
    print("That was a great investment")
else:
    print("That was an okay investment")
# %%
# Sometimes dictionaries are used to describe the same aspects of many different objects. 
# Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, 
# Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. 
# (Tip: keeping it all in either millions or thousands is a good idea)

nyc_boroughs = {"Manhattan":1.6, "Brooklyn":2.6, "Bronx":1.4, "Queens":2.3, "Staten Island":0.47}

# Display the population of Brooklyn.
nyc_boroughs["Brooklyn"]

# Display the combined population of all five boroughs.
print(f'The population of all five boroughs is {sum(nyc_boroughs.values())} million')

# Display what percent of NYC's population lives in Manhattan.
print(f'The population in Manhattan is {nyc_boroughs["Manhattan"]/(int(sum(nyc_boroughs.values())))*100}% of NYC population')

# %%
