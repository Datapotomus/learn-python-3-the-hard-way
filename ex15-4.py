from sys import argv

script, filename=argv
#Assigning variable txt, and opening a file
txt=open(filename)
#Printing out text with the filename variable you gave it. You could also use txt. Which I would probably do.
print(f"Here's your file {filename}:")
#doing a read function on the file that was the variable txt.
print(txt.read())