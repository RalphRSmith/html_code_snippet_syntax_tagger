'''
A module to tokenize html
'''
from typing import List, Type, Any
import d_stack
import html_defs

DEBUG = False

def tokenize(lines: Type[List[Any]]) -> List[Any]:
    '''Takes in a list of lines : str, returns a list of line tokens'''
    tokens = []  # will hold the line_tokens
    for i, line in enumerate(lines):
        line_tokens = list()
        matched_command=d_stack.D_Stack()
        working = ""
        for j, c in enumerate(line):
            if c == matched_command.top():
                if working:
                    line_tokens.append(working)
                line_tokens.append(c)
                matched_command.pop()
                working = ""
            elif c in html_defs.SINGLE or c in html_defs.PAIRS.keys():
                if working:
                    line_tokens.append(working)
                working = ""
                line_tokens.append(c)

                if c in html_defs.PAIRS.keys():
                    matched_command.push(html_defs.PAIRS[c])
            else:
                working += c

            if DEBUG:
                print(f"line iteration {i} and char iteration {j} current char {c}")
                print(f"outline {line_tokens}")
                print(f"tokens {tokens}")
                print(f"matched_command {matched_command}")
                print(F"working {working}")
                print()

        tokens.append(line_tokens)

    return tokens



def main():
    run_tests()



def run_tests():
    pass

if __name__ == "__main__":
    main()
