print("Welcome to tip calculator")

bill = float(input("Please provide bill ammount "))

persons = int(input("How many people are paying for this bill? "))

tip_ammount = int(input("How much % of tip do you want to give? "))

bill_per_person = (bill/persons) * (tip_ammount * (tip_ammount/100))

final_bill_per_person = "{:.2f}".format(bill_per_person)

print(f"Total for one person with tip is {final_bill_per_person}$")