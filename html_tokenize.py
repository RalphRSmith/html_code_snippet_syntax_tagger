'''
A module to tokenize html
'''
import d_stack
import parse
import html_defs

DEBUG = False

def tokenize(lines: list):
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
            elif c in html_defs._SINGLE or c in html_defs._PAIRS.keys():
                if working:
                    line_tokens.append(working)
                working = ""
                line_tokens.append(c)

                if c in html_defs._PAIRS.keys():
                    matched_command.push(html_defs._PAIRS[c])
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
    '''Run a test'''
    code_filename="html_to_convert.html"
    program(code_filename)



def run_tests():
    """Test runner for highlight module"""

    PASSED = "passed"
    FAILED = "*** failed ***"

    # define tests
    def test_label():
        s = "abcd"
        t = "name"

        try:
            r = label(s, t)
            assert(r == f"<span class='{t}'>{s}</span>")
            print(PASSED)
        except assertionError:
            print(FAILED)

    # invoke tests
    print("Running tests")
    print("-" * 13)
    tests = [test_label]
    for test in tests:
        print(f"{test.__name__}: ", end="")
        test()

if __name__ == "__main__":
    main()
    #run_tests()
