print("Enter DSA Merging Two Arrays")

# Merge function to merge two sorted arrays
def merge_sorted_arrays(arr1, arr2):
    # Initialize pointers for both arrays
    i, j = 0, 0
    result = []  # To store the merged array

    # Traverse both arrays and pick the smaller element
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # If any elements are left in arr1, add them to result
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # If any elements are left in arr2, add them to result
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

# Test the merge_sorted_arrays function
arr1 = [1, 3, 5]  # First sorted array
arr2 = [2, 4, 6]  # Second sorted array

merged_array = merge_sorted_arrays(arr1, arr2)
print(f"Merged and Sorted array: {merged_array}")

print("Exit DSA Merging Two Arrays")
