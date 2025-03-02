words = []

# open JS file for writing
file_js = open('words.js', 'w')

# read words file and transform all words into a JS array string
file_txt = open('words.txt', 'r')
words = file_txt.readlines()

file_js.write("words = [\n")
count = 0
for w in words:
  count += 1
  file_js.write('  "' + w.strip() + '", \n')

file_js.write("];\n")

file_txt.close()
file_js.close()
