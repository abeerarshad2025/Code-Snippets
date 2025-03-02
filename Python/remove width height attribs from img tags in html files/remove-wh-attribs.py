import os
import lxml.html as lh    # https://lxml.de/installation.html

for file in os.listdir():
  if file.endswith(".html"):
    file_path = file
    print(file_path)
    with open(file_path, 'r') as f:
      html = f.read()
      if (html):
        doc = lh.fromstring(html)
        for img in doc.xpath('//img'):
          img.attrib.pop('width', None)
          img.attrib.pop('height', None)
          outFile = open(os.path.splitext(os.path.basename(file_path))[0] + '_modified.html', 'wb')
          print(lh.tostring(doc))
          outFile.write(lh.tostring(doc))
