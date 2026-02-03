import time

def simple_recursive_multiplication(x, y):
    # Base case: if either number is a single digit, multiply directly
    if len(x) == 1 or len(y) == 1:
        return str(int(x) * int(y))
    
    # Make the numbers the same length by padding with zeros
    n = max(len(x), len(y))
    n = n if n % 2 == 0 else n + 1  # Ensure even length
    x = x.zfill(n)
    y = y.zfill(n)
    
    # Split the numbers into halves
    mid = n // 2
    x_high, x_low = x[:mid], x[mid:]
    y_high, y_low = y[:mid], y[mid:]
    
    # Recursively calculate the products
    z0 = simple_recursive_multiplication(x_low, y_low)
    z1 = simple_recursive_multiplication(x_high, y_high)
    z2 = simple_recursive_multiplication(str(int(x_low) + int(x_high)), str(int(y_low) + int(y_high)))
    
    # Combine the results
    result = int(z1) * (10 ** n) + (int(z2) - int(z1) - int(z0)) * (10 ** (n // 2)) + int(z0)
    return str(result)

    #Implementation of Karatsuba Multiplication
def karatsuba_multiplication(x, y):
    # Base case: If either number is a single digit, multiply them directly and return the result as a string.
    if len(x) == 1 or len(y) == 1:
        return str(int(x) * int(y))

   # Make the lengths of the two numbers equal by padding with leading zeros. 
    n = max(len(x), len(y)) # Find the maximum length of the two numbers.
    n = n if n % 2 == 0 else n + 1 # Ensure the length is even.
    x = x.zfill(n) # Pad x with leading zeros to make its length n.
    y = y.zfill(n) # Pad y with leading zeros to make its length n.

    # Split the numbers into halves.
    mid = n // 2
    x_high, x_low = x[:mid], x[mid:]  # Split x into high and low parts.
    y_high, y_low = y[:mid], y[mid:]  # Split y into high and low parts.

    # Recursively calculate the three products needed for Karatsuba multiplication.
    z0 = karatsuba_multiplication(x_low, y_low) # Product of the low parts.
    z1 = karatsuba_multiplication(x_high, y_high) # Product of the high parts.
    z2 = karatsuba_multiplication(str(int(x_low) + int(x_high)), str(int(y_low) + int(y_high))) # Product of the sums of the parts.

    # Combine the results using Karatsuba's formula: result = z1 * 10^n + (z2 - z1 - z0) * 10^(n/2) + z0  
    result = int(z1) * (10 ** n) + (int(z2) - int(z1) - int(z0)) * (10 ** (n // 2)) + int(z0)
    return str(result)

# Test cases
test_cases = [
    ("1234", "5678"),
    ("12345678", "87654321"),
    ("3141592653589793238462643383279502884197169399375105820974944592",
     "2718281828459045235360287471352662497757247093699959574966967627")
]

for x, y in test_cases:
    print(f"Simple Recursive Multiplication of {x} and {y}: {simple_recursive_multiplication(x, y)}")
    print(f"Karatsuba Multiplication of {x} and {y}: {karatsuba_multiplication(x, y)}")
    print()

    # Generate test numbers of increasing size
sizes = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
results = []

for n in sizes:
    x = "9" * n
    y = "8" * n
    
    # Time simple recursive multiplication
    start = time.time()
    simple_recursive_multiplication(x, y)
    simple_time = time.time() - start
    
    # Time Karatsuba multiplication
    start = time.time()
    karatsuba_multiplication(x, y)
    karatsuba_time = time.time() - start
    
    results.append((n, simple_time, karatsuba_time))

# Display results
print("Size\tSimple Recursive\tKaratsuba")
for n, simple_time, karatsuba_time in results:
    print(f"{n}\t{simple_time:.6f}\t\t{karatsuba_time:.6f}")