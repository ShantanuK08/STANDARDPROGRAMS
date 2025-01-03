print("Enter Shell Sort")

# Shell Sort Function
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Initialize the gap size

    # Reduce the gap size in each iteration
    while gap > 0:
        # Perform a gapped insertion sort for this gap size
        for i in range(gap, n):
            temp = arr[i]  # Temporarily store the current element
            j = i

            # Shift elements of the sorted sub-array to the right to make room for temp
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp  # Place temp in its correct position

        gap //= 2  # Reduce the gap size

    return arr  # Return the sorted array

# Test the shell_sort function
arr = [1,24,5,6,7,89,43]  # Define an array to be sorted
sorted_arr = shell_sort(arr)  # Call shell_sort to sort the array
print("Sorted array:", sorted_arr)  # Output the sorted array

print("Exit Shell Sort")
