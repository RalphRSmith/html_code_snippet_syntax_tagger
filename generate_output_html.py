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


def cleanse_and_style_tag(parsed_token_lines):
    """Takes a list of parsed token named tuples and returns a list of line strings"""
    cleansed = [f"<pre><code>"]

    for line in parsed_token_lines:
        cleansed_line = []
        for entry in line:
            cleansed_line.append(label(get_safe_html_char(entry.token), entry.token_type))
        cleansed_line.append(html_defs.NEWLINE)
        cleansed.append("".join(cleansed_line))
    cleansed.append("</code></pre>")
    return "".join(cleansed)




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
