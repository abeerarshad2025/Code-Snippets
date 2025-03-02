import argparse
import os.path

import lxml.html as lh    # https://lxml.de/installation.html
from lxml.etree import tostring

credits_name = 'add-favicons-to-html-url-list.py'
credits_url  = 'https://github.com/abeerarshad2025/Code-Snippets/tree/main/Python/add%20favicons%20to%20url%20links'
credits_html = '<p style="background-color: #DDB1B7; color: #981427; padding: 4px;">Generated by <a href="' + credits_url + '" target="_blank"' + '">' + credits_name + '</a></p>\n'

links = []
counter_styling = "vertical-align:middle; line-height: 1.8; font-family: Arial, Helvetica, sans-serif; font-size: 11px; color: grey;";
img_styling  = "vertical-align:middle;"
link_styling = "vertical-align:middle; line-height: 1.8; font-family: Arial, Helvetica, sans-serif; font-size: 13px; color: blue; text-decoration: none;";
nbsp = "&nbsp;&nbsp;"

parser = argparse.ArgumentParser("add-favicons-to-url-links")
parser.add_argument("linksfile", help="The file containing your list of HTML hyperlinks.", type=str)
args = parser.parse_args()

file_name = args.linksfile

# read html file
html_file = open(file_name, 'r', encoding="utf8")
contents = html_file.read()

# open new html file for writing
html_file_basename = os.path.splitext(os.path.basename(file_name))[0];
html_file_new_suffix = ' _favicons.html'
file_name_title_html = '<h1 style="text-align: center;">' + html_file_basename + "</h1>";

html_file_new = open(html_file_basename + html_file_new_suffix, 'w', encoding="utf8")
html_file_new.write(credits_html)
html_file_new.write(file_name_title_html)

counter = 0

doc = lh.fromstring(contents)
for a in doc.xpath('//a'):
  counter += 1
  href = a.attrib['href']
  html_file_new.write('<span style="' + counter_styling + '">' + str(counter) + '</span>' + nbsp)
  if href.startswith('http'):
    html_file_new.write('<img src="' + 'http://www.google.com/s2/favicons?domain=' + href + '" style="' + img_styling + '">' + nbsp)
  html_file_new.write('<a href="' + href + '" target="_blank" style="' + link_styling + '">' + a.text_content() + '</a>' + '<br>\n')

html_file_new.close()
html_file.close()

print(args.linksfile + ' favicons generated')
