print("Enter Practice")


print("Enter in sequential search")

def sequence_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            print("Found during search")
            return f"Found at index {index}"
    print("Not found during search")
    return "Not Found"

arr = [1, 24, 5, 6, 7, 89, 43]
target = 7
result = sequence_search(arr, target)
print(result)
print("Exit Sequential search")








print("Enter in binary search")

def binary_search(arr, target):
    arr.sort()  # Ensure the array is sorted
    print("Sorted array:", arr)  # Output the sorted array for reference
    left, right = 0, len(arr) - 1  # Define the search range

    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if arr[mid] == target:  # Check if the middle element is the target
            return f"Found at index {mid}"
        elif arr[mid] < target:  # Target is in the right half
            left = mid + 1
        else:  # Target is in the left half
            right = mid - 1

    return "Not Found"  # Target is not in the array

# Test the binary_search function
arr = [1, 24, 5, 6, 7, 89, 43]
target = 3
result = binary_search(arr, target)  # Call binary_search to find the target
print(result)  # Output the result

print("Exit Binary Search")
