'''
list comprehension, iterate the string or range and convert it on a list
var = ["statement" for "x" in "thing" "condition (optional)"]
'''

lst = [x for x in 'hello']
l = [x for x in range(1,10)]
lstif = [num for num in range(11) if num%2==0]

celsius = [0,10,20.1,34.5]

fahre = [(temp*9/5.0)+32 for temp in celsius]

lst2 = [x**2 for x in [x**2 for x in range(11)]]