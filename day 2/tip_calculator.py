print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip_per = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip = total_bill * (tip_per / 100)
bill = total_bill + tip
solo_bill = bill / people
print(f"Each person pay {round(solo_bill, 2)}$" )