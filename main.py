'''
A module to generate display code for my website
input: a file containing properly formatted html
output: a file with css tags added
'''
from typing import List, Optional
import argparse
import os.path
import html_tokenize
import parse
import generate_output_html


DEBUG = False


def load_code(code_file: str) -> List[str]:
    '''Loads a code file'''
    with open(code_file, mode="r", encoding="UTF-8" ) as infile:
        lines = infile.read()

    return [lines]


def save_code(code: str, out_name: str) -> None:
    """Writes code to a file"""
    with open(out_name, mode="w", encoding="UTF-8") as outfile:
        outfile.write(code)



def program(file_name : str, out_file_name: Optional[str] = None) -> None:
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


    html_code = generate_output_html.generate(parsed)
    if DEBUG:
        print("HTML_LINES")
        print(html_code)

    # save or send to standard out
    if out_file_name:
        save_code(html_code, out_file_name)
    else:
        print(html_code)



def main():
    ''' Function to drive the Program '''
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="generate styled html code-block from raw html",
        usage="%(prog)s [option] path")

    parser.add_argument('-f', "--file",
                        type=str,
                        help="specify filename of raw-html")

    parser.add_argument('-o', "--outfile",
                        type=str,
                        help="specify output filename, if none specified, output goes to std out")

    args = parser.parse_args()

    # validate infile arguments
    if not args.file:
        parser.error("raw-html filename missing.  Usage: python main.py -f <filename>")

    _, f_extension = os.path.splitext(args.file)

    if not os.path.exists(args.file):
        parser.error("input file cannot be found")

    if f_extension not in [".html", ".txt"]:
        parser.error("please pass a file with the extension .html or .txt")


    program(args.file, args.outfile)


if __name__ == "__main__":
    main()
