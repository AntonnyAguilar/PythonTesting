'''
range(n,m,o) --> only integers, is a list
  n: initial number
  m: up to number, m not including
  o: step - optional
range(m) --> from 0 to m-1
'''

x = range(0,10)
type(x) # type of variable

start = 0
stop = 20
range(start,stop,2)

# xrange(1,10) --> generation of range but is not loaded in memory

l = [1,2,3,4,5]

for num in xrange(1,6):
  print num