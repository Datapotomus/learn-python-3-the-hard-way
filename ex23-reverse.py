import sys
script, encoding, error=sys.argv

x=1
print(">>> Starting Script")
def main(language_file, encoding, errors):
    line=language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    global x
    next_lang=line.strip()
    raw_bytes=next_lang.encode(encoding, errors=errors)
    cooked_string=raw_bytes.decode(encoding, errors=errors)

    print("Line", str(x)+":", raw_bytes, "<===>", cooked_string)
    x += 1


languages=open("languages_rev.txt", encoding="utf-8")

main(languages, encoding, error)
print("<<< Ending Script")