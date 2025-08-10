expression = input("Expression: ").strip()

# Split into parts
x, y, z = expression.split()

# Convert to integers
x = int(x)
z = int(z)

# Perform the calculation
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
else:
    result = None  # In case of unexpected operator

# Output the result formatted to 1 decimal place
print(f"{result:.1f}")

