def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage with potential error:
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") # This will correctly print 0

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}") # This will correctly print 3.0

my_list = [1,2, 'a', 4, 5]
average = calculate_average(my_list) # This will raise TypeError because of string in the list
print(f"The average is: {average}")