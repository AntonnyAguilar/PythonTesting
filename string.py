# '' or ""
'''
\n --> salto de linea
\t --> tabular

from __future__ import print_function
python 3:
print 'Hello world' --> print('Hello world')
'''

len('Hello World')
s = 'Hello World'
s[0] # s[n] --> letra en la pos n
s[0:4] # s[n:m] --> letras desde la pos n hasta la pos m
s[0:] # s[n:] --> letras desde la pos n hasta el final
s[:3] # s[:n] --> letras desde el inicio hasta la pos n
s[-1] # last letter
s[:-1] # s[:-n] --> letras desde el inicio hasta 
s[::1] # s[::n] --> letras desde el inicio pero cada n espacios
s[::-1] # s[::n] --> reverse string

a = "l"
'''
a*3 --> "lll"
a+a --> "ll"
'''

s.upper() # uppercase all string
s.lower() # lowercase all string
s.split('n') # list, split the string into an array on each n letter found