#1.Write a recursive function in Python called print_playlist_songs(songs) that takes a list of song
#  names (like a Spotify playlist) and prints each song name one by one using recursion

l1 = ['Perfect','Arcade','Blinding Lights','Espresso','Levitating']

'''def print_playlist_songs(songs):
    if len(songs) ==0 :
        return
    print(songs[0])
    print_playlist_songs(songs[1:])
print_playlist_songs(l1)'''


# Create a recursive function count_unread_messages(messages) that takes a nested dictionary representing
# WhatsApp chat groups and subgroups, and returns the total number of unread messages across all groups.
# Each group can have a 'count' key for unread messages and a 'subgroups' key with a list of more groups.


def count_unread_messages(messages):
    total = messages["count"]

    if "subgroups" in messages:
        for group in messages["subgroups"]:
            total += count_unread_messages(group)

    return total


messages = {
    "count": 5,
    "subgroups": [
        {"count": 3},
        {
            "count": 2,
            "subgroups": [
                {"count": 4}
            ]
        }
    ]
}

print("Total unread messages:", count_unread_messages(messages))


# 3.Given the following code, identify which variables are local and which are global, 
# and explain what will be printed when you call outer() and then print(x) at the
#  end:python
# x = 'global'
# def outer():
# x = 'outer'
# def inner():
# nonlocal x
# x = 'inner'
# inner()
# print('Inside outer:', x)
# outer()
# print('Outside:', x)
# Focus on the scope of x inside and outside the functions.

x = 'global'
def outer():
    x = 'outer'
    def inner():
        nonlocal x
        x = 'inner'
    inner()
    print("Inside outer:",x)
outer()
print("Outside:",x)





# 4.Build a recursive function format_number_short(n) that takes a number (like a follower count on 
# Instagram or YouTube) and returns it as a string in short format: 1500 as '1.5K', 1200000 as
# '1.2M', 500 as '500'.

def format_number_short(n, index=0):
    l1 = ['', 'K', 'M', 'B', 'T']
    
    # Base case: number is small enough to display as-is
    if n < 1000:
        n = int(n * 10) / 10   # keep 1 decimal place, no rounding
        if n == int(n):
            n = int(n)
        return f"{n}{l1[index]}"
    
    # Recursive case: shrink number, move to next suffix
    return format_number_short(n / 1000, index + 1)


# Test cases
print(format_number_short(500))         # 500
print(format_number_short(1500))        # 1.5K
print(format_number_short(1200000))     # 1.2M
print(format_number_short(2500000000))  # 2.5B