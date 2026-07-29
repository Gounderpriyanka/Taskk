# Task 1.Write a Python script that takes your current Spotify listening time in minutes and 
# checks if it is above 120 minutes; if yes, print 'You are a true music fan!', otherwise
#  print 'Keep listening!'.
'''minutes = int(input("Enter your Spotify listening time in minutes:"))
if minutes>120:
    print("'You are a true music fan!'")
else:
    print("'Keep listening!'")'''



# Task 2.Create a Python program that asks the user to enter their Zomato order amount and 
# checks if it is above 300; if yes, print 'Eligible for free delivery', else print 'Delivery charges apply'.

'''Amount = int(input("Enter your Zomato order amount:"))
if Amount>300:
    print("'Eligible for free delivery'")
else:
    print("Delivery charges apply!")'''



# Task 3.Build a Python script that takes your Flipkart cart total and applies the following
#  logic: if total > 2000, print 'You get a 10% discount'; elif total > 1000, print 'You get a 5% discount'; 
# else print 'No discount available'.

'''Total = int(input("Enter your Filpkart cart total:"))
if Total>2000:
    print("'You get a 10% discount'")
elif Total>1000:
    print("'You get a 5% discount'")
else:
    print("'No discount available'")'''



# Task 4.Write a Python program that asks the user to enter their IPL fantasy team points and 
# uses nested if-else statements to print: 'Champion' if points > 800, 'Top Performer' if points 
# between 500 and 800, 'Keep Trying' otherwise.Hint: Use nested if-else blocks to check the ranges.

Team_points = int(input("Enter your IPL fantasy team points:"))
if Team_points > 800:
    print("Champions")
    if 800<Team_points and Team_points>500:
        print("Top Performers!")
else:
    print("Keep trying")

    



