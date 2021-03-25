# gcb2rst.py
# Use: python3 gcb2rst.py

# This script scrapes content from mobilecsp GCB pages and 
# converts it to Runestone format.

# The import certifi  may only be necessary for MacOS
# See: https://stackoverflow.com/questions/40684543/how-to-make-python-use-ca-certificates-from-mac-os-truststore
import certifi  # Needed for MacOS
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import base64
import io
import html

MOBILE_CSP_IMAGE = '.. image:: ../../_static/MobileCSPLogo.png\n\t:width: 250\n\t:align: center\n\n'

CUSTOM_SCRIPTS = """\n\t<!-- Custom Scripts -->\n\t<script src="../_static/assets/lib/lessons/tipped.js" type="text/javascript"></script>\n\t<script src="../_static/assets/lib/lessons/Framework2020.js" type="text/javascript"></script>\n\t<link href="../_static/assets/lib/lessons/tipped.css" rel="stylesheet" type="text/css"></link>\n\t<link href="../_static/assets/lib/lessons/lessons.css" rel="stylesheet" type="text/css"></link>\n\t<link href="../_static/assets/css/custom.css" rel="stylesheet" type="test/css"></link>\n\t<script src="../_static/assets/lib/lessons/vocabulary.js" type="text/javascript"></script>\n\t<style>    td { text-align: left; padding: 5px;}</style>\n"""

QUIZLY_TEMPLATE = """<div><div style="border: 1px solid black; margin: 5px; padding: 5px;"><iframe height="595" src="../_static/assets/lib/quizly/index.html?backpack=hidden&amp;selector=hidden&amp;quizname=###&amp;hints=true&amp;repeatable=false" style="border: 0px; margin: 1px; padding: 1px;" width="100%"></iframe></div><div style="text-align:center;">Quizly Activity:### (@@@)</div><hr style="background-color:#505050; height:5px;border:none;"></hr></div>
"""
PORTFOLIO_TEMPATE="""<div style="align-items:center;"><iframe class="portfolioQuestions" scrolling="yes" src="###?embedded=true" style="height:30em;width:100%"></iframe></div>
"""
UNDERSCORE = "---------------------------------------------------------------------------------------------------"
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
    hdr_tag = soup.find('h1',{"class" : "gcb-unit-header"})
    unit_title = hdr_tag.text
    dash = unit_title.find('-')
    unit = str.strip(unit_title[0:dash-1])
    unit_title = str.strip(unit_title[dash+2:])

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
    q_tag = 'repl-mcsp-' + label
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
        output_str += '\n\t' + q_text.replace('\n',' ') + '\n'
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
        output_str += '\n\t' + q_text.replace('\n',' ') + ' |blank|\n'
        output_str += '\n\t- :' + response.replace('\n',' ') + ': ' + feedback
        output_str += '\n\t  :x: ' + default_feedback.replace('\n',' ') + '\n'
    return output_str

# Replaces youtube scripts with RST code in lesson
# Doing this in pass #1 b/c it uses soup
def replace_youtubes(lesson_html):
  #print(".....Finding youtubes......")
  youtube_scripts = lesson_html.find_all('script',{"src":"/modules/core_tags/_static/js/youtube_video.js"})
  for script in youtube_scripts:
    youtube_tag = script.parent
    #print(str(youtube_tag))
    p1 = str(youtube_tag).find('Video(')
    p2 = str(youtube_tag).find(',',p1)
    youtube_id = str(youtube_tag)[p1+7:p2-1]
    #print('youtube id = ' + youtube_id)
    youtube_tag.replaceWith('\n.. youtube:: ' + youtube_id + '\n\t:width: 650\n\t:height: 415\n\t:align: center\n\n.. raw:: html\n\n')

def remove_scripts(scripts):
  for script in scripts:
    if (script.has_attr('type') and script['type'] == "text/javascript"):
      script.extract()
    if script.has_attr('src'):
      script.extract()

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

# Replace GCB quizly scripts with QUIZLY_TEMPLATE
def replace_quizly_scripts(scripts):
  global question_number

  for script in scripts:
    if (str(script).find("quiz.name") != -1):
      label = 'repl-mscp-' + unit_lesson + "-" + str(question_number+1)
      question_number = question_number + 1
      sstr = str(script)
      p = sstr.find("quiz.name")
      start = p+11
      end = sstr.find('";',start)
      q_name = sstr[start:end]
      quizly_code = QUIZLY_TEMPLATE.replace("###", q_name)
      quizly_code = quizly_code.replace("@@@",label)
      quizly_code += '\n\t'
      quizly_div = script.parent
      quizly_div.clear()
      quizly_div['class'] = 'quizly'
      quizly_soup = BeautifulSoup(quizly_code,'html.parser')
      quizly_div.insert(0,'\n')
      quizly_div.insert(1,quizly_soup)
      quizly_div.insert_before('\n\r.. raw:: html\n\n')

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
    cleanquestion = cleanhtml(str(question))
#    cleanquestion = cleanhtml(question.prettify(formatter=None))
    #print(str(cleanquestion) + "\n")
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
  global question_number
  global rst_questions
  question_number = 0 
  rst_questions = []
  
  # Get the web page and create the soup structure
  soup = BeautifulSoup(urlopen(src_page),"html.parser")

  # Find the content section
  divs = soup.find_all('div', {"class" : "gcb-lesson-content"})
  if len(divs) > 0:
    lesson_content = divs[0]
  else:
    print('\n\n---- File not scrapable (skipped): ' + src_page)
    return

#----------------- PART ONE --------------------#
# Use soup to clean up the lesson_content's HTML code

  get_unit_title(soup)
  unit_lesson = get_unit_lesson(soup)
  fix_portfolio_iframe(lesson_content)
  fix_assets_links(lesson_content)
  
  # Connvert the non-quizly quiz questions 
  quiz_questions = lesson_content.find_all('div', {"class" : "gcb-border-box"})
  convert_gcb2rst(quiz_questions)

  # Replace youtubes in soup
  replace_youtubes(lesson_content)

  # Remove unneeded scripts. Replaced by CUSTOM_SCRIPTS
  scripts = lesson_content.find_all('script')
  remove_scripts(scripts)

  # Remove unneeded malformed links. Replaced by CUSTOM_SCRIPTS
  # Soup insert </links> at end of file
  link = lesson_content.find('link')
  remove_links(link)

  # Replace quizly scripts
  scripts = lesson_content.find_all('script')
  replace_quizly_scripts(scripts)

  # --------- PART TWO ---------------
  # Construct the RST page

  # Use the page title as the RST filename
  titletag = soup.find('h1', attrs={'class':'gcb-lesson-title'})
  lesson_name = titletag.text.strip()
  filename = re.sub("\s", "-", lesson_name) + '.rst'
  toc.append(filename)

  # RST Page, built incrementally
  # Header image and page title
  rst_page = ""
  rst_page += MOBILE_CSP_IMAGE
  rst_page += lesson_name + '\n' + UNDERSCORE[0:len(lesson_name)] + '\n\n'
  rst_page += '.. raw:: html\n' + CUSTOM_SCRIPTS + '\n\n'

  # Indent HTML and replace H2 headings
  rst_page += convert_html_to_rst(lesson_content)
  rst_page = replace_h2s(rst_page)

  # Add in rst quizzes
  for q in rst_questions:
    rstq_div = '<div class="rst-question"></div>'
    p = rst_page.find(rstq_div)
    if p != -1:
      rst_page = rst_page[0:p] + q + BOGUS_DIV + rst_page[p+len(rstq_div):]

  # Avoids Runestone warnings about empty raw content
#  rst_page = rst_page.replace('###YOUTUBE###', BOGUS_DIV)

  # Convert all tabs to 4 spaces
  rst_page = rst_page.replace('\t',' '*4)
  # Remove <br/> tags at the beginning of lines  
  clean_rst = ''
  for line in io.StringIO(rst_page):
    if line.find('<br/>') != 0: 
      clean_rst += line

  rst_page = clean_rst
      
  # The completed page
  print(rst_page)

  # write in a file
  with open(filename, "w",newline='\n') as file: 
    file.write(rst_page)
    file.close()

# -------------------- Main Program --------------------------
#src_page = "https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=1&lesson=45"
#src_page = "https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=25&lesson=173"
#src_pages =["https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=1","https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=1&lesson=45","https://mobilecsp-2017.appspot.com/mobilecsp/unit?unit=25&lesson=173"]

# Read lesson URLs from file
urls=''
urls_file = "mcsp-urls.txt"
with open(urls_file) as file:
  urls = file.readlines()

# Process the URLs, outputting RST files
for url in urls:
  if url.find('#') == -1:  # Skip comment lines
    scrape_and_build_rst(url)

# Write table of contents file
with open('toctree.rst','w',newline='\n') as file:
  file.write(get_toc())
  file.close()




