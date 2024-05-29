'''
Pseudo-code:

# Create a dictionary to store course numbers and room numbers
# Create a dictionary to store course numbers and instructor names
# Create a dictionary to store course numbers and meeting times

# Prompt the user to enter a course number
# Read the user input and store it in a variable

# Check if the entered course number exists in all three dictionaries
    # If the course number is found in all dictionaries
        # Retrieve the room number, instructor, and meeting time for the entered course
        # Display the course information
    # Else
        # Display an error message indicating that the course number is invalid

'''


# Create a dictionary to store course numbers and room numbers
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# Create a dictionary to store course numbers and instructor names
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Create a dictionary to store course numbers and meeting times
meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Prompt the user to enter a course number
course_number = input("Enter a course number: ")

# Check if the entered course number exists in the dictionaries
if course_number in room_numbers and course_number in instructors and course_number in meeting_times:
    # Retrieve the room number, instructor, and meeting time for the entered course
    room_num = room_numbers[course_number]
    instructor = instructors[course_number]
    meeting_time = meeting_times[course_number]

    # Display the course information
    print(f"\nCourse: {course_number}")
    print(f"Room Number: {room_num}")
    print(f"Instructor: {instructor}")
    print(f"Meeting Time: {meeting_time}\n")
else:
    # If the course number is not found, display an error message
    print("\nInvalid course number entered.\n")