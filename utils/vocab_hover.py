# vocab_hover.py
# Use: python3 vocab_hover.py path-to-input-file
# Example python3 vocab_hover.py ../testpage.rst   # i.e., testpage.rst in parent directory

# This script uses regular expressions to make all occurrences of vocab words in
# an rst file hoverable. It skips over their occurrences in the vocabulary variable
# and in the vocab table, changing only those in the narrative portion of HTML. 

# Shortcomings:  
# 1. It is currently case sensitive, so 'Word' would not match 'word'
# 2. It may make too many occurences hoverable -- e.g., in H2 or H3 headings? 

# To make a vocab word overable, the word ('Input' in this case) needs to be embedded as follows:
# <span class="hover vocab yui-wk-div" data-id="Input">Input</span>

import sys  # system lib
import re   # regular expression library
import ast  # used to parse the vocabulary variable into a python dict

DEBUG = True

# This is what the vocabulary variable looks like in a typical rst page
# We read the actual dictionary from the source file
vocabulary = { 
    "Input" : "Input  is data sent to a computer for processing by a program and can be tactile, audible, visual, or text",
    "Output" : "Output is the data sent back from the program to the device and can be tactile, audible, visual, or text.",
    "User Interface" : "The part of computer application through which a user interacts with a program.",
    "UI Components" : "Parts of the user interface such as Buttons, Labels, etc.",
    "User Events" : "Actions by the user such as button clicks.",
    "Event-driven Programming" : "In event-driven programming, the program is activated by events such as button clicks.",
    "Event Handler" : "A block of code that reacts to an event like a button click.",
    "IDE" : "An IDE is software that provides comprehensive tools for programming such as UI design, code editing, and a way to interpret and run the program."
};

# The vocab word will be surrounded by PREFIX and SUFFIX
PREFIX = "<span class=\"hover vocab yui-wk-div\" data-id='" 
SUFFIX = "</span>"

# Get the input file from the command line
if len(sys.argv) < 2:
    print('Use:  python3 vocab_hover.py input-file-path')
    print('Example:  python3 vocab_hover.py ../testpage.rst')
    exit()

# Setup output file
# Change '_rev' to '' to rewrite the input file
in_file = sys.argv[1]
out_file = in_file[0:in_file.rfind('.')] + '_rev' + in_file[in_file.rfind('.'):]

print('DEBUG Input/output files: ' + in_file + ' ' + out_file) if DEBUG else None

# The contenst of the rst file
txt = ''
with open(in_file) as file:
    txt = file.read()

# Slice up the contents into thre parts to avoid embedded words in
# the vocab variable and vocab table

# Find the vocabulary variable embedded in the page
p1 = txt.find('var vocabulary')

if p1 == -1:
    print('This file does not appear to contain a vocabulary list')
    print('Exiting')
    quit()

p2 = txt.find('};',p1)

# Find the vocab table
p3 = txt.find('<span class="hover')  

print('DEBUG slices: ' + 'p1:' + str(p1) + ' p2:' +str(p2) + ' p3:' + str(p3)) if DEBUG else None

# Our three slices. We skip the prefix and suffix
prefix = txt[0:p2+2]  # everything upto and including the vocab variable
suffix = txt[p3:]     # everything including and after the vocab table
scan_slice = txt[p2+3:p3]

# Creat the vocab dictionary 
print('DEBUG vocab dict: ' + txt[p1+17:p2+1]) if DEBUG else None
vocab = ast.literal_eval(txt[p1+17:p2+1])   # create the vocab dict
print('DEBUG python dict: ' + str(vocab)) if DEBUG else None

counter = 0

# Regular expression match function 
# Called in re.sub

# m is the pattern that was matched, containing the vocab word
# m.group(0) is the vocab word itself
# We surround it with the appropriate hover span
def repl(m):
    global counter
    counter = counter + 1
    res = PREFIX + str.strip(m.group(0)) + "'>" + str.strip(m.group(0)) + SUFFIX
    print('DEBUG ' + res) if DEBUG else None
    return res

# Replace all vocab words in the narrative (scan_slice) with appropriate hover span
for word in vocab:
    print('DEBUG ' + word) if DEBUG else None
    scan_slice = re.sub(r'\b%s+\b' % word, repl, scan_slice) 
    
print('Replaced ' + str(counter) + ' occurences')

with open(out_file, 'w', newline='\n') as file:
    file.write(prefix + scan_slice + suffix)
    print('The revised rst is in ' + out_file)
