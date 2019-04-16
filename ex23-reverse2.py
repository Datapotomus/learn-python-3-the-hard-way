import sys
script, encoding, error=sys.argv


def main(language_file, encoding, errors):
    line=language_file.readline()
    

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang=line.strip()

    cooked_string=next_lang.decode(encoding, errors=errors)
    raw_bytes=cooked_string.encode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages=open("lang_rev2.txt", "rb")

main(languages, encoding, error)