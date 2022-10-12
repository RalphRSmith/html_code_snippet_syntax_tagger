'''
A module to generate display code for my website
input: a file containing properly formatted html
output: a file with css tags added
'''
import d_stack
DEBUG = False


_PAIRS = {
    '<' : '>',
    '"' : '"',
}


_SINGLE = set(["="," "])


_HTMLSAFE = {
    '<' : "&lt",
    '>' : "&gt",
}


# load in data
def load_code(code_file: str):
    '''Loads a code file'''
    lines = list()  # holds all the lines
    l = list()      # holds a single lines
    with open(code_file, "r") as f:
        l = f.readline()
        while l:
            lines.append(l.rstrip())
            l = f.readline()
    return lines


# run tokenizer
def tokenizer(lines: list):
    '''Takes in a list of lines : str, returns a list of line tokens'''
    tokens = []  # will hold the line_tokens
    for i, line in enumerate(lines):
        line_tokens = list()
        matched_command=d_stack.D_Stack()
        working = ""
        for j, c in enumerate(line):
            if c == matched_command.top():
                line_tokens.append(working)
                line_tokens.append(c)
                matched_command.pop()
                working = ""
            elif c in _SINGLE or c in _PAIRS.keys():
                if working:
                    line_tokens.append(working)
                working = ""
                line_tokens.append(c)

                if c in _PAIRS.keys():
                    matched_command.push(_PAIRS[c])
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





def program(file_name):
    lines = load_code(file_name)
    tokens = tokenizer(lines)

    for line in tokens:
        print(f"tokens: {line}")
        print(F"joined: {''.join(line)}")
        print()


def main():
    '''Run a test'''
    code_filename="html_to_convert.html"
    program(code_filename)



if __name__ == "__main__":
    main()