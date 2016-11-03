# Use https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions

# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.


import requests
import re
from bs4 import BeautifulSoup

print
print (" - ....working......")
print


base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
# print (soup)

# for student in soup.findall('student'):
# 	print (student.get('alt', 'No!!'))

findstudent = soup.find_all(text = re.compile('student'))
empty = []
for word in findstudent:
    fixed_text = str(word).replace('student', '“AMAZING student')
    word.replace_with(fixed_text)
    empty.append(fixed_text)

print(empty)