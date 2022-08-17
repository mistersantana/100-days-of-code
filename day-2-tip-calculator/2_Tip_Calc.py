#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


print("Welcome to the tip calculator!")
bill_amount = float(input("What was the total bill? $"))
tip_amount = int(input("How much would you like to tip? 10, 12, or 15? "))
people_amount = int(input("How many people to split the bill? "))

tip_percent = tip_amount / 100
full_tip = bill_amount * tip_percent
full_bill = bill_amount + full_tip
full_people_amount = full_bill / people_amount

full_total = round(full_people_amount, 2)

print(F"Each person should pay: ${full_total}")