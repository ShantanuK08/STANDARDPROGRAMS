print("Enter Non-Recursive Merge Sort")

# Function to merge two sorted sub-arrays
def merge(arr, left, mid, right):
    left_sub = arr[left:mid + 1]  # Left sub-array
    right_sub = arr[mid + 1:right + 1]  # Right sub-array

    i = j = 0  # Pointers for left_sub and right_sub
    k = left  # Pointer for the original array

    # Merge the two sub-arrays into arr
    while i < len(left_sub) and j < len(right_sub):
        if left_sub[i] <= right_sub[j]:
            arr[k] = left_sub[i]
            i += 1
        else:
            arr[k] = right_sub[j]
            j += 1
        k += 1

    # Copy any remaining elements from left_sub
    while i < len(left_sub):
        arr[k] = left_sub[i]
        i += 1
        k += 1

    # Copy any remaining elements from right_sub
    while j < len(right_sub):
        arr[k] = right_sub[j]
        j += 1
        k += 1

# Non-Recursive Merge Sort Function
def merge_sort_iterative(arr):
    n = len(arr)
    current_size = 1  # Start with sub-arrays of size 1

    # Double the size of sub-arrays in each iteration
    while current_size < n:
        for left in range(0, n, 2 * current_size):
            mid = min(left + current_size - 1, n - 1)
            right = min(left + 2 * current_size - 1, n - 1)
            merge(arr, left, mid, right)

        current_size *= 2  # Double the sub-array size

# Test the merge_sort_iterative function
arr = [1,24,5,6,7,89,43]  # Define an array to sort
merge_sort_iterative(arr)  # Call the non-recursive merge sort
print("Sorted array:", arr)  # Output the sorted array

print("Exit Non-Recursive Merge Sort")




#Eliminates recursion by iteratively merging sub-arrays in a bottom-up manner.

#Begins with sub-arrays of size 1 and doubles the size in each pass.

#Avoids the overhead of recursive calls, reducing stack memory usage.

#Combines two sorted sub-arrays into a single sorted array using the merge function.

#Uses left, mid, and right indices to define sub-array boundaries for merging.


#Doubles the sub-array size (current_size *= 2) after each iteration, gradually encompassing the entire array.

#Maintains the relative order of equal elements, making it a stable sorting algorithm.

#Overall time complexity  is O(nlogn), the same as recursive merge sort.

#Requires additional space for temporary arrays during merging,O(n) auxiliary space.

#Produces a fully sorted array after progressively merging all sub-arrays.