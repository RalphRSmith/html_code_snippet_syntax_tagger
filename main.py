'''
A module to generate display code for my website
input: a file containing properly formatted html
output: a file with css tags added
'''
import html_tokenize
import parse
import generate_output_html

DEBUG = False


def load_code(code_file: str):
    '''Loads a code file'''
    lines = list()  # holds all the lines
    l = list()      # holds a single lines
    with open(code_file, mode="r", encoding="UTF-8" ) as f:
        l = f.readline()
        while l:
            lines.append(l.rstrip())
            l = f.readline()
    return lines


def save_code(code: str, out_name: str):
    """Writes code to a file"""
    with open(out_name, mode="w", encoding="UTF-8") as f:
        f.write(code)



def program(file_name : str):
    """Runs the procedures to generate html output"""
    lines = load_code(file_name)
    if DEBUG:
        print("LINES")
        for line in lines:
            print(f"Line: {line}")
        print()

    tokens = html_tokenize.tokenize(lines)
    if DEBUG:
        print("TOKENS")
        for line in tokens:
            print(f"tokens: {line}")
            print(F"joined: {''.join(line)}")
            print()


    parsed = parse.process(tokens)
    if DEBUG:
        print("PARSED")
        for i, line in enumerate(parsed):
            print(f"Line {i + 1}")
            for entry in line:
                print(f"{entry.token_type:2} : '{entry.token}'")
            print()

    html_code = generate_output_html.cleanse_and_style_tag(parsed)
    if DEBUG:
        print("HTML_LINES")
        print(html_code)

    save_code(html_code, f"output_{file_name}")


def main():
    '''Run a test'''
    code_filename="html_to_convert.html"
    program(code_filename)


if __name__ == "__main__":
    main()
