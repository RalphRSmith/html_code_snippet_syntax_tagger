"""Module to get filename from commandline"""

from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--file",
                    help="specify html file to convert")

parser.add_option("-o", "--outfile",
                    help="specify filename for output, if no output name specified, output will go to standard out")


(cli_options, cli_args) = parser.parse_args()

if not cli_options.file:
    parser.error("please specify a file to convert with the -f or --file flag")

print(options)
print(args)
