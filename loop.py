l = [1,2,3,4,5]

for element in l:
  print element

for num in l:
  if num%2==0:
    print 'even number: %s' %(num)
  else
    print 'Odd even number: %s' %(num)

list_num=0

for num in l:
  list_num = list_num + num

print list_num

tup = (1,2,3,4,5)
l = [(2,4), (6,8), (10,12)]

for (t1,t2) in l:
  print t1

d = {'k1':1,'k2':2, 'k3':3}

for k,v in d.iteritems():
  print 'key: %s' %(k)
  print 'value: %s' %(v)