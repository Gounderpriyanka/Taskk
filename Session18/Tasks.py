#1.Use re.findall() to extract all valid phone numbers from a given string in the format 
#'+91-XXXXXXXXXX' (e.g., '+91-9876543210'). Print the list of found numbers.

'''import  re 

text = "Contact me at +91-9876543210 or +91-9123456789. Invalid: 9876543210"
numbers = re.findall(r'\+91-\d{10}',text)
print(numbers)

'''
# 2.Write a Python function using re.search() that checks if a string contains a valid date in the 
# format 'DD/MM/YYYY'. The function should return True if a date is found, otherwise False.

'''import re
def check_date(text):
    d = r'\d{2}/\d{2}/\d{4}'

    if re.search(d,text):
        return True
    else:
        return False
print(check_date("my birthday is 04/09/2005"))'''



# 3.Given a block of text containing multiple prices (like 'Rs. 299', 'Rs. 1500', etc.), use re.findall() to extract all the 
# numeric price values as integers and print their sum.Hint:Look for patterns like 'Rs. ' 
# followed by one or more digits.

'''import re
text = "I bought a shirt for Rs. 299, shoes for Rs. 1500 and a bag for Rs. 750."

prices = re.findall(r'Rs\. \d+',text)
print(prices)

-'''





#4.Use re.sub() to replace all email addresses in a string with '[hidden email]' and print the 
# modified string.Do not use any external libraries except re.

'''import re
text = "My email is priyanka@gmail.com and you can also contact me at test@example.com"

result = re.sub(r'\w+@\w+\.\w+', '[hidden email]', text)

print(result)'''

# 5.Download a sample Instagram comments text file (or create your own with at least 10 lines),
# then write a Python script to extract all valid Instagram usernames (pattern: starts with '@', followed by letters,
# numbers, underscores, minimum 3 characters) using re.findall() and print the unique usernames.

