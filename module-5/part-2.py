'''
Pseudo-code:
Note: This pseudo code (and corresponding source code) is written as per the problem statement. 
The problem statement has a gap, wherein it doesn't explicitly specify what happens when odd number of books are purchased.
I have the assumption that the even number of the books is a range boundry condition (rather than the exact number of books).

START

GET num_books_purchased

IF num_books_purchased < 2 THEN
    points_awarded = 0
ELSE IF 2 <= num_books_purchased <= 3 THEN
    points_awarded = 5
ELSE IF 4 <= num_books_purchased <= 5 THEN
    points_awarded = 15
ELSE IF 6 <= num_books_purchased <= 7 THEN
    points_awarded = 30
ELSE IF num_books_purchased >= 8 THEN
    points_awarded = 60

PRINT points_awarded

END
'''

# Ask the user to enter the number of books purchased
num_books_purchased = int(input("\nEnter the number of books you purchased this month: "))

# Initialize the points awarded to 0
points_awarded = 0

# Determine the points awarded based on the number of books purchased
if num_books_purchased < 2:  # If 0 or 1 book was purchased
    points_awarded = 0
elif 2 <= num_books_purchased <= 3:  # If 2-3 books were purchased
    points_awarded = 5
elif 4 <= num_books_purchased <= 5:  # If 4-5 books were purchased
    points_awarded = 15
elif 6 <= num_books_purchased <= 7:  # If 6-7 books were purchased
    points_awarded = 30
elif num_books_purchased >= 8:  # If 8 or more books were purchased
    points_awarded = 60

# Display the points awarded
print(f"\nYou earned {points_awarded} points for purchasing {num_books_purchased} books.\n")