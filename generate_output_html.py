"""A module to generate the output html"""

def label(substring : str, type : str):
    """ Wraps the substring in an html span of class <type>"""
    return f"<span class='{type}'>{substring}</span>"


def get_safe_html_char(token):
    """Returns a safe dict"""
    if token in html_defs._HTMLSAFE:
        return html_defs._HTMLSAFE[token]
    else:
        return token


