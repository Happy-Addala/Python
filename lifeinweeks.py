# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
age_as_int = int(age)
# 🚨 Don't change the code above 👆
year_remaining = 90 - age_as_int
days_remaining = year_remaining * 365
weeks_remaining = year_remaining * 52
months_remaining = year_remaining * 12
#Write your code below this line 👇
print(f"You have {days_remaining} days,  {weeks_remaining} weeks, and {months_remaining} months left")
