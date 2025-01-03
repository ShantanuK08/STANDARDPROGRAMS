# Merge Sort Implementation

# Merge function to combine two halves
def merge(left, right):
    print("Enter merge sort")
    print("Merging:", left, "and", right)  # This will show what is being merged

    result = []  # Initialize an empty list to store the merged result
    i = j = 0  # Initialize indices for the left and right halves

    # Merge the two lists while maintaining order
    while i < len(left) and j < len(right):  # Loop until we reach the end of either left or right
        if left[i] < right[j]:  # Compare the current element of left and right
            result.append(left[i])  # If left element is smaller, add it to result
            i += 1  # Move the index in the left half
        else:
            result.append(right[j])  # If right element is smaller, add it to result
            j += 1  # Move the index in the right half

    # If there are remaining elements in left or right, append them to the result
    result.extend(left[i:])  # Append any remaining elements from left
    result.extend(right[j:])  # Append any remaining elements from right

    return result  # Return the merged sorted list


# Merge Sort Function
def merge_sort(arr):
    # Base case: an array with one element is already sorted
    if len(arr) <= 1:
        return arr  # If the array has one or no elements, it's already sorted

    # Split the array into two halves
    mid = len(arr) // 2  # Find the midpoint of the array
    left = merge_sort(arr[:mid])  # Recursively sort the left half
    right = merge_sort(arr[mid:])  # Recursively sort the right half

    # Merge the sorted halves
    return merge(left, right)


# Test the merge_sort function
arr = [1, 24, 5, 6, 7, 89, 43]  # Define an array to be sorted
sorted_arr = merge_sort(arr)  # Call merge_sort to sort the array
print("Sorted array:", sorted_arr)  # Output the sorted array
print("Exit merge sort")




#Merge Function: It combines two sorted lists (left and right) into a single sorted list.
#Comparing Elements: Inside the merge function, elements from left and right are compared to ensure the final list is sorted.
#append() Method: It adds individual elements to the result list as we compare the elements of left and right.
#extend() Method: This is used to add all remaining elements from either left or right to result after one of them is exhausted.
#Recursive Splitting: The merge_sort function splits the array into two halves recursively until each half has one or no elements.
#Base Case: The recursion stops when the array has one element or no elements (i.e., it's already sorted).
#Midpoint Calculation: mid = len(arr) // 2 calculates the midpoint to divide the array into two halves.
#Time Complexity: Merge Sort has a time complexity of O(n log n), making it efficient for large datasets.
#merge() Efficiency: The merge step processes each element once, contributing to the O(n) time complexity in each merge.
#Why Use extend(): extend() is preferred over append() for adding multiple elements to a list in one operation, improving efficiency.

