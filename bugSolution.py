def calculate_average(numbers):
    # Validate input: Check if the list is empty
    if not numbers:
        return 0

    # Validate input: Check if all elements are numbers
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers.")

    return sum(numbers) / len(numbers)

# Example usage:
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")  # Output: 0

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")  # Output: 3.0

my_list = [1, 2, 'a', 4, 5]
try:
    average = calculate_average(my_list)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: List must contain only numbers.