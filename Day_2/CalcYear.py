
age = input("What is your current age? ")

day = int(365*90)

wekees = int(90*52)

months = int(90*12)

age_day = (int(age) * 365) - day

age_wekees = (int(age) * 52 ) - wekees

age_months = (int(age) * 12 ) - months


print(f"You have {age_day} days, {age_wekees} weeks, and {age_months} months left.")

