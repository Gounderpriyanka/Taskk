"""
Task 2.Write a Python script that uses indentation correctly to check if a Flipkart product's price is above 1000;
 if yes, print 'Eligible for free delivery', else print 'Delivery charges apply'.
<br><br><em><strong>Hint:</strong> Use an if-else block and make sure your indentation is consistent.</em>
"""

price = int(input("Enter the  Flipkart product's price:"))
if price > 1000:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")
