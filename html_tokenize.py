'''
A module to tokenize html
'''
from typing import List
import d_stack
import html_defs

DEBUG = False

def tokenize(lines: List[str]) -> List[List[str]]:
    '''Takes in a list of lines : str, returns a list of line tokens'''
    # declaration of type
    tokens : List[List[str]]
    line_tokens : List[str]
    working : str

    tokens = []
    for i, line in enumerate(lines):
        line_tokens = []
        matched_command=d_stack.D_Stack()
        working = ""
        for j, c in enumerate(line):
            if c == matched_command.top():
                if working:
                    line_tokens.append(working)
                line_tokens.append(c)
                matched_command.pop()
                working = ""
            elif html_defs.is_binary_key_or_single(c):
                if working:
                    line_tokens.append(working)
                working = ""
                line_tokens.append(c)

                if html_defs.in_binary_pair_keys(c):
                    matched_command.push(html_defs.get_binary_complement(c))
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
    """Module main for test running """
    run_tests()



def run_tests():
    """ Function to run module level tests """
    # todo
    pass

if __name__ == "__main__":
    main()
