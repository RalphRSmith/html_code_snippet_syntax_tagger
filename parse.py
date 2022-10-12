"""Module for parsing html tags

input:  assumes valid html tag, starting with "<" and ending with ">"
"""
import html_defs

def is_operator(token):
    return token in html_defs.OPERATORS

def is_whitespace(token):
    return token in html_defs.WHITESPACE


def parse_line(token_line):
    info = []
    tag = []
    in_tag = False
    for token in token_line:
        if token == html_defs.START_TAG:
            if tag:
                info.append(tag)
                tag = []
            tag.append(token)
            in_tag = True
        elif token == html_defs.END_TAG:
            tag.append(token)
            info.append(parse_tag_list(tag))
            in_tag = False
        else:
            tag.append(token)
    return info


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
            while tag_token[i] != end:
                collapsed_attribute_name.append(tag_token[i])
                i += 1

            collapsed_attribute_name.append(end)
            content.append("".join(collapsed_attribute_name))
            types.append(html_defs.L_ATTRIBUTE_VALUE)

        else:
            types.append(html_defs.L_UNKOWN)

        i += 1


    print(f"content {content}")
    print(f"types {types}")

    if (len(types) != len(content)):
        raise Exception ("There is a error in the logic here somewhere")
    if (html_defs.L_UNKOWN in types):
        raise Exception ("Unknown type in types list")

    return types



def test():

    sample_one = ['<', 'a', ' ', 'href', '=', '"', 'https:', '/', '/', 'www.w3schools.com', '"', '>', 'Visit', ' ', 'W3Schools', '<', '/', 'a', '>']
    print(sample_one)
    parse_line(sample_one)



def main():
    print("in main")
    test()


if __name__ == "__main__":
    main()
