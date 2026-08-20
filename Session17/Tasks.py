#1.Create a Python script that imports the math module and uses math.sqrt() to calculate and 
# print the square root of 225.

'''import math

print(math.sqrt(225))'''

#2.Write a script that uses the os module to create a new folder named 'MyDownloads' in your current 
# working directory, then print the absolute path of the new folder.

'''import os

folder_name = "MyDownloads"
current_dir = os.getcwd()

new_folder_path = os.path.join(current_dir, folder_name)
os.makedirs(new_folder_path, exist_ok=True)
print("New folder created at:", os.path.abspath(new_folder_path))'''



#3.Use the datetime module to get the current date and time, then format and print it as 'DD-MM-YYYY HH:MM:SS',
#  similar to how WhatsApp shows message timestamps.Use strftime() to format the output.

'''import datetime as dt

today = dt.datetime.today().strftime("%d-%m-%Y %H:%M:%S")
print(today)'''

#4.Create a custom Python module called playlist_utils.py with a function add_song(playlist, song) that
#  adds a song to a list. Import this module in another script and use it to add three songs to a playlist,
#  then print the final playlist.





# 5.Set up a new virtual environment using venv, activate it, and install the 'requests' package using pip.
#  Write a short script that imports requests and prints the version installed.Use 'python -m venv venv_folder',
#    then 'pip install requests'.

'''Step 1: Creating new virtual environment
  python -m venv venv_folder

Step 2: Activate the Virtual Environment
  venv_folder\Scripts\activate

Step 3: Install the requests Package
  pip install requests

Step 4: Python Script

import requests
print("Requests version:", requests.__version__)'''