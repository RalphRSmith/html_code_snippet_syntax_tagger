"""A module to generate the output html"""

from typing import List
import html_defs
import parse

def label(substring : str, substring_type : str):
    """ Wraps the substring in an html span of class <type>"""
    return f"<span class='{substring_type}'>{substring}</span>"


def get_safe_html_char(token : str) -> str:
    """Returns a safe dict"""
    if html_defs.should_escape(token):
        return html_defs.escape(token)
    return token


def generate(parsed_tokens : List[parse.ParsedToken]) -> str:
    """Takes a list of parsed token named returns sanitized and labeled html"""
    tok:    parse.ParsedToken
    token:  str
    t_type: str

    cleansed = ["<pre><code>"]

    for tok in parsed_tokens:
        if html_defs.NEWLINE in tok.token:
            parts = tok.token.split(html_defs.NEWLINE)
            labeled = [label(x, tok.token_type) for x in parts]
            cleansed.append("\n".join(labeled))
        else:
            token, t_type = tok.token, tok.token_type

            to_check = [html_defs.START_TAG, html_defs.END_TAG]
            for tag in to_check:
                if tag in token:
                    token = token.replace(tag, html_defs.escape(tag))

            cleansed.append(label(get_safe_html_char(token), t_type))

    cleansed.append("</code></pre>")
    return "".join(cleansed)


def main():
    """ Invoked when module is run """
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
            test_label = label(sub1, type1)
            assert test_label == f"<span class='{type1}'>{sub1}</span>"
            print(PASSED)
        except AssertionError:
            print(FAILED)


    def test_two():
        """check if chars are properly escaped"""
        try:
            start = html_defs.START_TAG
            assert get_safe_html_char(start) == html_defs.escape(start)  # must be escaped
            assert get_safe_html_char("s") == "s"                  # s char - no need to escape
            print(PASSED)
        except AssertionError:
            print(FAILED)


    # invoke tests
    print(f"\nRunning {__file__} tests")
    print("-" * (14 + len(__file__)))
    tests = [test_one, test_two]
    for test in tests:
        print(f"{test.__name__}: ", end="")
        test()


if __name__ == "__main__":
    main()
