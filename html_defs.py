"""Module for holding all html defs and values"""

# Important Constants
START_TAG = "<"
END_TAG = ">"
NEWLINE = "\n"


# Operators
BINARY_PAIRS = {
    START_TAG : END_TAG,
    '"' : '"',
    "'" : "'",
}

SINGLE = set(["="," ", "/"])


# HTML Safe Values for Conversion
HTMLSAFE = {
    START_TAG : '&lt;',
    END_TAG : '&gt;',
    '&' : '&amp;',
    "'" : "&#34",
    '"' : '&quot;',
}

# Type Class Labels
L_OP              = "o"
L_ELEMENT         = "e"
L_ATTRIBUTE_NAME  = "an"
L_ATTRIBUTE_VALUE = "av"
L_COMMENT         = "c"
L_TEXT            = "t"
L_WHITESPACE      = "w"
L_NEWLINE         = "n"
L_UNKOWN          = "X"

# Some sets used for matching
OPERATORS   = set("<>/=")
WHITESPACE  = set("     ")              # add support for tab
QUOTES      = set(["'"] + ['"'])
COMMENT_START = "!--"                   # after a start_tag


# Functions
def in_binary_pair_keys(char : str) -> bool:
    """ Returns true if char is in binary operator pairs datastructure"""
    return char in BINARY_PAIRS

def is_binary_key_or_single(char : str) -> bool:
    """ Returns true if c (char) is in binary operator pairs or single datastructure"""
    return (char in SINGLE or in_binary_pair_keys(char))

def get_binary_complement(char : str) -> str:
    """ Returns the value of the char key in the BINARY PAIRS datastructure"""
    return BINARY_PAIRS[char]

def should_escape(token : str) -> bool:
    """returns true if the token should be escaped"""
    return token in HTMLSAFE

def escape(char : str) -> str:
    """ escapes the current char with an html safe value"""
    return HTMLSAFE[char]
