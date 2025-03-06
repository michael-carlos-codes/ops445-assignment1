#!/usr/bin/env pyth3
# Student ID: Michael Carlos

"""
Academic Honesty Declaration:
I confirm that I have completed this assignment by myself and have adhered to the academic integrity policies.

Assignment 1: Weekend Days Calculator

This script calculates the number of weekend days (Saturdays and Sundays) between two given dates.
The start and end dates are provided as command-line arguments in YYYY-MM-DD format. The script will
calculate the number of weekend days, regardless of the order of dates, and handle invalid input gracefully.

Usage:
    python3 assignment1.py 2023-05-01 2023-05-30
"""

import sys
from datetime import datetime, timedelta

def valid_date(date: str) -> bool:
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def count_weekend_days(start_date: str, end_date: str) -> int:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Ensure start is always earlier than end date
    if start > end:
        start, end = end, start

    count = 0
    current_date = start
    while current_date <= end:
        if current_date.weekday() == 5 or current_date.weekday() == 6:  # 5 = Saturday, 6 = Sunday
            count += 1
        current_date += timedelta(days=1)

    return count

def usage():
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

if len(sys.argv) != 3:
    usage()

start_date = sys.argv[1]
end_date = sys.argv[2]

# Validate the dates
if not valid_date(start_date) or not valid_date(end_date):
    usage()

# Calculate and print the result
weekend_days = count_weekend_days(start_date, end_date)
print(f"The period between {start_date} and {end_date} includes {weekend_days} weekend days.")

# Convert the string date into a datetime object for comparison
start = datetime.strptime(start_date, "%Y-%m-%d")

def count_weekend_days(start_date: str, end_date: str) -> int:
    """
    Counts the number of weekend days (Saturdays and Sundays) between two given dates.
    
    Args:
        start_date (str): The start date in YYYY-MM-DD format.
        end_date (str): The end date in YYYY-MM-DD format.
        
    Returns:
        int: The number of weekend days in the date range.
    """

