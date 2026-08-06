#1.Write a lambda function to convert a list of song titles from Spotify to 
# all lowercase letters and use map() to apply it to ['Shape Of You', 'Blinding Lights',
#  'Levitating', 'Senorita'], printing the cleaned list.

'''songs = ['Shape Of You', 'Blinding Lights','Levitating', 'Senorita']
result = list(map(lambda a : a.lower(),songs))
print(result)'''

#2.Given a list of Zomato restaurant ratings [4.2, 3.8, 4.5, 2.9, 3.5],
#  use filter() with a lambda to find and print only the restaurants with 
# ratings above 4.0.

'''rating = [4.2, 3.8, 4.5, 2.9, 3.5]
result = list(filter(lambda x: x>4.0,rating ))
print(result)'''

# 3.Use reduce() from functools to calculate the total price of items in a
#  Flipkart shopping cart: [499, 1299, 299, 799]. Print the final total.
# Hint:Import reduce from functools and use a lambda to sum two numbers.

'''from functools import reduce
cart = [499,1299,299,799]
result = reduce(lambda x,y: x+y,cart)
print(result)'''

#4.Create a function format_followers that takes a number and returns it in 'K' or 'M' format
# (e.g., 1500 → '1.5K', 1200000 → '1.2M'), then use map() to apply it to a list of follower 
# counts: [950, 1500, 25000, 1200000].

'''def format_followers(numbers):
    if numbers>=1000000:
        return f"{numbers/1000000}M"
    elif  numbers>=1000:
        return f"{numbers/1000}K"
    else:
        return numbers
    
l1 = [950,1500,25000,1200000]
result = list(map(format_followers,l1 ))
print(result)'''

#5.Use an AI tool like ChatGPT or Copilot to generate a lambda function that filters out all
#  odd numbers from a list of IPL scores [101, 98, 120, 77, 88], then test the code in your 
# Python environment and paste the working code here.

l1 = [101,98,120,77,88]
result = list(filter(lambda x : x%2==0,l1))
print(result)