print("Type the filename:")
#This is a variable that then gets generated via input. file_again is essential the name of the file.
file_again=input("> ")
#Assigning a new variable as txt_again that you are just opening the file. Since you are using open it will hold all the text.
txt_again=open(file_again)
#printing out the text in the file again. You can use read on it, because you used open above to open the file as the variable.
print(txt_again.read())