import sys
script, encoding, error=sys.argv

x=1
dot="."
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
    
    out_line=f"{cooked_string}\n"
    #out_line=f"Line {str(x)}: {raw_bytes} <===> {cooked_string}\n"
    out_file.write(out_line)
    x += 1


languages=open("lang_rev2.txt", encoding="utf-8")

lang_reverse="lang_rev2-decode.txt"
out_file=open(lang_reverse, 'w')

main(languages, encoding, error)
out_file.close()
print("<<< Ending Script")