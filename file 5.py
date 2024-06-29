def sum_of_integers(n):
    if n <= 0:
        return 0  # Sum is zero for non-positive n
    return n * (n + 1) // 2  # Using integer division

# Example usage
n1 = 10
n2 = 100

sum_1_to_10 = sum_of_integers(n1)
sum_1_to_100 = sum_of_integers(n2)

print(f"The sum of numbers from 1 to {n1} is: {sum_1_to_10}")  # Output: 55
print(f"The sum of numbers from 1 to {n2} is: {sum_1_to_100}")  # Output: 505
