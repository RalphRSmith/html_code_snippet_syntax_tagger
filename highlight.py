'''A module to generate display code for my website'''
import d_stack
DEBUG = True


_PAIRS = {
    '<' : '>',
    '"' : '"',
}

_SINGLE = set(["="," "])


_HTMLSAFE = {
    '<' : "&lt",
    '>' : "&gt",
}

code_filename="html_to_convert2.html"
lines = list()

with open(code_filename, "r") as f:
    l = f.readline()
    while l:
        lines.append(l.rstrip())
        l = f.readline()

out_text = []
for i, line in enumerate(lines):
    out_line = list()
    tokens = d_stack.D_Stack()
    matched_command=d_stack.D_Stack()
    working = ""
    for j, c in enumerate(line):
        if c == matched_command.top():
            out_line.append(working)
            out_line.append(c)
            matched_command.pop()
            working = ""
        elif c in _SINGLE or c in _PAIRS.keys():
            if working:
                out_line.append(working)
            working = ""
            out_line.append(c)

            if c in _PAIRS.keys():
                matched_command.push(_PAIRS[c])
        else:
            working += c

        if DEBUG:
            print(f"line iteration {i} and char iteration {j} current char {c}")
            print(f"outline {out_line}")
            print(f"tokens {tokens}")
            print(f"matched_command {matched_command}")
            print(F"working {working}")
            print()

    out_text.append(out_line)

print(f"out_text: {out_text[0]}")
print(F"joined: {''.join(out_text[0])}")
