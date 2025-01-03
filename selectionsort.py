print("Enter Selection Sort")
# Selection Sort Function
def selection_sort(arr):
 # Loop through the entire array
    for i in range(len(arr)):
         # Find the minimum element in the remaining unsorted part of the array
        min_index = i

    for j in range(len(arr)):

        if arr[j] < arr[min_index]:

            min_index =j
         # Swap the found minimum element with the first element of the unsorted part
            arr[i],arr[min_index] = arr[min_index],arr[i]

            return arr # Return the sorted array

# Test the selection_sort function        
arr = [1, 24, 5, 6, 7, 89, 43]  # Define an array to be sorted
sorted_arr = selection_sort(arr)  # Call selection_sort to sort the array
print("Sorted array:", sorted_arr)  # Output the sorted array

print("Exit selection sort")


#Finding the Minimum: For each position in the array, the algorithm finds the minimum element in the unsorted portion and swaps it with the current position.

#Outer Loop: The outer loop goes through each element in the array to place the smallest element in the correct position.

#Inner Loop: The inner loop compares the current element with the remaining unsorted elements to find the minimum.

#Swapping: Once the minimum element is found, it is swapped with the element at the current position.

#Time Complexity: The time complexity of Selection Sort is O(n²), where n is the number of elements. This is because for each element, the algorithm scans the entire remaining unsorted portion.

#Space Complexity: The space complexity is O(1) because the sorting is done in-place without using additional storage.

#Stability: Selection Sort is not stable, meaning it does not preserve the relative order of equal elements.

#In-Place Sorting: The algorithm sorts the array in-place, without requiring extra memory for another array.

#Efficient for Small Arrays: Though Selection Sort is inefficient for large datasets, it can be useful for small arrays or partially sorted data.

#Simple Implementation: Selection Sort is easy to implement and understand, making it a good choice for educational purposes, despite its inefficiency for large datasets.



