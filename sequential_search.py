print("Enter Sequential Search")

# Sequential Search Function
def sequential_search(arr, target):
    # Iterate through each element in the array
    for index, element in enumerate(arr):
        if element == target:  # Check if the current element matches the target
            return f"Found at index {index}"  # Return the index where the element is found

    return "Not Found"  # Return "Not Found" if the target is not in the array

# Test the sequential_search function
arr = [1, 24, 5, 6, 7, 89, 43]  # Define the array
target = 3  # Define the element to search for
result = sequential_search(arr, target)  # Call sequential_search to find the target
print(result)  # Output the result

print("Exit Sequential Search")


















#Iterative Approach:Traverses the list from start to end.
#Worst Case Time Complexity:𝑂(𝑛) where 𝑛n is the number of elements in the list
#Best Case Time Complexity:O(1), if the target is the first element.
#Unsorted Input:Works efficiently even for unsorted arrays.
#Return Result:Outputs the index if found or "Not Found" if the target is absent.