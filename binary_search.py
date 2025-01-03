print("Enter Binary Search")

# Binary Search Function
def binary_search(arr, target):
    arr.sort()  # Ensure the array is sorted
    print("Sorted array:", arr)  # Output the sorted array for reference
    left, right = 0, len(arr) - 1  # Define the search range

    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if arr[mid] == target:
            return f"Found at index {mid}"  # Return index if target is found
        elif arr[mid] < target:
            left = mid + 1  # Continue searching in the right half
        else:
            right = mid - 1  # Continue searching in the left half

    return "Not Found"  # Return "Not Found" if the target is not in the array

# Test the binary_search function
arr = [1, 24, 5, 6, 7, 89, 43]  # Define the array
target = 3  # Define the element to search for
result = binary_search(arr, target)  # Call binary_search to find the target
print(result)  # Output the result

print("Exit Binary Search")






#Sorted Array:

#Binary search requires a sorted array to work.
#Time Complexity:

#Best Case: 

#O(1), if the target is the middle element.
#Worst Case: 

#O(logn), where 

#n is the number of elements.
#Space Complexity:

#O(1), iterative approach requires no additional memory.
#Efficient for Large Datasets:

#Significantly faster than linear search for large sorted arrays.
#Divide and Conquer:

#Reduces the search range by half in each iteration.