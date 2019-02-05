from sys import argv

script, input_file=argv
# Defining function print_all with a argument of f. "f" will be the open contents of the input_file.
def print_all(f):
    #Using the print function to read out the contents of the input file. 
    print(f.read())
# Defining the function named rewind with the f argument that will eventually be the input_file contents when called.
def rewind(f):
    #Set's the file pointer back to the beginning of the file. Since everything in computers starts with 0 it is the beginning.
    #If you forget a good explanation is here. https://stackoverflow.com/questions/11696472/seek-function
    f.seek(0)
# Defining  the function print a line to recieve two arguments, the line count, and the file pointer.
def print_a_line(line_count, f):
    #It is printing out the line count, which it gets from the "current_line" variable below, and then is reading each line. Also note that the line count is just a increment of one. It doesn't actually correspond to the position of the file.
    print(line_count, f.readline())
#Using a variable to open a file, and read it's contents in so it becomes a file pointer.
current_file=open(input_file)
#printing out some text.
print("First let's print the whole file:\n")
#Invoking the print_all function, using the current_file which is now the file pointer to the contents of the file.
print_all(current_file)
#printing some text.
print("Now let's rewind, kind of like a tape.")
#Invoking the rewind function which takes you back to the beginning of the file.
rewind(current_file)
#printing some output.
print("Let's print three lines:")
#Defining a variable
current_line=1
#Invoking the print_a_line function, passing it the variable current_line, and then giving it the current_file file pointer.
print_a_line(current_line, current_file)
#Incrementing the curren_line variable by one
current_line=current_line + 1
#Invoking the print_a_line function, and passing it the current_line variable that has now been incremented by one, as well as the same file pointer. Since we already read in the first line, it will read in the second line of the file. 
print_a_line(current_line, current_file)
#incrementing the variable again
current_line=current_line+1
#Invoking the print_a_line function, and giving it the incrimented variable agian, along with the current_file again. it will read the next line in the file, and print that out.
print_a_line(current_line, current_file)
