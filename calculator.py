# calculator.py - Simple calculator with intentional issues for testing

# ISSUE: Hardcoded secret - should trigger security warning
API_KEY = "sk-1234567890abcdef"

class Calculator:
    def __init__(self):
        self.history = []
    
    # ISSUE: Missing type hints and docstring
    def add(self, a, b):
        return a + b
    
    # ISSUE: Division by zero not handled - will crash!
    #lol
    def divide(self, x, y):
        return x / y
    
    # ISSUE: Poor variable naming
    def calc_stuff(self, nums):
        result = 0
        # ISSUE: No input validation
        for n in nums:
            result += n * 2
        return result
    
    # ISSUE: Magic number without explanation
    def apply_tax(self, amount):
        return amount * 1.08  # What tax rate is this?

# ISSUE: No main function guard
calculator = Calculator()
print(calculator.add(5, 3))
print(calculator.divide(10, 0))  # This will crash!