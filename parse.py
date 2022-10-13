"""Module for parsing html tags

input:  assumes valid html tag, starting with "<" and ending with ">"
"""
from collections import namedtuple
import html_defs

ParsedToken = namedtuple("ParsedToken", ["token", "token_type"])


def is_operator(token: str):
    """returns true if the token is an HTML operator"""
    return token in html_defs.OPERATORS

def is_whitespace(token: str):
    """returns true if the token is a whitespace character"""
    return token in html_defs.WHITESPACE


def parse_line(token_line: list) -> list:
    """Parses a list of tokens

    returns the line as a list of parsedToken named tuples"""
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
                tag_content, tag_type = parse_tag_list(tag)
            info.extend(tag_content)
            types.extend(tag_type)
            tag = []
        else:
            tag.append(token)

    if (len(info) != len(types)):
        raise Exception ("There is a error in the logic here somewhere")
    if (html_defs.L_UNKOWN in types):
        raise Exception ("Unknown type in types list")

    return  [ParsedToken(tok, typ) for tok, typ in zip(info, types)]


def parse_comment_list(tag_token):
    """parses a comment line"""
    content = ["".join(tag_token[:])]
    types = [html_defs.L_COMMENT]

    return content, types



def parse_tag_list(tag_token):
    """returns a parsed tag

    input:  a valid html tag with opening and closing brackets
    """
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

        elif i < 3 and types[-1] == html_defs.L_OP:
            content.append(token)
            types.append(html_defs.L_ELEMENT)

        elif i > 2 and ((types[-2] == html_defs.L_ELEMENT or types[-2] == html_defs.L_ATTRIBUTE_VALUE)
                or (types[-1] == html_defs.L_WHITESPACE and types[-2] == html_defs.L_ATTRIBUTE_NAME)):
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

    if (len(types) != len(content)):
        raise Exception ("There is a error in the logic here somewhere")
    if (html_defs.L_UNKOWN in types):
        raise Exception ("Unknown type in types list")

    return content, types


def process(token_lines):
    """Takes a line of tokens, returns parsed html"""
    p_lines = []
    for line in token_lines:
        p_lines.append(parse_line(line))

    return p_lines


def test():

    sample_one = ['<', 'a', ' ', 'href', '=', '"', 'https:', '/', '/', 'www.w3schools.com', '"', '>', 'Visit', ' ', 'W3Schools', '<', '/', 'a', '>']
    line = (parse_line(sample_one))
    for entry in line:
        print(entry)



def main():
    print("in main")
    test()


if __name__ == "__main__":
    main()
