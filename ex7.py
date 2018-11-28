#printing out mary had a little lamb.
print("Mary had a little lamb.")
#using str.format to insert snow into curly braces.
print("Its fleece was white as {}.".format('snow'))
#printing where mary went
print("And everywhere that Mary went.")
#Printing out 10 periods by multiplying the string 10 times.
print("." * 10) # what'd that do?

#assigning each of these letters a variable so they spell out cheeseburger when you combine them in a string.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that comma at the end. try removing it to see what it happens
#blows up with syntax error when you remove it, because it is actively acting like a space.
# based on the multiple runs that comma will allow it to also show up on the same line for two print statements.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
