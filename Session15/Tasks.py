# 1.Write a Python function called get_song_duration_per_minute that divides the total duration
# of a Spotify playlist (in minutes) by the number of songs, and handles the case where the
# number of songs is zero using try, except, and finally blocks.


'''def get_song_duration_per_minute():

    try :
        n = int(input("Enter total playlist duration (minutes):"))
        y = int(input("Enter number of songs:"))
        result = n/y
        print("Average duration per song : ",result)
    except ZeroDivisionError:
        print("Error: Number of songs cannot be zero.")
    finally :
        print("completed")

get_song_duration_per_minute()'''

 
# 2.Build a Flipkart-style price-per-item calculator: take total cart amount and item count as input, 
# perform division, and use try-except to catch and display a user-friendly message if the item count is zero.


'''def Flipkart_Price_per_Item():
    try :
         n = int(input("Enter total cart amount:"))
         y = int(input("Enter number of items:"))
         result = n/y
    except ZeroDivisionError:
         print("Error: Number of items cannot be zero.")
         
         
Flipkart_Price_per_Item()'''



# 3.Create a Paytm cashback calculator that asks for total spend and number of offers applied, then divides 
# spend by offers to show average cashback per offer. If the number of offers is zero, raise a custom 
# exception called NoOffersApplied and display a custom error message.
# Define your own exception class by subclassing Exception.




'''class NoOffersApplied(Exception):
    pass


def cashback_calculator():
    try:
        spend = float(input("Enter total spend: "))
        offers = int(input("Enter number of offers applied: "))

        if offers == 0:
            raise NoOffersApplied("No offers were applied.")

        cashback = spend / offers
        print("Average cashback per offer:", cashback)

    except NoOffersApplied as e:
        print("Error:", e)


cashback_calculator()'''



# 4.Refactor the following buggy code to handle exceptions correctly so it never crashes and always
# prints 'Thank you for using the calculator' at the end, even if an exception occurs:
# def calculate_average_rating(total_rating, num_reviews):return total_rating / num_reviews
# print(calculate_average_rating(500, 0))



'''def calculate_average_rating(total_rating, num_reviews):
        try:
            return total_rating / num_reviews

        except ZeroDivisionError:
            print('Thank you for using the calculator')


print(calculate_average_rating(500, 0))'''


# 5.Write a function called safe_divide_for_zomato that takes two numbers (bill amount and number of people),
#  uses try, except, else, and finally to divide the bill and print the result, print a custom error if 
#  division by zero, and always print 'Split calculation done' at the end.

def safe_divide_for_zomato():
    try:
        amount = int(input("Enter a Bill amount:"))
        People = int(input("Enter the number of people:"))
        result = amount/People
    except ZeroDivisionError:
        print("Cannot divide by Zero")
    else:
        print("Result:",result)
    finally:
        print("succefully Completed")
safe_divide_for_zomato()