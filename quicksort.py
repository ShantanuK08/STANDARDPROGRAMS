
print("Enter quick sort")
# Quick Sort Function
def quick_sort(arr):
   
    # Base case: an array with one or no elements is already sorted
    if len(arr) <= 1:
        return arr  # If the array has one or no elements, it's already sorted

    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively apply quick_sort to the left and right parts
    return quick_sort(left) + middle + quick_sort(right)

# Test the quick_sort function
arr = [1, 24, 5, 6, 7, 89, 43]  # Define an array to be sorted
sorted_arr = quick_sort(arr)  # Call quick_sort to sort the array
print("Sorted array:", sorted_arr)  # Output the sorted array
print("Exit quick sort")



#Pivot Selection: A pivot is chosen (middle element) to divide the array into smaller and larger elements for efficient sorting.

#Recursive Nature: Quick Sort works by recursively dividing the array into subarrays, sorting them, and combining the results.

#Partitioning: The array is partitioned into three lists: elements smaller than the pivot, equal to the pivot, and greater than the pivot.

#Time Complexity: Quick Sort’s average time complexity is O(n log n), though it can degrade to O(n²) in the worst case.

#Space Complexity: Quick Sort has O(log n) space complexity due to recursive calls, making it efficient in terms of memory.

#Efficient Sorting: The recursive partitioning ensures that each element is processed only once, making the sorting process efficient.

#In-Place Sorting: In typical implementations, Quick Sort can be in-place, reducing additional memory usage.

#List Comprehension: List comprehensions are used to create smaller, equal, and larger subarrays in a concise and efficient way.

#Combining Subarrays: After sorting, the subarrays are concatenated using the + operator, combining the results from the left, middle, and right parts.
