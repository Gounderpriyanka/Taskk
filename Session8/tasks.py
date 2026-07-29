# 1.Create a Python script that uses a for loop to print the names of 5 favorite food delivery apps 
# (e.g., Zomato, Swiggy, etc.), one per line.

l1 = ["Zomato","Swiggy","QuickBite","Foodport","Fresh2Door"]
for i in l1:
    print(i)

# 2.Given a list of daily step counts for a week, use a while loop to find and print the first day
#  when you crossed 10,000 steps.Hint: Loop through the list and stop
#  as soon as you find a value greater than 10,000.

steps = [6500, 7800, 9200, 10500, 9800, 12000, 8500]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

i = 0
while i <len(steps):
    if steps[i]>10000:
        print("First day you crossed 10,000 steps: ",days[i])
        print("Steps:",steps[i])
        break
    i += 1

#3.Write a Python function that takes a list of IPL team names and prints only those teams
#  whose names are longer than 6 characters, skipping the rest using the continue statement.

teams = ["MI", "CSK", "Royal Challengers Bengaluru", "Sunrisers Hyderabad", "GT", "Punjab Kings", "KKR"]
i = 0
while i <len(teams):
    if len(teams[i])<=6:
        i += 1
        continue

    print(teams[i])
    i += 1

#4.You have a list of song durations (in seconds) from your Spotify playlist.
# Use a for loop with enumerate to print each song's position (starting from 1) and
#  its duration in the format: 'Song 1: 210 seconds'

durations = [210, 185, 240, 195, 220]


         

        
