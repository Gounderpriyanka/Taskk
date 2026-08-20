#1.Use iter() and next() to manually loop through a list of your 5 favorite food delivery apps
#  (like Zomato, Swiggy, Domino's, etc.) and print each app name one by one.

'''l1 = ["Zomato","Swiggy","Domino's","Uber Eats","EatSure"]
iter_apps = iter(l1)
for i in l1:
    print(next(iter_apps))'''

#2.Write a generator function called playlist_generator that takes a list of song names and yields each song
#  one at a time, simulating a Spotify playlist shuffle.

'''def playlist_generator(a):
    for i in a:
        yield i

songs = ["Shape of You", "Believer", "Perfect", "Havana"]

a = playlist_generator(songs)
for i in  a:
    print(i)'''



#3.Use enumerate() to print out the index and name of each item in a shopping cart list 
# (e.g., ['Pizza', 'Burger', 'Fries', 'Coke']) like Flipkart displays item numbers in your cart.

'''l1 = ["Pizza", "Burger", "Fries", "Coke"]
for i,j in enumerate(l1,start=1):
    print(i,j)
'''


#4.Given two lists — one with cricket team names and one with their IPL points — use zip() to pair
#  each team with its points and print them in the format: 'Team: Mumbai Indians, Points: 18'.


'''Teams = ["Mumbai Indians", "CSK", "RCB", "KKR"]
Points = [18, 16, 14, 20]
for i,j in (zip(Teams,Points)):
    print(i,j)'''



#5.Create a generator function called order_id_generator that yields a new order ID (starting from 1001) 
# each time it's called, similar to how Zomato or Swiggy generates unique order numbers.
#  Use the yield statement inside a loop to generate the next ID.



def order_id_generator():
    
    id = 1001
    while True:
        yield id
        id +=1

result = order_id_generator()
a = int(input("Number of IDs:"))
for i in range(a):
    print(next(result))



