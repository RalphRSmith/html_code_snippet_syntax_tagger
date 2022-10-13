"""Module to get filename from commandline"""

import argparse
import os.path

parser = argparse.ArgumentParser(
        prog="main.py",
        description="generate styled html code-block from raw html",
        usage="%(prog)s [option] path")

parser.add_argument('-f', "--file",
                    type=str,
                    help="specify filename of raw-html")

parser.add_argument('-o', "--outfile",
                    type=str,
                    help="specify output filename, if none specified, output goes to std out")

args = parser.parse_args()

# validate infile arguments
if not args.file:
    parser.error("raw-html filename missing.  Usage: python main.py -f <filename>")

f_name, f_extension = os.path.splitext(args.file)

if not os.path.exists(args.file):
    parser.error("input filename cannot be found")

if f_extension not in [".html", ".txt"]:
    parser.error("please pass a .html or .txt files")


print("made past checks")
print(args)
