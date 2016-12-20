# dictionary = hash{key:value}

my_dict = {'key1':'value1','key2':'value2'}
my_dict['key2'] # 'value2'

my_dict = {'k1':123,'k2':4.666,'k3':'value'}

'''

my_dict['k3'] --> if values is a string it could be use all the string methods
my_dict['k1'] --> if values is a int/float it could be use all the int/float methods
my_dict['k1']+= 120 --> 243
my_dict['k1']-= 120 --> 3

'''

di = {}
di{'str'} = "add string"
di{'asw'} = 12.21
# di = {'str':'add string', 'asw':12.21}
d = {'k1':{'nestkey':{'subnestkey':'value'}}}
d['k1']['nestkey']['subnestkey'] # 'value'

d = {'k1':1,'k2':2, 'k3':3}
d.keys() # ['k3','k1','k2']
d.values() # [1,2,3]
d.items() # [('k3',3), ('k2',2), ('k1',1)]