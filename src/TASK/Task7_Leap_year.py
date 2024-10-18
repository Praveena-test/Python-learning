# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

year = int(input("Enter a year to check if it is leap year or not\n"))
if year%4==0 and year%100 != 0 or year%400==0:
    print(f"Given year {year} is leap year")
else:
    print(f"Given year {year} is 'NOT' leap year")

