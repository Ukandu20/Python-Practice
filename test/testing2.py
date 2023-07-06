from datetime import datetime, timedelta

# Read the first date from the user
date1_str = input("Enter the first date (YYYY-MM-DD): ")

# Parse the date string and create a datetime object
date1 = datetime.strptime(date1_str, "%Y-%m-%d")

# Read the second date from the user
date2_str = input("Enter the second date (YYYY-MM-DD): ")

# Parse the date string and create a datetime object
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

# Calculate the number of days between the two dates
num_days = (date2 - date1).days

# Print the result
print(f"There are {num_days} days between {date1_str} and {date2_str}.")
