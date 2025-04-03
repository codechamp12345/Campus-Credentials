i = {"A": 10, "B": 20, "C": 30, "D": 40, "E": 50}

largest_value = None  # Initialize with None to handle empty dictionaries

for value in i.values():
    if largest_value is None or value > largest_value:
        largest_value = value

print("Largest value:", largest_value)  # Output: Largest value: 50