"""Module for parsing html tags

input:  assumes valid html tag, starting with "<" and ending with ">"
"""
from dataclasses import dataclass
from typing import List, Tuple
import html_defs

DEBUG = False

@dataclass
class ParsedToken:
    """  a token, type dataclass """
    token: str
    token_type: str


def is_operator(token: str):
    """returns true if the token is an HTML operator"""
    return token in html_defs.OPERATORS

def is_whitespace(token: str):
    """returns true if the token is a whitespace character"""
    return token in html_defs.WHITESPACE

def is_newline(token: str):
    """returns true if the token is a newline character"""
    return token == html_defs.NEWLINE


def parse_line(token_line: List[str]) -> List[ParsedToken]:
    """Parses a list of tokens

    returns the line as a list of parsedToken dataclass tuples"""
    info: List[str]
    types: List[str]
    tag: List[str]

    info = []
    types = []
    tag = []

    for token in token_line:
        if token == html_defs.START_TAG:
            if tag:
                info.append(''.join(tag))
                types.append(html_defs.L_TEXT)
                tag = []
            tag.append(token)
        elif token == html_defs.END_TAG:
            tag.append(token)
            if len(tag) > 1 and tag[1] == html_defs.COMMENT_START:
                tag_content, tag_type = parse_comment_list(tag)
            else:
                if DEBUG:
                    print("before calling parse_tag_list")
                    print(f"\tinfo len{len(info)}: {info}")
                    print(f"\ttypes len{len(types)}: {types}")
                    print()
                tag_content, tag_type = parse_tag_list(tag)
            info.extend(tag_content)
            types.extend(tag_type)
            tag = []
        else:
            tag.append(token)

    if DEBUG:
        print(f"info len{len(info)}: {info}")
        print(f"types len{len(types)}: {types}")


    if len(info) != len(types):
        raise Exception ("Error -> len(info) != len(types)")
    if html_defs.L_UNKOWN in types:
        raise Exception ("Unknown type in types list")

    return  [ParsedToken(tok, typ) for tok, typ in zip(info, types)]


def parse_comment_list(tag_token: List[str]) -> Tuple[List[str], List[str]]:
    """parses a comment line"""
    content: List[str]
    types:   List[str]


    content = ["".join(tag_token[:])]
    types = [html_defs.L_COMMENT]

    return content, types



def parse_tag_list(tag_token: List[str]) -> Tuple[List[str], List[str]]:
    """returns a parsed tag

    input:  a valid html tag with opening and closing brackets
    """
    content: List[str]
    types:   List[str]


    content = []
    types = []

    i = 0

    while i < len(tag_token):
        token = tag_token[i]

        if is_operator(token):
            content.append(token)
            types.append(html_defs.L_OP)

        elif is_whitespace(token):
            content.append(token)
            types.append(html_defs.L_WHITESPACE)

        elif is_newline(token):
            content.append(token)
            types.append(html_defs.L_NEWLINE)

        elif i < 3 and types[-1] == html_defs.L_OP:
            content.append(token)
            types.append(html_defs.L_ELEMENT)

        elif i > 2 and ((types[-2] == html_defs.L_ELEMENT
                            or types[-2] == html_defs.L_ATTRIBUTE_VALUE)
                or (types[-1] == html_defs.L_WHITESPACE and types[-2] == html_defs.L_ATTRIBUTE_NAME)
                or (types[-1] == html_defs.L_WHITESPACE and is_operator(tag_token[i+1]))):
            content.append(token)
            types.append(html_defs.L_ATTRIBUTE_NAME)

        elif i > 2 and ((token in html_defs.QUOTES) and
                ((types[-1] == html_defs.L_OP and (types[-2] == html_defs.L_ATTRIBUTE_NAME)))):
            end = token
            collapsed_attribute_name = [token]
            i += 1
            # while loop has no bounds check as the tag is guaranteed to be properly formed
            while tag_token[i] != end:
                collapsed_attribute_name.append(tag_token[i])
                i += 1

            collapsed_attribute_name.append(end)
            content.append("".join(collapsed_attribute_name))
            types.append(html_defs.L_ATTRIBUTE_VALUE)

        else:
            types.append(html_defs.L_UNKOWN)

        i += 1

    if DEBUG:
        print("in parse tag list")
        print(f"info len {len(content)}: {content}")
        print(f"types len {len(types)}: {types}")
        print()

    if len(types) != len(content):
        raise Exception("Error -> len(content) != len(types)")
    if html_defs.L_UNKOWN in types:
        raise Exception ("Unknown type in types list")

    return content, types


def process(token_lines: List[List[str]]) -> List[ParsedToken]:
    """Takes a line of tokens, returns parsed html"""
    return parse_line(token_lines[0])


def run_tests():
    """ Runs a simple test"""

    def test_one():
        sample_one = ['<', 'a', ' ', 'href', '=', '"', 'https:', '/', '/',
                    'www.w3schools.com', '"', '>', 'Visit', ' ', 'W3Schools', '<', '/', 'a', '>']

        test_parse_line = (parse_line(sample_one))

        solution = [ParsedToken(token='<', token_type='o'), ParsedToken(token='a', token_type='e'),
        ParsedToken(token=' ', token_type='w'), ParsedToken(token='href', token_type='an'),
        ParsedToken(token='=', token_type='o'),
        ParsedToken(token='"https://www.w3schools.com"', token_type='av'),
        ParsedToken(token='>', token_type='o'),
        ParsedToken(token='Visit W3Schools', token_type='t'),
        ParsedToken(token='<', token_type='o'), ParsedToken(token='/', token_type='o'),
        ParsedToken(token='a', token_type='e'), ParsedToken(token='>', token_type='o')]

        try:
            assert test_parse_line == solution
            print("passed")
        except AssertionError:
            print("*** failed ***")

    # invoke tests
    print(f"\nRunning {__file__} tests")
    print("-" * (14 + len(__file__)))
    tests = [test_one]
    for test in tests:
        print(f"{test.__name__}: ", end="")
        test()


def main():
    """ main function to run module tests """
    run_tests()


if __name__ == "__main__":
    main()
