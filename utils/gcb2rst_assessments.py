# gcb2rst.py
# Use: python3 gcb2rst.py

# This script scrapes content from mobilecsp GCB pages and 
# converts it to Runestone format.

# The import certifi  may only be necessary for MacOS
# See: https://stackoverflow.com/questions/40684543/how-to-make-python-use-ca-certificates-from-mac-os-truststore
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import base64
import io
import os

#KLUDGE: Unknown URL not validated, just let them all come through...fixed, but for future reference
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#OUTPUT FOLDER
OUT_FOLDER = 'rst_out//'
CUR_PATH = os.path.dirname(__file__)

MOBILE_CSP_IMAGE = '.. raw:: html \n\n\t<a href="../index.html"><img class="align-center" src="../_static/MobileCSPLogo.png" width="250px"/></a>\n\n'

PORTFOLIO_TEMPATE="""<div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="###?embedded=true" style="height:30em;width:100%"></iframe></div>
"""
UNDERSCORE = "---------------------------------------------------------------------------------------------------"
EQUALS = "======================================================================================================="
COLONS = "::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"

# Used to avoid Runestone warnings about emtpy raw content
BOGUS_DIV = '\n\n.. raw:: html\n\n\t<div id="bogus-div">\n\t<p></p>\n\t</div>\n\n'

# Array for quiz questions, stored as RST strings
rst_questions = []

# Toble of Contents file names
toc = []
unit_title = ''
unit = ''

# Get Unit title -- only need to do this for one lesson
def get_unit_title(soup):
  global unit_title
  global unit
  if len(unit_title) == 0:
    hdr_tag = soup.find('div',{"class" : "gcb-assessment-contents"})


    # title is an unnamed h1 under gcb-assessment-contents div
    unit_title = hdr_tag.contents[1].text
    print("Unit Title: " + unit_title)
#    dash = unit_title.find('-')
#    unit = str.strip(unit_title[0:dash-1])
#    unit_title = str.strip(unit_title[dash+2:])

# Construct TOC as a string
def get_toc():
  toc_str = MOBILE_CSP_IMAGE
  toc_str += unit_title + '\n'
  toc_str += COLONS[:len(unit_title) + 2] + '\n\n'
  toc_str += '.. toctree::\n\t:caption: ' + unit + ' Table of Contents\n\t:maxdepth: 0\n\n'
  for page in toc:
    toc_str += '\n\t' + page
  #print('\n\n' + toc_str)
  return toc_str

# Scrape the unit and lesson number, used in Quiz labels
def get_unit_lesson(soup):
  uls = soup.find('ul', {"class":"gcb-breadcrumb"})
  lis = uls.find_all('li')
  unit= lis[1].text
  lesson = lis[2].text
  unit_lesson = unit.strip()[5:] + "-" + lesson.strip()[7:]
  return unit_lesson

# Fix the portfolio iframe
def fix_portfolio_iframe(lesson_content):
  portfolio = lesson_content.find('iframe',
{"class":"portfolioQuestions"})
  if portfolio != None:
    parent = portfolio.parent
    # Move the heading in front of the portfolio html div
    h2 = parent.find('h2')
    parent.insert_before(h2)

    portfolio_str = str(portfolio)
    p = portfolio_str.find('src=')
    pp = portfolio_str.find('/pub')
    doc = portfolio_str[p+5:pp+4]
    portfolio_new = PORTFOLIO_TEMPATE.replace('###',doc)
    portfolio_soup = BeautifulSoup(portfolio_new,"html.parser")
    portfolio.replaceWith(portfolio_soup)

#  Fix the assets links
def fix_assets_links(lesson_content):
  imgs = lesson_content.find_all('img')
  for img in imgs:
    src = img['src']
    if src.find("assets/img") == 0:
      img['src'] = '../_static/' + src
    if src.find("./assets/img") == 0:
      img['src'] = '../_static/' + src[2:]

# Converts GCB to RST encoded quiz question
# q_text is the quiz question
# data is decoded question data taken from the GCB page  
# q_type is either 'mc' or 'sa'
# label is the question number
# returns an rst-encoded representation of the question
def q_to_RST(q_text, data, q_type, label): 
    letters = ['a','b','c','d','e','f','g']
    q_data = json.loads(data)
    output_str = '\n.. '
    q_tag = 'mcsp-' + label
    if q_type == 'mc':
        output_str += 'mchoice:: ' + q_tag + '\n'
        output_str += '\t:random:\n'
        output_str += '\t:practice: T\n'
        choices = q_data['choices']
        correct = ''
        count = 0
        for y in choices:
            text = y['text']
            text = text.replace('\n',' ')
            score = y['score']
            feedback = y['feedback']
            if score > 0:
                if correct == '':
                    correct += letters[count]
                else:
                    correct += ',' + letters[count]
            output_str += '\t:answer_' + letters[count] + ': ' + text.replace('\n', ' ') + '\n'
            output_str += '\t:feedback_' + letters[count] + ': ' + feedback.replace('\n',' ') + '\n'
            count += 1
        output_str += '\t:correct: ' + correct + '\n'
        output_str += '\n\t' + q_text + '\n'
    elif q_type == 'sa':
        output_str += 'fillintheblank:: ' + q_tag + '\n'
        hint = q_data['hint']
        default_feedback = q_data['defaultFeedback']
        graders = q_data['graders']
        response = ''
        feedback = ''
        for z in graders:
             matcher = z['matcher']
             if matcher == 'case_insensitive':
                 output_str += '\t:casei:\n'
             response = z['response']
             feedback = z['feedback']
        output_str += '\n\t' + q_text + ' |blank|\n'
        output_str += '\n\t- :' + response.replace('\n',' ') + ': ' + feedback
        output_str += '\n\t  :x: ' + default_feedback.replace('\n',' ') + '\n'
    return output_str

# Replaces youtube scripts with RST code in lesson
# Doing this in pass #1 b/c it uses soup
def replace_youtubes(lesson_html):
  youtube_scripts = lesson_html.find_all('script',{"src":"/modules/core_tags/_static/js/youtube_video.js"})
  for script in youtube_scripts:
    youtube_tag = script.parent
    p1 = str(youtube_tag).find('Video(')
    p2 = str(youtube_tag).find(',',p1)
    youtube_id = str(youtube_tag)[p1+7:p2-1]
   # youtube_tag.replaceWith('\n.. youtube:: ' + youtube_id + '\n\t:width: 650\n\t:height: 415\n\t:align: center\n\n.. raw:: html\n\n')
    youtube_tag.replaceWith('\n.. youtube:: ' + youtube_id + '\n\t:width: 650\n\t:height: 415\n\t:align: center' + '###ENDYOUTUBE###')

def remove_scripts(scripts):
  for script in scripts:
    if (script.has_attr('type') and script['type'] == "text/javascript"):
      script.extract()
    if script.has_attr('src'):
      script.extract()

# Constructs new lesson structure...
#   - Introduction and Goals section at the top
#   - Learning Activities section
#   - Individual activities are h3 elements
# @param lesson_html: the gcb-lesson-content element
# @param soup: beautiful soup object
def construct_new_structure(lesson_html, soup):
  # no h2 elements --> it's an overview...abort!
  if len(lesson_html.find_all('h2')) == 0:
    return
  
  # all lesson content contained within the last element of the gcb-lesson-content
  lesson_content = lesson_html.contents[len(lesson_html)-1]
  
  # h2 elements
  sections = lesson_content.find_all('h2')
  
  # abort if no h2 elements (i.e., overview lesson page)
  if len(sections) == 0:
    return
  
  #--- Introduction and Goals section to start lesson
  if 'Introduction' in str(sections[0].string) or 'Preview' in str(sections[0].string):
    # replace with new heading
    sections[0].string = 'Introduction and Goals'
    
  else: 
    # create new h2 element for Introduction and Goals
    ig_element = soup.new_tag("h2")
    ig_element.string = "Introduction and Goals"

    # insert after Time Estimate
    lesson_content.find('h3', {'id':'est-length'}).insert_after(ig_element)
    
    #refresh h2 element list
    sections = lesson_content.find_all('h2')

  # --- Create Learning Activities sections
  # start looking for activities after Introduction and Goals section
  l = 1
  
  # lesson activities end when standard section is encountered (accounting for lessons potentially missing curious/summary)
  std_sections = ['Summary', 'Still Curious?', 'Self-Check']
  end_activities = sections[l].string in std_sections
  
  if(not end_activities):
    # add Learning Activities h2 element
    act_h2 = lesson_content.find_all('h2', string='Activities')
    if(len(act_h2) > 0):
      act_h2[0].string = 'Learning Activities'
    else:
      # create new h2 element for Learning Activities
      la_element = soup.new_tag("h2")
      la_element.string = "Learning Activities"

      # insert before the next h2 element
      sections[l].insert_before(la_element)

      #refresh h2 element list
      sections = lesson_content.find_all('h2')

    # make each activity a sub-section to Learning Activities (i.e., h3 element)
    while not end_activities and l < len(sections):
      
      # - don't other if the h2 is empty
      if(sections[l].string != None):
        # - no more activities in lesson
        if(sections[l].string in std_sections):
          end_activities = True
        
        # - don't change the Learning Activities heading we just created!
        elif(sections[l].string != 'Learning Activities'):
          
          # create new h3
          h3_element = soup.new_tag('h3')
          h3_element.string = sections[l].string

          # replace h2 with h3
          sections[l].replace_with(h3_element)

      l += 1

# Removes a couple of incomplete <link> tags
def remove_links(link):
  if link == None:
    return
  linkstr = str(link)
  p = linkstr.find('<script>')  # Find the first link
  pp = linkstr.find('</link></link></link>') 
  linkstr = linkstr[p:pp]  # Get rid of links
  linkdiv = link.parent    # Modify enclosing div
  linkdiv.attrs.clear()
  linkdiv['class'] = "MCSP-lesson-content"
  linkdiv.clear()          # Clear div's contents
  # Insert the newly constructed div 
  link_soup = BeautifulSoup(linkstr,"html.parser")
  linkdiv.insert(0,'\n')
  linkdiv.insert(1,link_soup)

# Replace GCB quizly scripts with quizly directive 
def replace_quizly_scripts(scripts):
  global question_number

  for script in scripts:
    if (str(script).find("quiz.name") != -1):
      label = 'mscp-' + unit_lesson + "-" + str(question_number+1)
      question_number = question_number + 1
      sstr = str(script)
      p = sstr.find("quiz.name")
      start = p+11
      end = sstr.find('";',start)
      q_name = sstr[start:end]
      quizly_div = script.parent
      quizly_div.clear()
      quizly_div['class'] = 'quizly'
      quizly_div['id'] = q_name
      quizly_div.insert_before('\n\r.. quizly:: ' + label + '\n\n\r\t:quizname: ' + q_name + '\n')
      quizly_div.decompose()

# Replace <h2> headings with RST
def repl(m):
  p = m.group(0).find('>') # find first >
  heading = m.group(0)[p+1:-5]
  return '\n\n' + m.group(0)[p+1:-5] + '\n' + UNDERSCORE[0:len(heading)+1] + '\n\n.. raw:: html\n\n\t<p>'

def replace_h2s(raw_html):
  pattern = '<h2[^>]*>([^<]+)</h2>'
  cleanr = re.compile(pattern, re.IGNORECASE)
  cleantext = re.sub(cleanr, repl, raw_html)
  return cleantext

# https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string       
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|\n|\t')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

# Decodes question data from hidden base64-encoded data.
# Right answer is base64 encoded (ugh)
def decode_question_data(data):
  data_str = str(data)
  i = data_str.find("atob")
  if i is not None:
    start= i+6
    end = data_str.find("));",i)
    decodedStr = str(base64.b64decode(data_str[start:end]),'utf-8')
    return decodedStr

# Operates on the soup structure
def convert_gcb2rst(quiz_questions):
  global unit_lesson
  global question_number
  for q in quiz_questions:
    decodedStr = decode_question_data(q)
    mc_question = q.find('div',{"class" : "qt-mc-question"})
    if mc_question != None:
      type = "mc"
      question = mc_question.find('div',{"class":"qt-question"})
    else:
      type = "sa"
      sa_question = q.find('div',{"class" : "qt-sa-question"})
      question = sa_question.find('div',{"class":"qt-question"})

    # if there is an image in the question text, put it in an raw:: html  
    if "<img" in str(question):
        questionstr = str(question).replace('\n',' ')
        imgStart = questionstr.find("<img")
        imgEnd = questionstr.find(">",imgStart)
        imgstr = questionstr[imgStart:imgEnd+1] 
        imgstr = imgstr.replace("PNG", "png")
        cleanquestion = cleanhtml(str(question)) + "\n\n\t.. raw:: html\n\n\t\t" + imgstr 
    else: 
        cleanquestion = cleanhtml(str(question)).replace('\n',' ')

    label = unit_lesson + "-" + str(question_number+1)

    # Replace the containing div with the rst question
    rst_q = q_to_RST(cleanquestion,decodedStr,type, label)

    # Store the question for future use
    rst_questions.append(rst_q)
    parent = q.parent
    q_soup = BeautifulSoup('<div class="rst-question"></div>',"html.parser")
#    q.parent.replaceWith(rst_q)
    q.parent.replaceWith(q_soup)  # placeholder for quiz question
    question_number = question_number + 1

# Add all the HTML content to the RST page and indent it
def convert_html_to_rst(lesson_content):
  lesson_str = (str(lesson_content))
  indented_str = ''
  for line in io.StringIO(lesson_str):
    if line.find('..') != 0:
      indented_str += '\t' + line
    elif line.find('\t') == 0:
      indented_str += line
    else:
      indented_str += line
  lesson_str = indented_str
  lesson_str = '.. raw:: html\n\n\t' + lesson_str
  return lesson_str

def scrape_and_build_rst(src_page):
  global unit_lesson
  global unit_title
  global question_number
  global rst_questions
  question_number = 0 
  rst_questions = []
  
  # Get the web page and create the soup structure
  soup = BeautifulSoup(urlopen(src_page),"html.parser")

  # Find the content section for assessments
  divs = soup.find_all('div', {"class" : "gcb-assessment-body"})
  
  if len(divs) > 0:
    lesson_content = divs[0]
  else:
    print('\n\n---- File not scrapable (skipped): ' + src_page)
    return

#----------------- PART ONE --------------------#
# Use soup to clean up the lesson_content's HTML code

  get_unit_title(soup)
#  unit_lesson = get_unit_lesson(soup)
  fix_portfolio_iframe(lesson_content)
  fix_assets_links(lesson_content)
  
  #TO DO: Remove heading images. Replaced by CSS rules
  
  # Implement new lesson structure...except in Wrap Up Lessons
  titletag = soup.find('h1', attrs={'class':'gcb-lesson-title'})
  if 'Wrap Up' not in str(titletag):
    construct_new_structure(lesson_content, soup)
  
  # Connvert the non-quizly quiz questions 
  #quiz_questions = lesson_content.find_all('div', {"class" : "gcb-border-box"})
  #convert_gcb2rst(quiz_questions)

  # Replace youtubes in soup
  replace_youtubes(lesson_content)

  # Remove unneeded scripts. Replaced by CUSTOM_SCRIPTS
  scripts = lesson_content.find_all('script')
  remove_scripts(scripts)

  # Remove unneeded malformed links. Replaced by CUSTOM_SCRIPTS
  # Soup insert </links> at end of file
  link = lesson_content.find('link')
  remove_links(link)

  # Replace quizly scripts with directives
  #scripts = lesson_content.find_all('script')
  #replace_quizly_scripts(scripts)

  # --------- PART TWO ---------------
  # Construct the RST page

  # There is no unit for an assessment...Use the unit title as the RST filename.
  assess_div = soup.find('div',{"class" : "gcb-assessment-contents"})
  
  # title is an unnamed h1 under gcb-assessment-contents div
  lesson_name = assess_div.contents[1].text.strip()
  print("Unit Title: " + unit_title)
  lesson_name =  re.sub("[^A-Za-z0-9\s]+", "", lesson_name)
  filename = re.sub("\s+", "-", lesson_name) + '.rst'
  toc.append(filename)

  # RST Page, built incrementally
  # Header image and page title
  rst_page = ""
  rst_page += MOBILE_CSP_IMAGE
  rst_page += lesson_name + '\n' + EQUALS[0:len(lesson_name)] + '\n\n'
  # Moved CUSTOM_SCRIPTS inclusion to conf.py in runestone build
  #rst_page += '.. raw:: html\n' + CUSTOM_SCRIPTS + '\n\n'

  # Indent HTML and replace H2 headings
  rst_page += convert_html_to_rst(lesson_content)
  rst_page = replace_h2s(rst_page)

  # Add in rst quizzes
#  for q in rst_questions:
#    rstq_div = '<div class="rst-question"></div>'
#    p = rst_page.find(rstq_div)
#    if p != -1:
#      rst_page = rst_page[0:p] + q + BOGUS_DIV + rst_page[p+len(rstq_div):]

  # Avoids Runestone warnings about empty raw content
  rst_page = rst_page.replace('###ENDYOUTUBE###', BOGUS_DIV)

  # Convert all tabs to 4 spaces
  rst_page = rst_page.replace('\t',' '*4)
  # Remove <br/> tags at the beginning of lines  
  clean_rst = ''
  for line in io.StringIO(rst_page):
    if line.find('<br/>') != 0: 
      clean_rst += line

  rst_page = clean_rst
      
  # The completed page
  #print(rst_page)

  # write in a file
  out_path = os.path.relpath(OUT_FOLDER+filename, CUR_PATH)
  with open(out_path, "w",newline='\n') as file: 
    file.write(rst_page)
    file.close()
  
  # add vocab hovering to RST files (Ralph's script as function)
  add_vocab_hover(out_path)
  

# --- Adding vocab hovering --- #
def add_vocab_hover(path):
    global counter
    
    # Read the contents of the input file
    txt = ''
    with open(path) as file:
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
        return
    
    # Vocab items in the table look like this. We grab both hover_id and hover_str
    # <span class="hover vocab yui-wk-div" data-id="HOVER_ID">HOVER_STR</span>
    spans = re.findall(r'<span.*hover.*</span>',vocab_table)
    hover_ids = re.findall(r'<span.*data-id="(.+)">', vocab_table)
    hover_strs = re.findall(r'<span.*hover.*>(.+)</span>', vocab_table)
    
    # Slice up the contents of the page into three parts to avoid embedded words in
    # the (commented out) vocab variable and in the vocab table
    
    # Find the (commented out) js vocabulary variable embedded in the page
    p1 = txt.find('var vocabulary')
    p2 = txt.find('};',p1)
        
    # Three slices. We skip the prefix and suffix portions of the lesson
    prefix = txt[0:p2+2]  # everything upto and including the script containing the vocab variable
    suffix = txt[p3:]     # everything including and after the vocab table
    scan_slice = txt[p2+3:p3]
    
    counter = 0 

    # Replace all vocab words in the narrative (scan_slice) with appropriate hover span
    for word in hover_ids:
        scan_slice = re.sub(r'\b%s+\b' % word, repl_vocab, scan_slice, flags=re.IGNORECASE) 
        
    print('Replaced ' + str(counter) + ' occurences')
    
    # Updated files saved to its own folder so we know which changed without losing original file name
    hover_path = os.path.relpath(OUT_FOLDER+'1_hover_out//'+path[path.rfind('/'):], CUR_PATH)
    with open(hover_path, 'w', newline='\n') as file:
        file.write(prefix + scan_slice + suffix)
        print('The revised rst is in ' + hover_path)
  
# Regular expression match function 
# Called in re.sub
# m is the pattern that was matched, containing the vocab word
# m.group(0) is the vocab word itself
# We surround it with the appropriate hover span
def repl_vocab(m):
    global counter
    
    # To make them hoverable vocab words in the narrative  will be surrounded by PREFIX and SUFFIX
    PREFIX = "<span class=\"hover vocab yui-wk-div\" data-id='" 
    SUFFIX = "</span>"
    
    counter = counter + 1
    res = PREFIX + str.strip(m.group(0)) + "'>" + str.strip(m.group(0)) + SUFFIX
    return res


# -------------------- Main Program --------------------------
#src_page = "https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=1&lesson=45"
#src_page = "https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=25&lesson=173"
#src_pages =["https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=1","https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=1&lesson=45","https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=25&lesson=173"]

# Read lesson URLs from file
urls=''
#urls_file = "mcsp-urls_Unit7.txt"
urls_file = "mcsp-urls_Assessments.txt"
#urls_file= "urlTest.txt"
with open(urls_file) as file:
  urls = file.readlines()

# Process the URLs, outputting RST files
for url in urls:
  print(url)
  if url.find('#') == -1:  # Skip comment lines
    scrape_and_build_rst(url)

# Write table of contents file
out_path = os.path.relpath(OUT_FOLDER+'toctree.rst', CUR_PATH)
with open(out_path,'w',newline='\n') as file:
  file.write(get_toc())
  file.close()
  
