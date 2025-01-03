print("Enter Insertion Sort")

# Insertion Sort Function
def insertion_sort(arr):
    # Loop over the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1

        # Shift elements in the sorted part of the array to make room for the key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Move the element one position to the right
            j -= 1
        
        arr[j + 1] = key  # Insert the key into the correct position

    return arr  # Return the sorted array

# Test the insertion_sort function
arr =  [1,24,5,6,7,89,43] # Define an array to be sorted
sorted_arr = insertion_sort(arr)  # Call insertion_sort to sort the array
print("Sorted array:", sorted_arr)  # Output the sorted array

print("Exit Insertion Sort")







#Builds the sorted portion of the array incrementally by inserting each element in its proper place.
#Comparison with Sorted Subarray:

#Compares the current element with elements in the already sorted part of the array.


#Shifts larger elements one position to the right to make room for the current element.


#Sorts the array in-place, requiring 𝑂(1)O(1) extra memory.


#Performs efficiently (𝑂(𝑛)O(n)) for nearly sorted arrays as fewer comparisons and shifts are needed.

#Time complexity is 𝑂(𝑛2)O(n 2 ) when the array is sorted in reverse order.

#Maintains the relative order of elements with equal keys, making it stable.

#Performs well for small-sized arrays or as a subroutine in hybrid sorting algorithms like Timsort.

#Easy to implement and understand due to its intuitive approach.

#Can be used for scenarios where elements are received in a stream, as it handles each new element incrementally.