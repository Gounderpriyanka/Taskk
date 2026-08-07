#1.Create a text file named playlist.txt and write the names of 5 songs you listened to this week, 
# each on a new line using Python's open() function in write mode.

'''with open ("playlist.txt",'w') as f:
    f.write("Perfect\n")
    f.write("Photograph\n")
    f.write("Yellow\n")
    f.write("Espresso\n")

    f.close()'''


#2.Read the playlist.txt file you created and display each song name
#  in uppercase letters using Python.

with open("playlist.txt",'r') as f:
    content = f.readlines()
    for i in content:
        print(i.upper())

#3.Download a sample CSV file of IPL match scores (you can create your own with
#columns: match_id, team1, team2, winner) and write a Python script to read the file
# and print the winner of each match using the csv module.

import csv as cv

with open("IPL_Match_S(core.csv",'w') as file:
    writer = cv.writer(file)
    writer.writerow(['match_id','team1','team2','winner'])
    writer.writerow(["101","Chennai Super Kings","Mumbai Indians","Chennai Super Kings"])
    writer.writerow(["102","Royal Challengers Bengaluru","Kolkata Knight Riders","Kolkata Knight Riders"])
    writer.writerow(["103","Gujarat Titans","Rajasthan Royals","Gujarat Titans"])
    writer.writerow(["104","Sunrisers Hyderabad","Punjab Kings","Sunrisers Hyderabad"])
    writer.writerow(["105","Delhi Capitals","Lucknow Super Giants","Lucknow Super Giants"])

    file.close()

 
 
 
 
'''
 4.Find a public JSON file of trending movies (or create your own movies.json with at least 3 movie objects containing title, year, and rating), then use the json module in Python to load the file and print the title and rating of each movie.
5.Use the pathlib module to check if a file called 'my_fav_apps.json' exists in your current directory, and if not, create it and write a JSON array of your top 3 mobile apps (e.g., Instagram, Zomato, Paytm) with their names and categories.<br><br><em><strong>Hint:</strong> Use Path('my_fav_apps.json').exists() to check for the file, and json.dump() to write the data.</em>'''