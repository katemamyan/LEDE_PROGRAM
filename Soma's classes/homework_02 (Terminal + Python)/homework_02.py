# katya mamyan
# resubmission 20 jun 2025
# homework_02

# How old the user is
year_of_birth = int(input("What year were you born in?"))
while year_of_birth > 2025:
    year_of_birth = int(input("We are in 2025 now! Try again! What year were you born in?"))

age = 2025 - year_of_birth
print(f"You are {age} years old")

# In that time, how many times the user's heart has beaten.
human_heartbeats = 60 * 24 * 365 * age * 60
print(f'As you mentioned, you are {age} years old. Your heart has beaten {human_heartbeats} times in that time')

# In that time, how many times a blue whale's heart has beaten.
blue_whale_heartbeats = 60 * 24 * 365 * age * 14.5
print(f'The blue whales heart rate can drop to as low as 2 beats per minute and can increase to about 27 beats per minute. So the avarege is {blue_whale_heartbeats} times in that time')

# In that time, how many times a rabbit's heart has beaten. 
# If the answer to rabbit heartbeats is more than a billion, 
# say "XXX billion" instead of the very long raw number
rabbit_heartbeats = 60 * 24 * 365 * age * 160

if rabbit_heartbeats > 1000000000:
    rabbit_heartbeats_bn = rabbit_heartbeats / 1000000000
    print(f"A rabbit's heart has beaten {rabbit_heartbeats_bn:,.2f} billion times")

else:
    print(f"A rabbit's heart has beaten {rabbit_heartbeats:,} billion times")

# There are several ways to calculate and format/display numbers in Python – string addition, 
# f-strings, commas, etc etc etc. Redo one of the above questions above with another technique 
# and briefly explain the pros and cons of each approach.

# I personally like f-string, easy to use and compact, without additional commas etc. 

# Whether they are the same age as you, older or younger
# If older or younger, how many years difference

if age > 29:
    print(f"The user is older then me. The difference is {abs(29-age)}")
elif age < 29:
    print(f"The user is younger then me. The difference is {abs(29-age)}")
elif age == 29:
    print(f"We have the same age!")

# If they were born in an even or odd year

if year_of_birth % 2 == 0:
    print("You were born in an even year")
else:
    print("You were born in an odd year")

#How many times there has been a president from the Democratic Party in office since they were born (1980 onward, and each president only counts once)

presidents = [{"number" : 40,
              "name" : "Ronald Reagan",
              "party" : "Republican",
              "start_year" : 1981,
              "end_year" : 1989
              },
              {"number" : 41,
              "name" : "George Bush",
              "party" : "Republican",
              "start_year" : 1989,
              "end_year" : 1993
              },
              {"number" : 42,
              "name" : "Bill Clinton",
              "party" : "Democratic",
              "start_year" : 1993,
              "end_year" : 2001
              },
              {"number" : 43,
              "name" : "George Bush",
              "party" : "Republican",
              "start_year" : 2001,
              "end_year" : 2009
              },
              {"number" : 44,
              "name" : "Barack Obama",
              "party" : "Democratic",
              "start_year" : 2009,
              "end_year" : 2017
              },
              {"number" : 45,
              "name" : "Donald Trump",
              "party" : "Republican",
              "start_year" : 2017,
              "end_year" : 2021
              },  
              {"number" : 46,
              "name" : "Joe Biden",
              "party" : "Democratic",
              "start_year" : 2021,
              "end_year" : 2025
              },
              {"number" : 47,
              "name" : "Donald Trump",
              "party" : "Republican",
              "start_year" : 2025,
              "end_year" : "-"
              }
]
selected_presidents = []
for president in presidents:
    if president["start_year"]>year_of_birth or president["start_year"]>year_of_birth:
        if president["party"] == "Democratic":
            selected_presidents.append(president)
print(f"{len(selected_presidents)} times there has been a president from the Democratic Party in office since you were born")

# Which US President was in office when they were born (1980 onward)

for president in presidents:
    if president["start_year"]<=year_of_birth and president["end_year"]>=year_of_birth:
        print(f"{president["name"]} was in office when you were born")

# Can you think of another approach to #7 and/or #8 that you could have tried? Why is yours better? If you could not get #7/#8 to work, use this question to explain what you were trying to do.
# I know that the code written can definitely be optimized and improved, but at the moment it seems pretty good to me)






