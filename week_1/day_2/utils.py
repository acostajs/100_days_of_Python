# This is the utils functions for day 2 of 100 days of Python

def calculate_tip(bill, tip_percentage, people):
    tip = (bill * tip_percentage) / people
    return round(tip, 2)

def calculate_total_bill(bill, tip_percentage, people):
    total_bill = ((bill * tip_percentage) + bill) / people
    return round(total_bill, 2) 
