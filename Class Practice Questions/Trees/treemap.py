from sortedcontainers import SortedDict

#Creating treemap
tree_map = SortedDict() 

#Add key Value Pairs
tree_map['a'] = 1
tree_map['b'] = 3
print(tree_map)  

# Accessing a value by key
value = tree_map['b']
print(value) # Output = 3

# Removing Key 
tree_map.pop('b')
print(tree_map) # Output = SortedDict({'a': 1})

# Iterating through the map
# Key
for key in tree_map.keys():
    print(key) # Output = a 

#Value
for value in tree_map.values():
    print(value) # Output = 1 

#KeyValuePair
for key,value in tree_map.items():
    print(key,value) # Output = a 1 
  
