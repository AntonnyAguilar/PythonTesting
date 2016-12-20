'''
  break
  continue
  pass
'''

def sum_val(arg1, arg2):
  '''
  Here is the information related to the function
  '''
  # print arg1+arg2
  return arg1+arg2
x=sum_val(2,3)

def say_hello():
  print 'Hello'

def greeting(name):
  print 'Hello '+ name

def is_prime(num):
  '''
  Check  if a number is prime or not
  '''
  for n in range(2,num):
    if num % n ==0:
      print 'Not Prime'
      break
  else:
    print 'Prime'