def find_max(numbers):
    if len(numbers) == 0:
        return None  # Handle empty list case
    
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

# Example usage
numbers = [17, 92, 18, 33, 58, 7, 33, 42]
max_number = find_max(numbers)
print(f"The largest number is: {max_number}")  # Output: The largest number is: 92
