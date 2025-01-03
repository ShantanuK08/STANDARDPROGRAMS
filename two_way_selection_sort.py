print("Enter 2-way merge sort")

# Merge function to combine two sorted halves
def merge(left, right):
    result = []  # Initialize an empty list for the merged result
    i = j = 0  # Indices for left and right halves

    # Merge the two halves while maintaining order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])  # Add the smaller element from the left half
            i += 1
        else:
            result.append(right[j])  # Add the smaller element from the right half
            j += 1

    # Add any remaining elements from the left and right halves
    result.extend(left[i:])  # Extend with remaining elements in the left half
    result.extend(right[j:])  # Extend with remaining elements in the right half

    return result

# Two-Way Merge Sort Function
def merge_sort(arr):
    # Base case: an array with one or no elements is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Recursively sort the left half
    right = merge_sort(arr[mid:])  # Recursively sort the right half

    # Merge the sorted halves
    return merge(left, right)

# Test the merge_sort function
arr = [1,24,5,6,7,89,43]  # Example array to sort
sorted_arr = merge_sort(arr)  # Call merge_sort to sort the array
print("Sorted array:", sorted_arr)  # Output the sorted array

print("Exit 2-way merge sort")




#Divide and Conquer: The array is divided into two halves recursively until each subarray has only one element (base case).

#Merge Step: The merge function combines two sorted subarrays into a single sorted array.

#Two-Way: The "two-way" aspect comes from merging two sorted subarrays at a time.

#Base Case: The recursion stops when the array has only one element, which is inherently sorted.

#Time Complexity: O(n log n) due to dividing the array into halves (log n levels) and merging (O(n) per level).

#Space Complexity: O(n) for the temporary arrays created during the merge

