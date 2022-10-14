# HTML Code Snippet Syntax Tagger

Generates formatted code snippets with class tags to simplify CSS styling.

Date: Oct 13, 2022

Author: [Ralph Smith](https://github.com/RalphRSmith)

## About

The program does three things:
1. All start ("\<") and end ("\>") tags from the input HTML file are escaped.
2. Each code token gets wrapped in a \<span> with the class of its type
3. The returned code is wrapped in a \<pre>\<code> block

The program can output to a file or standard out.

## Load requirements

First load the required packages
```
pip install -r requirements.txt
```

## Usage

Run the program **main.py** from the command line and specify the file to be processed with the -f flag.  The file should have a .html or .txt extension.

```
python main.py -f <filename>
```
|flag|behaviour| if flag is missing |
|---|---|---|
| -f filename | Specify the HTML file to be processed | Program will throw an error |
| -o out_filename  | Specify name for output file.  If the file exists it will be overwritten | Program will direct output to std.out  |

To output the results to a file, use:
```
python main.py -f <filename> -o <out_filename>
```

### Example

Below is the starting raw html
```
<a href="ralphrandallsmith.com">link</a>
```

Below is the program output.  Notice the \<span\> and class selectors added

```
<pre><code><span class='o'>&lt;</span><span class='e'>a</span><span class='w'> </span><span class='an'>href</span><span class='o'>=</span><span class='av'>"ralphrandallsmith.com"</span><span class='o'>&gt;</span><span class='t'>link</span><span class='o'>&lt;</span><span class='o'>/</span><span class='e'>a</span><span class='o'>&gt;</span></code></pre>
```


# Some Implementation Details

The program has some similarities to a compiler.

The basic steps are:

1. Lexical Analysis (converts raw html code to tokens)
    - read the input characters and produce as output a sequence of tokens

2. Syntax Anylizer
    - categorizes tokens

3. Outputs html with each token type wrapped in it's own span with class token type

|language token type | coresponding labeled css class|
|---|---|
|Operator|o|
|Element | e |
|Attribute Name | an |
|Attribute Value | av |
|Comment | c |
|text | t|
|Whitespace | w |
|Newline | n |


## Known Issues

1) If a comment has a ">" in its text body, the program will throw an error.  The code below will throw an error.
```
<-- This is a line comment <  -->
```


## Links

WHATWG HTML Living Standard: https://html.spec.whatwg.org/multipage/
