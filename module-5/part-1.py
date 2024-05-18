'''
Pseudo-code:

START

SET total_rainfall = 0

GET number_of_years with a value greater than 0

FOR year = 1 TO number_of_years
    FOR month = 1 TO 12
        GET rainfall
        total_rainfall = total_rainfall + rainfall
    NEXT month
NEXT year

PRINT "Number of months: ", years * 12
PRINT "Total inches of rainfall:", total_rainfall
PRINT "Average Rainfall per Month: ", total_rainfall / (years * 12)

END

'''

# Initialize total rainfall to 0
total_rainfall = 0
years = 0

#Get positive valued number of years from the user
while years <= 0:
    # Ask the user for the number of years
    years = int(input("\nEnter the number of years: "))

# For each year from 1 to number of years
for year in range(1, years + 1):
    # For each month from 1 to 12
    for month in range(1, 13):
        # Ask the user for the inches of rainfall for that month
        monthly_rainfall = float(input(f"Enter the inches of rainfall for year {year} month {month}: "))
        # Add the rainfall for that month to the total rainfall
        total_rainfall += monthly_rainfall

# Calculate the total number of months
total_months = years * 12

# Calculate the average rainfall per month
average_rainfall = total_rainfall / total_months

# Display the total number of months, the total inches of rainfall, and the average rainfall per month
print(f"\nNumber of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month: {average_rainfall:.2f}")
