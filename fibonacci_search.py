print("Enter Fibonacci Search")
print("Enter Fibonacci Search")

def fibonacci_search(arr, target):
    arr.sort()  # Ensure the array is sorted
    print("Sorted array:", arr)
    n = len(arr)

    # Initialize Fibonacci numbers
    fib_m_2 = 0  # (m-2)'th Fibonacci number
    fib_m_1 = 1  # (m-1)'th Fibonacci number
    fib = fib_m_1 + fib_m_2  # m'th Fibonacci number

    # Generate the smallest Fibonacci number greater than or equal to n
    while fib < n:
        fib_m_2 = fib_m_1
        fib_m_1 = fib
        fib = fib_m_1 + fib_m_2

    # Marks the eliminated range from the front
    offset = -1

    # While there are elements to be inspected
    while fib > 1:
        # Calculate the index to compare
        i = min(offset + fib_m_2, n - 1)

        print(f"Comparing index {i}, value: {arr[i]}")

        # If the target is greater than the value at index `i`,
        # cut the subarray array from offset to `i`
        if arr[i] < target:
            fib = fib_m_1
            fib_m_1 = fib_m_2
            fib_m_2 = fib - fib_m_1
            offset = i
        # If the target is smaller than the value at index `i`,
        # cut the subarray after `i+1`
        elif arr[i] > target:
            fib = fib_m_2
            fib_m_1 = fib_m_1 - fib_m_2
            fib_m_2 = fib - fib_m_1
        # Element found, return the index
        else:
            return f"Found at index {i}"

    # Check the last element if necessary
    if fib_m_1 and offset + 1 < n and arr[offset + 1] == target:
        return f"Found at index {offset + 1}"

    # Element not found
    return "Not Found"

# Test the Fibonacci Search function
arr = [1, 24, 5, 6, 7, 89, 43]
target = 3
result = fibonacci_search(arr, target)
print(result)

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