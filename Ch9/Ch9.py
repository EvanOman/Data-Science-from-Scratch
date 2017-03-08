# Chapter 6: Getting Data

# NOTE: This file is more for archival use, not meant to be run

# Read in lines of text and spits out lines which match a regex

##  egrep.py  ##
import sys, re

# sys.argv is te list of command line arguments
# sys.argv[0] is the name of the program itself
# sys.argv[1] will be the regex specified at the command line
regex = sys.argv[1]

# for every line passed into the script
for line in sys.stdin:
    # if it matches the regez, write it to stdout
    if re.search(regex, line):
        sys.stdout.write(line)



##  line_count.py  ##
import sys

count = 0
for line in sys.stdin:
    count += 1

# print goes to sys.stdout
print(count)



##  most_common_words.py  ##
import sys
from collections import Counter

# pass in the number of words as first argument
try:
    num_words = int(sys.argv[1])
except:
    print("usage: most_common_words.py num_words")
    sys.exit(1) # non-zero exit code indicates error

couter = Counter(word.lower()                       # lowercase words
                 for line in sys.stdin              #
                 for word in line.strip().split()   # split on space
                 if word)                           # skip empty 'words'

for word, count in cunter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")


# sample usage: $ cat the_bible.txt | python most_common_words.py 10
# 64193     the
# 51380     and
# 34753     of
# 13643     to
# 12799     that
# 12560     in
# 10263     he
# 9840      shall
# 8987      unto
# 8836      for



# O'Reilly Website Scraping

from bs4 import BeautifulSoup

url = "http://shop.oreilly.com/category/browse-subjects/" + \
"data.do?sortby=publicationDate&page=1"
soup = BeautifulSoup(requests.get(url).text, 'html5lib')


tds = soup('td', 'thumbtext')
print(len(tds)) # 30


# Only want books
def is_video(td):
    """it's a video if it has exactly one pricelabel, and if
       the stripped text inside that pricelabel starts with 'Video'"""
    pricelabels = td('span', 'pricelabel')
    return  (len(pricelabels) == 1 and pricelabels[0].text.strip().startswith("Video"))

print(len([td for td in tds if not is_video(td)]))
# 21ish, depends on the new books added


def book_info(td):
    # Book titke is inside the <a> tag inside the <div class="thumbheader">
    title = td.find("div", "thumbheader").a.text

    # the authors are in the text of the AuthorName <div>. They are preface by a "By" and
    # separated by commas
    author_name = td.find('div', 'AuthorName').text
    authors = [x.strip() for x in re.sub("^By ", "", author_name).split(",")]

    # the ISBN is contained in the link thatin the thumbheader <div>
    isbn_link = td.find("div", "thumbheader").a.get("href")

    # re.match captures the part of the regex in parentheses
    isbn = re.match("/product/(.*)\.do", isbn_link).group(1)

    # Date is the contents of the <span class="directorydate">
    date = td.find("span", "directorydate").text.strip()

    return {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "date": date
    }


# Now we can use this to scrape all the pages
from bs4 import BeautifulSoup
import requests
from time import sleep
base_url =  "http://shop.oreilly.com/category/browse-subjects/" + \
"data.do?sortby=publicationDate&page="

books = []

NUM_PAGES = 31 # At the time of writing

for page_num in range(1, NUM_PAGES + 1):
    print("souping page", page_num,", ", len(books), " found so far")
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')

    for td in soup('td', 'thumbtext'):
        if not is_video(td):
            books.append(book_info(td))

    # now we need to respect the website's robots.txt
    sleep(30)

# Now we can plot the data
def get_year(book):
    return int(book["date".split()[1]])

# up to 2015
year_counts = Counter(get_year(book) for book in books if get_year(book) <= 2015)

import matplotlib.pyplot as plt
years = sorted(year_counts)
book_counts = [year_counts[year] for year in years]
plt.plot(years, book_counts)
plt.ylabel("# of data books")
plt.title("Date is Big!")
plt.show()

