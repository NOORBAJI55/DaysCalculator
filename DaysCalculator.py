from datetime import datetime

print("enter month date year seperated by '/'")
def calculate_days_between_dates():
    start_date = input("Enter the start date (MM/DD/YYYY): ")
    end_date = input("Enter the end date (MM/DD/YYYY): ")

    start_date = datetime.strptime(start_date, "%m/%d/%Y")
    end_date = datetime.strptime(end_date, "%m/%d/%Y")

    days_between = (end_date - start_date).days

    print(f"There are {days_between} days between {start_date.strftime('%B %d, %Y')} and {end_date.strftime('%B %d, %Y')}.")

calculate_days_between_dates()
