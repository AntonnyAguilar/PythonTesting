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

def ran_bool(num,low,high):
  # def ran_bool(num,low,high): return num in range(low,high)
   if num >= low and num<=high:
  # if num in range(low,high):
    return True
  else:
    return False

def volu(rad):
  return (4.0/3)*3.14*(rad**3)