# Adapted from
# - https://pypi.org/project/img2pdf/
# - https://stackoverflow.com/questions/4836710/is-there-a-built-in-function-for-string-natural-sort

# make a single PDF file from all images inside a directory

import os, re
import img2pdf

def natural_sort(list, key=lambda s:s):
  """
    Sort the list into natural alphanumeric order.
  """
  def get_alphanum_key_func(key):
    convert = lambda text: int(text) if text.isdigit() else text 
    return lambda s: [convert(c) for c in re.split('([0-9]+)', key(s))]
    sort_key = get_alphanum_key_func(key)
    list.sort(key=sort_key)

dirname = "./images"
imgs = []
exts = [".jpg", ".jpeg", ".png", ".webp", ".gif"]
currImg = 0

for fname in os.listdir(dirname):
  for ext in exts:
    if fname.endswith(ext):
      path = os.path.join(dirname, fname)
      if os.path.isdir(path):
        continue
      imgs.append(path)
      ## uncomment for generating individual PDFs
      # with open(fname + ".pdf", "wb") as f:
      #   f.write(img2pdf.convert(imgs[currImg]))
      # currImg += 1

natural_sort(imgs)

with open("images-merged.pdf", "wb") as f:
  f.write(img2pdf.convert(imgs))
