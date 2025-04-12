import heapq 
h = [10,20,30,40,50] # Creating a list
heapq.heapify(h)
print(h)

# Operations
heapq.heappush(h,90) # Adding 
print(h)

print(h[0]) # Peek

heapq.heappop(h) # Removing 
print(h[0])

print(len(h)) # Size 