print("Welcome to the tip calculator!.")
bill=float(input("What was the total bill? $ \n"))
tip=int(input("What percentage tip would u like to give ? 10,12,15 \n"))
people=int(input("How many people to spilt the bill ? \n"))
tip_as_percent = tip/100
total_tip = tip_as_percent*bill
total_bill = total_tip + bill
bill_per_person=bill/people
final_amount=round(bill_per_person,2)
print(f"Each person should pay ${fin
