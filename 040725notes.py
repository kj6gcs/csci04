# 04-07-2025 Class Notes
#strings

#Strings have bunches of characters, each individual character has an index of where it is.
#example
#string:  H e l l o !
#indices: 0 1 2 3 4 5 (H is in 0 position, e in 1 position, etc.)
#To get a character from a string using an index:
greet = "Hello!" #(strings must use double quotes)
first = greet[0] #This gets only the character which is at Index Position 0, H in this case.
print("first", first)


#Slices (substrings)
#A slice in Python is a section of a larger thing (usually some kind of list)
longString = "I'm gonna write a whole sentence in here"
#String: I ' m  g o n n a ...
#indices:0 1 2 3 4 5 6 7 8 ...

#For slices, you need a range of characters to get, which is done based on indicies
#Either ou give it two numbers (starting and stopping index), or give it just one
# Or if you give it just one number, it will be either the start or the end of the string.
shortString = longString[0:3] #This will stop 1 before the second number.
print(shortString)
shortString = longString[10:15]
print("second:", shortString)
#with slices you can say the exact end and stat if you want, but oly 1 of the two numbers
# are required.
shortString = longString[:3] #without a start index, it will start at 0.
print(shortString)
shortString = longString[15:]
print(shortString)
#Indices can e variables rather than plain nubers.
index = 8
shortString = longString[index]
print(shortString)

#In code, capital  and lowecase call are not the same, even if they aren't, even if theyre the same letterl
#Built in functions: topper() and low.variable
low = "hey"
low = low.upper()
print(low)

#If you want to know how long a string is, you can get it's lengt with len().
longLength = len(longString)
print("length:", longLength)

#The way for loops work in this languagrd:
#   for variable in lit:
#q  each time this repeats, the next thing in the list goes into the the variable

#to loop through a string:
someStr = "Hey, it's raining outside"
for current in someStr:
    print(current)