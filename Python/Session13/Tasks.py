#1.Write a recursive function in Python called print_playlist_songs(songs) that takes a list of song
#  names (like a Spotify playlist) and prints each song name one by one using recursion

l1 = ['Perfect','Arcade','Blinding Lights','Espresso','Levitating']

def print_playlist_songs(songs):
    if len(songs) ==0 :
        return
    print(songs[0])
    print_playlist_songs(songs[1:])
print_playlist_songs(l1)


'''
def print_playlist_songs(songs):
    if len(songs)==0:
        for i in songs:
            return''' 
        


# 2.Create a recursive function count_unread_messages(messages) that takes a nested dictionary 
# representing WhatsApp chat groups and subgroups, and returns the total number of unread messages 
# across all groups.Hint:Each group can have a 'count' key for unread messages and a 'subgroups'
#  key with a list of more groups.

'''def count_unread_messages(messages):
    groups = {
        subgroups = {

        }
    }'''





'''3.Given the following code, identify which variables are local and which are global, and explain what will be printed when you call outer() and then print(x) at the end:<br><br>```python
x = 'global'
def outer():
x = 'outer'
def inner():
nonlocal x
x = 'inner'
inner()
print('Inside outer:', x)
outer()
print('Outside:', x)
```<br><br><em><strong>Hint:</strong> Focus on the scope of x inside and outside the functions.</em>
4.Build a recursive function format_number_short(n) that takes a number (like a follower count on 
Instagram or YouTube) and returns it as a string in short format: 1500 as '1.5K', 1200000 as
'1.2M', 500 as '500'.'''