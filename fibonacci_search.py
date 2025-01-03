print("Enter Fibonacci Search")

# Fibonacci Search Function
def fibonacci_search(arr, target):
    arr.sort()  # Ensure the array is sorted
    print("Sorted array:", arr)  # Output the sorted array for reference

    n = len(arr)
    fib_m_2 = 0  # (m-2)'th Fibonacci number
    fib_m_1 = 1  # (m-1)'th Fibonacci number
    fib = fib_m_1 + fib_m_2  # m'th Fibonacci number

    # Find the smallest Fibonacci number greater than or equal to the length of the array
    while fib < n:
        fib_m_2 = fib_m_1
        fib_m_1 = fib
        fib = fib_m_1 + fib_m_2

    # Mark the range for searching
    offset = -1

    # Perform the search using Fibonacci numbers
    while fib > 1:
        i = min(offset + fib_m_2, n - 1)  # Calculate the index for the comparison

        if arr[i] == target:
            return f"Found at index {i}"  # Return index if the target is found
        elif arr[i] < target:
            fib = fib_m_1
            fib_m_1 = fib_m_2
            fib_m_2 = fib - fib_m_1
            offset = i
        else:
            fib = fib_m_2
            fib_m_1 = fib_m_1 - fib_m_2
            fib_m_2 = fib - fib_m_1

    # Check the last element
    if fib_m_1 and arr[offset + 1] == target:
        return f"Found at index {offset + 1}"

    return "Not Found"  # Return "Not Found" if the target is not in the array

# Test the fibonacci_search function
arr = [1, 24, 5, 6, 7, 89, 43]  # Define the array
target = 3  # Define the element to search for
result = fibonacci_search(arr, target)  # Call fibonacci_search to find the target
print(result)  # Output the result

print("Exit Fibonacci Search")



#Sorted Array:

#Fibonacci search works only on sorted arrays, like binary search.
#Fibonacci Numbers:

#The algorithm uses Fibonacci numbers to decide the search range, which can be more efficient in some cases compared to binary search.
#Time Complexity:

#Best Case: 

#O(1), if the element is found at the first comparison.
#Worst Case: 

#O(logn), where 

#n is the size of the array.
#Space Complexity:

#O(1), since it uses only a constant amount of extra space.
#Efficiency:

#Fibonacci search can sometimes outperform binary search, especially when working with large datasets.