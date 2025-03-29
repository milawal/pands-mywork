# Weekday Detector
# This program outputs whether or not today is a weekday
# Author: Michael Lawal
# Reference: Python datetime module for retrieving the current day of the week.

import datetime

# Get the current date and day of the week
today = datetime.datetime.now()

# Check if today is a weekday (0 = Monday, 6 = Sunday)
if today.weekday() < 5:
    print("Today is a weekday.")
else:
    print("Today is not a weekday.")
