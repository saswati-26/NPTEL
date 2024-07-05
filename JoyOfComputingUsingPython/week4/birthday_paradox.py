import random
import datetime

# Generate random birthdays for a given number of people
def generate_birthday(n_people):
    birthdays = []
    for _ in range(n_people):
        year = random.randint(1900, 2020)
        month = random.randint(1, 12)
        if month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                day = random.randint(1, 29)
            else:
                day = random.randint(1, 28)
        elif month in [4, 6, 9, 11]:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)
        birthdays.append(datetime.date(year, month, day).timetuple().tm_yday)       #straight away gives the day of the year
    return sorted(birthdays)

# Run simulations to estimate the probability of the birthday paradox
n_people = int(input("Enter the number of people: "))
n_simulations = int(input("Enter the number of simulations: "))

count = 0
for _ in range(n_simulations):
    birthdays = generate_birthday(n_people)
    if len(birthdays) != len(set(birthdays)):
        count += 1

print(f"{count} no. of birthday paradox")
