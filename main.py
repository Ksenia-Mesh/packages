from application import salary
print('Done salary')
from db import people
print('Done people')
from datetime import datetime, date, time

Now_date = datetime.today()
print(f"Local Date: {Now_date}")


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
print('Done')