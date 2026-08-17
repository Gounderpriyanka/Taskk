"""
Task 2.Write a function total_cart_amount(prices) that takes a list of product prices as strings 
(like ['199.99', '49', '350.75']) and returns the total as a float.Print the result for a sample 
Flipkart-style cart.<br><br><em><strong>Hint:</strong> Use float() to convert each string before summing.</em>
"""

def total_cart_amount(prices):
    total = 0.0
    for i in prices:
        total = total + float(i)
    return total

cart_prices = ['199.99', '49', '350.75']
print("Flipkart-style cart",total_cart_amount(cart_prices))