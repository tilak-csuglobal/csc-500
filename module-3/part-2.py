'''
Pseudo-code:

START

INPUT current_hours
WHILE current_hours < 0 OR current_hours > 23
    OUTPUT "Invalid hour. Please enter a value between 0 and 23."
    INPUT current_hours
END WHILE

INPUT current_minutes
WHILE current_minutes < 0 OR current_minutes > 59
    OUTPUT "Invalid minutes. Please enter a value between 0 and 59."
    INPUT current_minutes
END WHILE

INPUT wait_hours
INPUT wait_minutes

SET total_minutes = (current_hours * 60 + current_minutes) + (wait_hours * 60 + wait_minutes)
SET alarm_hours = total_minutes // 60 % 24
SET alarm_minutes = total_minutes % 60

OUTPUT alarm_hours
OUTPUT alarm_minutes

END
'''

# Ask the user for the current time (hours)
current_hours = int(input("Enter the current hour (0-23): "))

# Check if the entered hour is valid
while current_hours < 0 or current_hours > 23:
    print("Invalid hour. Please enter a value between 0 and 23.")
    current_hours = int(input("Enter the current hour (0-23): "))

# Ask the user for the current time (minutes)
current_minutes = int(input("Enter the current minutes (0-59): "))

# Check if the entered minutes are valid
while current_minutes < 0 or current_minutes > 59:
    print("Invalid minutes. Please enter a value between 0 and 59.")
    current_minutes = int(input("Enter the current minutes (0-59): "))

# Ask the user for the wait time (hours and minutes)
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))
wait_minutes = int(input("Enter the number of minutes to wait for the alarm: "))

# Calculate the time when the alarm will go off
total_minutes = (current_hours * 60 + current_minutes) + (wait_hours * 60 + wait_minutes)
alarm_hours = (total_minutes // 60) % 24
alarm_minutes = total_minutes % 60

# Display the time when the alarm will go off
print(f"The alarm will go off at {alarm_hours:02d}:{alarm_minutes:02d}")
