#Quiz: Average Electricity Bill
# Write an expression that calculates the average of 23, 32 and 64.
# Place the expression in this print statement.
print((23 + 32 + 64)/3)
#Quiz: Calculate
# Fill this in with an expression that calculates how many tiles are needed.
print(9*7 + 5*7)
# Fill this in with an expression that calculates how many tiles will be left over.
print(17*6 - (9*7 + 5*7))

#Solution: Assign and Modify Variables

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)

#Solution: Changing Variables

crs_per_rab = carrots/rabbits

>>> crs_per_rab = carrots/rabbits
>>> print(crs_per_rab)
2.0

#Quiz: Which is denser, Rio or San Francisco?
print(san_francisco_pop_density > rio_de_janeiro_pop_density)
#Note other solutions are possible, like the one below, but take a moment to make sure you understand and appreciate the concise efficiency of the one line above!

if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print (True)
else:
    print (False)
    
#Quiz: Fix the Quote

# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

# TODO: Fix this string!
ford_quote = "Whether you think you can, or you think you can't--you're right."

# Quiz: Write a Server Log Message

print (username + " accessed the site " + url + " at " + timestamp + ".")

OR

message = username + " accessed the site " + url + " at " + timestamp + "."
print(message)


