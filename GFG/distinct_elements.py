# Function to count distinct elements in an array
# https://www.geeksforgeeks.org/python-program-to-count-distinct-elements-in-an-array/
def distinct(arr):
    distinct_arr = set(arr)
    return len(distinct_arr)