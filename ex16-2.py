from sys import argv

script, filename=argv

print(f"Opening file {filename}...\n")
target_file=open(filename)
print("Printing out contents of file.\n")
print(target_file.read())

print("Closing file...")
target_file.close()