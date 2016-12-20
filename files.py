f = open('test')
f.read() # read the file
f.seek(0) # goes to the first letter of the file
f.readlines() # show the text of the file

''' in jupyter

%%writefile new.txt
first line
second line

'''

for line in open('test'):
  print line