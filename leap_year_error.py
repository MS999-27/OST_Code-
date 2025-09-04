# leap_year_error.py
# This version includes an intentional error to demonstrate a NameError.

def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, else False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


if __name__ == "__main__":
    year = int(input("Enter a year: "))
    # INTENTIONAL ERROR BELOW: misspelled function name -> NameError
    if is_leap_yaer(year):  # NameError: name 'is_leap_yaer' is not defined
        print(f"{year} is a leap year ✅")
    else:
        print(f"{year} is not a leap year ❌")
