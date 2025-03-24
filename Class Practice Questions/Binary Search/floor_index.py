def find_floor_index(arr, k):
    low, high = 0, len(arr) - 1
    floor_index = -1  # Default if no element ≤ k

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= k:
            floor_index = mid  # Potential floor index
            low = mid + 1  # Search in the right half for a closer floor
        else:
            high = mid - 1  # Search in the left half

    return floor_index

# Example Usage
arr = [1, 3, 5, 7, 9, 11]
k = 6
print(find_floor_index(arr, k))  # Output: 2 (arr[2] = 5)

k = 10
print(find_floor_index(arr, k))  # Output: 4 (arr[4] = 9)

k = 0
print(find_floor_index(arr, k))  # Output: -1 (No element ≤ 0)
