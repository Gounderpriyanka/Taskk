"""
Task 3.Create a script that asks the user to input their cricket score as a string, converts it to an int, and 
prints 'Half-century!' if the score is 50 or more, otherwise prints 'Keep going!'.
<br><br><em><strong>Constraint:</strong> Use input(), int(), and if-else.</em>
"""

cricket_score = input("Enter the cricket score:")
if int(cricket_score)>=50:
    print("Half-century!")
else:
    print("Keep going!")