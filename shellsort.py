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









#Shell sort improves upon insertion sort by allowing comparisons and exchanges over larger gaps, reducing the overall number of moves.

#Starts with a large gap (usually 𝑛//2n//2) and reduces it progressively until it becomes 1.

#Elements separated by the gap are treated as a sub-array and sorted using insertion sort principles.

#The gap is halved in each iteration (or reduced using a sequence like Knuth’s or Hibbard’s).

#Requires no additional memory aside from a few variables, making it space-efficient (𝑂(1)O(1)).

#Sorting with a large gap allows the array to become partially ordered, speeding up the final sorting pass when the gap is 1.

#Depends on the gap sequence, typically 𝑂(𝑛1.5)O(n 1.5 ) in the average case and can reach 𝑂(𝑛2)O(n 2) for certain sequences. Optimized sequences bring it closer to 𝑂(𝑛log⁡𝑛)O(nlogn).

#Generally unstable because elements can move far apart, disrupting their relative order.

#Performs particularly well for small or nearly sorted arrays.

#Can be implemented with different gap sequences for specific use cases, allowing flexibility in optimization.