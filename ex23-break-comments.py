#Importing the sys module
import sys
#Using script to start tells pyhton to start passing in arguments with sys.argv at the end.
script, encoding, error=sys.argv

#Defining x as 1
x=1
#Defining a dot as a period.
dot="."
# Added a print statement that tells you where the print starts.
print(">>> Starting Script")
def main(language_file, encoding, errors):
    line=language_file.readline()
    global dot

    if line:
        dot += "."
        print(dot)
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    global x
    next_lang=line.strip()
    raw_bytes=next_lang.encode(encoding, errors=errors)
    cooked_string=raw_bytes.decode(encoding, errors=errors)
    
    print(f"{raw_bytes}\n")
    #out_line=f"Line {str(x)}: {raw_bytes} <===> {cooked_string}\n"
    #out_file.write(out_line)
    x += 1


languages=open("languages2.txt", encoding="utf-8")

#lang_reverse="lang_rev2.txt"
#out_file=open(lang_reverse, 'w')

main(languages, encoding, error)
#out_file.close()
print("<<< Ending Script")