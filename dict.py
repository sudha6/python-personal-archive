my_dict = {'name':'Hema','name':'Sudha', 'age': 19}
#the reason it displays last key is the value gets overwritten as dict is key-value pair

print(my_dict)
# Output: Jack
print(my_dict['name'])

# Output: 26
#print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# my_dict.get('address')
# my_dict['address']

dict1 = {'address':"Vandalur", 'ph':9150549766}

print(dict1)

dict2 = {}

dict2.update(my_dict)

dict2.update(dict1)

print(dict2)