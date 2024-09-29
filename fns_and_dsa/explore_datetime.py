# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
    current_date = datetime.now()  # Get current date
    future_date = current_date + timedelta(days=days_to_add)  # Calculate future date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Calculate future date based on user input
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)
