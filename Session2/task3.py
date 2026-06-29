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