# leap_year.py

def is_leap_year(year: int) -> bool:
    """
    Check if a given year is a leap year.
    Returns True if leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


if __name__ == "__main__":
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year ✅")
        else:
            print(f"{year} is not a leap year ❌")
    except ValueError:
        print("Please enter a valid number.")
