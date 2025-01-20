from sortedcontainers import SortedSet

# Creating a TreeSet equivalent using SortedSet
tree_set = SortedSet()

# Adding elements to the set
tree_set.add(5)
tree_set.add(3)
tree_set.add(8)
tree_set.add(5)  # Duplicate elements will be ignored

# Printing the set (elements will be sorted)
print(tree_set)

# Checking if an element exists
print(3 in tree_set)  # Output: True

# Iterating through the set
for element in tree_set:
    print(element)
