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
import json

DEBUG = True

# We will extract this lesson's vocab words from the embedded vocab <table>, eg: 
'''
<table align="center">
<tbody><tr>
  <td>
    <span class="hover vocab yui-wk-div" data-id="Input">Input</span>
    <br/><span class="hover vocab yui-wk-div" data-id="Output">Output</span><br/>
    <span class="hover vocab yui-wk-div" data-id="User Interface">User Interface (UI)</span>
    <br/><span class="hover vocab yui-wk-div" data-id="UI Components">UI Components</span>
  
  </td>
  <td>

  <span class="hover vocab yui-wk-div" data-id="User Events">User Events</span>
  <br/>
    <span class="hover vocab yui-wk-div" data-id="Event-driven Programming">Event-driven Programming</span>
    <br/><span class="hover vocab yui-wk-div" data-id="Event Handler">Event Handler</span>
   <br/><span class="hover vocab yui-wk-div" data-id="IDE">Integrated Development Environment (IDE)</span>
  </td>
  </tr>
</tbody></table>
'''

# To make them hoverable vocab words in the narrative  will be surrounded by PREFIX and SUFFIX
PREFIX = "<span class=\"hover vocab yui-wk-div\" data-id='" 
SUFFIX = "</span>"

# Get the input file from the command line
if len(sys.argv) < 2:
    print('Use:  python3 vocab_hover.py input-file-path')
    print('Example:  python3 vocab_hover.py')
    exit()

# Setup output file
# Change '_rev' to '' if it's preferable to rewrite the input file
in_file = sys.argv[1]
out_file = in_file[0:in_file.rfind('.')] + '_rev' + in_file[in_file.rfind('.'):]
print('DEBUG Input/output files: ' + in_file + ' ' + out_file) if DEBUG else None

# Read the contents of the input file
txt = ''
with open(in_file) as file:
    txt = file.read()

p1 = p2 = p2 = 0   # Indexes for slicing up the lesson

# Find the vacab table, which contains the vocab words for this lesson
# We use regular expressions to create vocab list for this lesson
tables = re.findall(r'<table.*?</table>', txt, re.DOTALL)  # finds all tables, ignoring line breaks
vocab_table = ''
print(len(tables))
for t in tables:
    if re.search(r'hover',t):
        p3 = txt.find(t)  # Index of the vocab table
        print('p3 = ' + str(type(p3)))
        vocab_table = t

# Skip this lesson if no vocab table
if vocab_table == '':
    print("This lesson does not appear to have a vocab table. Exiting.")
    quit()

# Vocab items in the table look like this. We grab both hover_id and hover_str
# <span class="hover vocab yui-wk-div" data-id="HOVER_ID">HOVER_STR</span>
spans = re.findall(r'<span.*hover.*</span>',vocab_table)
hover_ids = re.findall(r'<span.*data-id="(.+)">', vocab_table)
hover_strs = re.findall(r'<span.*hover.*>(.+)</span>', vocab_table)
print('DEBUG hover_ids ' + str(hover_ids)) if DEBUG else None
print('DEBUG hover_strs ' + str(hover_strs)) if DEBUG else None

# Slice up the contents of the page into three parts to avoid embedded words in
# the (commented out) vocab variable and in the vocab table

# Find the (commented out) js vocabulary variable embedded in the page
p1 = txt.find('var vocabulary')
p2 = txt.find('};',p1)

print('DEBUG slices: ' + 'p1:' + str(p1) + ' p2:' +str(p2) + ' p3:' + str(p3)) if DEBUG else None

# Three slices. We skip the prefix and suffix portions of the lesson
prefix = txt[0:p2+2]  # everything upto and including the script containing the vocab variable
suffix = txt[p3:]     # everything including and after the vocab table
scan_slice = txt[p2+3:p3]

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
for word in hover_ids:
    print('DEBUG ' + word) if DEBUG else None
#    finds = re.findall(r'\b%s+\b' % word, scan_slice, flags=re.IGNORECASE) 
    finds = re.findall(r'\b%s+\b' % word, scan_slice) 
#    print(finds)
    scan_slice = re.sub(r'\b%s+\b' % word, repl, scan_slice, flags=re.IGNORECASE) 
    
print('Replaced ' + str(counter) + ' occurences')

with open(out_file, 'w', newline='\n') as file:
    file.write(prefix + scan_slice + suffix)
    print('The revised rst is in ' + out_file)
