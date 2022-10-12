"""Module for holding all html defs and values"""

START_TAG = "<"
END_TAG = ">"

_PAIRS = {
    START_TAG : END_TAG,
    '"' : '"',
    "'" : "'",
}

_SINGLE = set(["="," ", "/"])

# HTML Safe Values for Conversion
_HTMLSAFE = {
    '<' : '&lt;',
    '>' : '&gt;',
    '&' : '&amp;',
    "'" : "'", # need to locate safe entry for single quote
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
L_UNKOWN          = "X"

OPERATORS   = set("<>/=")
WHITESPACE  = set(" ")              # add support for tab
QUOTES      = set(["'"] + ['"'])

