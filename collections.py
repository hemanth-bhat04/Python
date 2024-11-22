#Lists and its methods

# Initial list of items
items = ["bread", "chips", "pasta", "fruits"]
print("Initial list:", items)

#indexing
items[0] = "biscuits"
print("After changing the first item:", items)

#append
items.append("vegetables")
print("After appending 'vegetables':", items)

# Insert 
items.insert(3, "tomato")
print("After inserting 'tomato' at index 3:", items)

# Remove 
items.remove("chips")  
print("After removing 'chips':", items)

# Remove an item by index 
removed_item = items.pop(2)  
print("After popping index 2 (removed item):", removed_item)
print("List after popping:", items)

# Find the index of a specific item in the list
index_of_pasta = items.index("pasta") 
print("Index of 'pasta':", index_of_pasta)

# Sort 
items.sort()  
print("After sorting the list:", items)

# Reverse 
items.reverse()  
print("After reversing the list:", items)

# Count 
count_of_biscuits = items.count("biscuits") 
print("Number of 'biscuits' in the list:", count_of_biscuits)

# Copy 
new_items = items.copy()  
print("Copy of the list:", new_items)

# Clear 
items.clear()  
print("List after clearing all items:", items)

# Add multiple items 
new_items.extend(["milk", "cheese", "butter"])  
print("After extending the list:", new_items)

#list comprehension
squares = [i**2 for i in range(10)]
print(squares)


