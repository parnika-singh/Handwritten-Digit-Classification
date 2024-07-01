class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

# Example usage and test results
calc = Calculator()

# Test results
print("Addition (3 + 5):", calc.add(3, 5))  # Expected output: 8
print("Subtraction (10 - 4):", calc.subtract(10, 4))  # Expected output: 6
print("Multiplication (7 * 6):", calc.multiply(7, 6))  # Expected output: 42
print("Division (8 / 2):", calc.divide(8, 2))  # Expected output: 4.0
print("Division by zero (5 / 0):", calc.divide(5, 0))  # Expected output: Error! Division by zero.
