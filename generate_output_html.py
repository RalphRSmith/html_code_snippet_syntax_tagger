"""A module to generate the output html"""

import html_defs

def label(substring : str, type : str):
    """ Wraps the substring in an html span of class <type>"""
    return f"<span class='{type}'>{substring}</span>"


def get_safe_html_char(token):
    """Returns a safe dict"""
    if token in html_defs.HTMLSAFE:
        return html_defs.HTMLSAFE[token]
    else:
        return token


def cleanse_and_style_tag(parsed_tokens):
    """Takes a list of parsed token named tuples and returns a list of line strings"""
    cleansed = [f"<pre><code>"]

    for tok in parsed_tokens:
        if html_defs.NEWLINE in tok.token:
            parts = tok.token.split(html_defs.NEWLINE)
            labeled = [label(x, tok.token_type) for x in parts]
            cleansed.append("\n".join(labeled))
        else:
            cleansed.append(label(get_safe_html_char(tok.token), tok.token_type))

    cleansed.append("</code></pre>")
    return "".join(cleansed)


def fix_newlines(parsed_tokens):
    """ fixes newlines """
    for i, entry in enumerate(parsed_tokens):
        if html_defs.NEWLINE in entry.token:
            print(i, entry.token.split(html_defs.NEWLINE))

    return parsed_tokens


def generate(parsed_tokens):
    return cleanse_and_style_tag(parsed_tokens)



def main():
    run_tests()


def run_tests():
    """ Test Runner """

    PASSED = "passed"
    FAILED = "*** failed ***"

    # define tests
    def test_one():
        """check that label works correctly"""
        sub1 = "abcd"
        type1 = "Q"

        try:
            v1 = label(sub1, type1)
            assert (v1 == f"<span class='{type1}'>{sub1}</span>")
            print(PASSED)
        except assertionError:
            print(FAILED)


    def test_two():
        """check if chars are properly escaped"""
        try:
            T = html_defs.START_TAG
            assert(get_safe_html_char(T) == html_defs.HTMLSAFE[T]) # must be escaped
            assert(get_safe_html_char("s") == "s")                  # s char - no need to escape
            print(PASSED)
        except assertionError:
            print(FAILED)


    # invoke tests
    print("Running tests")
    print("-" * 13)
    tests = [test_one, test_two]
    for test in tests:
        print(f"{test.__name__}: ", end="")
        test()



if __name__ == "__main__":
    main()
