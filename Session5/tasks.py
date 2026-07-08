#  Task 1.Create a list called playlist_ids with 5 song IDs (as integers) that you might
#  see in a Spotify playlist, and print the list.
playlist_ids = [101,102,103,104,105]
print("playlist ids:",playlist_ids)




# Task 2.Add two more song IDs to your playlist_ids list using both append() and extend(), 
# then print the updated list.
# Hint: Use append() for a single ID and extend() for adding multiple IDs at once.
playlist_ids = [101,102,103,104,105]
playlist_ids.append(106)
print("playlist ids:",playlist_ids)
playlist_id2 = [101,102,103,104,105]
playlist_ids.extend(playlist_id2)
print("playlist ids:",playlist_ids)


#  Task 3.Simulate removing the last played song from your playlist_ids list using pop(),
#  and display the removed ID along with the remaining playlist.
playlist_ids = [101,102,103,104,105]
print(playlist_ids.pop())
print(playlist_ids)




# Task 4.Create a tuple called insta_filters with 4 Instagram filter names (as strings).
#  Try to change the first filter name and observe what error you get.
# Hint:Tuples are immutable. Note down the error message.
insta_filters = ("flicker flashing vid","Asthetic blur","film burn","Glitch")
# insta_filters[0] = "black"
print("Error message: TypeError: 'tuple' object does not support item assignment")



# Task 5.Write a short Python script that takes a scenario (like a list of recent Zomato orders 
# vs a tuple of fixed IPL team names) and prints which one should use a list and 
# which should use a tuple, explaining your choice in a comment.

# List: Recent Zomato orders (can change by adding/removing orders)
zomato_orders = ["Pizza", "Burger", "Biryani"]

# Tuple: Fixed IPL team names (these do not change)
ipl_teams = (
    "CSK", "MI", "RCB", "KKR", "GT",
    "RR", "PBKS", "DC", "LSG", "SRH"
)

print("Recent Zomato Orders:", zomato_orders)
print("Use: List")
# A list is used because orders can be added, removed, or updated.

print("\nIPL Team Names:", ipl_teams)
print("Use: Tuple")
# A tuple is used because the team names are fixed and should not be modified.