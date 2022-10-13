'''
A module to generate display code for my website
input: a file containing properly formatted html
output: a file with css tags added
'''
import html_tokenize
import parse
import generate_output_html

DEBUG = True


def load_code(code_file: str):
    '''Loads a code file'''
    with open(code_file, mode="r", encoding="UTF-8" ) as infile:
        lines = infile.read()

    return [lines]


def save_code(code: str, out_name: str):
    """Writes code to a file"""
    with open(out_name, mode="w", encoding="UTF-8") as f:
        f.write(code)



def program(file_name : str):
    """Runs the procedures to generate html output"""
    lines = load_code(file_name)
    if DEBUG:
        print("LINES")
        print(lines)
        print()


    tokens = html_tokenize.tokenize(lines)
    if DEBUG:
        print(f"The lenth of TOKENS is {len(tokens)}")
        for line in tokens:
            print(f"tokens: {line}")
            print()
            print(F"joined:\n{''.join(line)}")
            print()


    parsed = parse.process(tokens)
    if DEBUG:
        print("PARSED")
        print(parsed)


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
