from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import base64
import io
import os

# Unit listed in the URL for Units 1-11 (0th index is Unit 1)
UNITS = [19, 1, 22, 23, 24, 25, 26, 127, 149, 175, 176]

# User-Defined Units
#unit_num = -1
#while(not(unit_num >= 1 and unit_num <= 11)):
#    unit_num = int(input('Enter Unit Number (1-11): '))

# Create text files with URL links for all units
for unit_num in range(1,12):
    # Source Page is unit landing page
    course_url = 'https://mobilecsp-2017.appspot.com/mobilecsp/'
    src_page = course_url + 'unit?unit=' + str(UNITS[unit_num-1])

    # Get the web page and create the soup structure
    soup = BeautifulSoup(urlopen(src_page),"html.parser")
    print(src_page)

    # For each div on the sidebar, grab the hyperlink in the anchor tag
    unit_urls = []
    div_unitURL = soup.find_all('div', {"class":"gcb-lesson-title-no-progress"})
    for div in div_unitURL:
        links = div.find_all('a')
        if(len(links) > 0):
            # add url to the list
            unit_urls.append(course_url + links[0].get('href') + '\n')

    # Write URLs to text file for scraping
    filename = 'mcsp-urls_Unit' + str(unit_num) + '.txt'
    with open(filename, "w",newline='\n') as file:
        file.write('# MobileCSP URLs for Unit ' + str(unit_num) + '\n')
        file.write(src_page + '\n')
        for url in unit_urls:
            file.write(url)
        file.close()