# Task 1.Create a Python dictionary called insta_followers that stores the number of followers 
# for 5 Instagram influencers (use their usernames as keys and follower counts as values).
#  Print the dictionary.

insta_followers = {
    "viratkohli": 272000000,
    "shraddhakapoor": 95000000,
    "aliaabhatt": 87000000,
    "narendramodi": 108000000,
    "priyankachopra": 93000000
}
print(insta_followers)

# Task 2.Add a new influencer to your insta_followers dictionary and update the follower count 
# for one existing influencer. Then, delete one influencer from the dictionary and 
# print the updated dictionary.

insta_followers["kyliejenner"] = 393000000
print(insta_followers)
insta_followers.pop("narendramodi")
print(insta_followers)

# Task Given a dictionary called food_prices with 5 Zomato food items as keys and their prices 
# as values, write code to display all items that cost more than ₹200.

food_prices = {"Pizza":500,
               "Tart" : 200,
               "Burger": 199,
               "French fries": 160,
               "choppati" : 150
               }
for i in food_prices:
    if food_prices[i] > 200:
        print(i , ":",food_prices[i])


# Task 4.Create two sets: flipkart_users and myntra_users, each containing 5 unique usernames.
#  Find and print the set of users who have accounts on both platforms using set intersection.
flipkart_users = {"abc","def","ghi","riya","Sam"}
myntra_users = {"Sam","riya","john","som","siya"}
print(flipkart_users.intersection(myntra_users))


# Task 5.Write a function get_unique_artists(spotify_playlist1, spotify_playlist2) that
#  takes two sets of artist names and returns a set of all unique artists across 
# both playlists (set union).Hint:Use the union() method or the | operator for sets.

def get_unique_artists(spotify_playlist1, spotify_playlist2):

    return spotify_playlist1.union(spotify_playlist2)

a = {"Justin Bieber","Rihanna","Taylor Swift","Bruno Mars"}
b = {"Bruno Mars","Lady Gaga","Arijit Singh","Shreya Ghoshal"}

print(get_unique_artists(a,b))