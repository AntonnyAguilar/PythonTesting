# list = array

my_list = [40,148,'asdas',2,5]
len(my_list)

narray = ['one', 'two', 3,4 ,5]

'''
narray[n] --> element in the n position
narray[n:m] --> element desde la pos n hasta la pos m
narray[n:] --> element desde la pos n hasta el final
narray[:n] --> element desde el inicio hasta la pos n
narray*2
narray+narray

'''
l = [1,2]
l.append(5) # --> [1,2,5]
l.count() # 3
l.pop() # l.pop(n); get the element on the n position (last element by default) and deleted from the list

new_list = ['x','g','h','a','f']
new_list.reverse() # [f,a,h,g,x]
new_list.sort() # [a,f,g,h,x]

matrix = [my_list, narray, l, new_list]

matrix[0] # my_list
matrix[0][0] # my_list[0] --> 40

first_col = [row[0] for row in matrix] #  first_col --> [40,'one',1,'f']

x=2
list(x) # parse x to a list