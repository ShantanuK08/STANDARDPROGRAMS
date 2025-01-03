print("Enter Insertion and Reversal")

# Function to insert a number at a specific position
def insert_at_position(arr, num, position):
    # Insert the number at the specified position (1-based index)
    arr.insert(position - 1, num)  # Subtract 1 to convert to 0-based index
    return arr

# Function to reverse the array
def reverse_array(arr):
    return arr[::-1]  # Reverse the array using slicing

# Main code
arr = [1, 24, 5, 6, 7, 89, 43]  # Define the array
num = 99  # Number to insert
position = 3  # Position to insert the number at (1-based index)

# Step 1: Insert the number at the specified position
arr = insert_at_position(arr, num, position)
print(f"Array after inserting {num} at position {position}:", arr)

# Step 2: Reverse the array
arr_reversed = reverse_array(arr)
print("Reversed array:", arr_reversed)

print("Exit Insertion and Reversal")





