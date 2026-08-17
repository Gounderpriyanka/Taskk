"""
Task 3.Add both single-line and multi-line comments in your script explaining
 what each section does, using # for single-line and triple quotes for multi-line comments.

"""

"""
This program checks whether a product
is eligible for free delivery.
"""

# Take product price as input
price = int(input("Enter product price: "))

# Check the delivery condition
if price > 1000:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")