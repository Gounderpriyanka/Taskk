#1.Write a recursive function in Python called print_playlist_songs(songs) that takes a list of song
#  names (like a Spotify playlist) and prints each song name one by one using recursion

l1 = ['Perfect','Arcade','Blinding Lights','Espresso','Levitating']

def print_playlist_songs(songs):
    for i in songs:
        return print(print_playlist_songs(songs))
print_playlist_songs(l1)