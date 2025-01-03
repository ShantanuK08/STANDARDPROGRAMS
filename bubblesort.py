def bubble_sort(arr):
    print("Enter in bubble_sort sorting")

    n = len(arr)  # Get the length of the array
    
    for i in range(n):
        swapped = False  # Track whether a swap happened in this iteration

        # Traverse through the array from 0 to n-i-1
        for j in range(0, n - i - 1):  # Corrected the loop range
            # Compare adjacent elements and swap them if they are in the wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                swapped = True  # Mark that a swap occurred

        # If no elements were swapped, the array is already sorted, so break early for optimization
        if not swapped:
            print("Array is already sorted.")
            break
            
    return arr

# Test Array
arr = [1, 24, 5, 6, 7, 89, 43]
print("Original array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)


#The loop inside should iterate from 0 to n - i - 1, not 0 - i - 1. The incorrect range caused no iterations to occur.

#Ensure that the swapping logic is properly aligned, and no extra commas (arr[j],arr[j+1]=arr[j+1],arr[j],) are present.

#The if not swapped block must be placed outside the inner loop to correctly determine whether a full pass through the array was made without any swaps.

#Correct indentation for if blocks and statements within the loop.

#Best case (already sorted): O(n); Worst case: O(n²).

#Best case (already sorted): O(n); Worst case: O(n²).Inefficient for large datasets but simple and intuitive.Modifies the array in-place; no extra memory used.Suitable for small or nearly sorted arrays.