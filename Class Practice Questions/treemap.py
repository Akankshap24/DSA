from sortedcontainers import SortedDict

#Creating treemap
tree_map = SortedDict() 

#Add key Value Pairs
tree_map['a'] = 1
tree_map['b'] = 3
print(tree_map)  # Output = SortedDict({'a': 1, 'b': 3}

# Accessing a value by key
value = tree_map['b']
print(value) # Output = 3

# Removing Key 
tree_map.pop('b')
print(tree_map) # Output = SortedDict({'a': 1})

