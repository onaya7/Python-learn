# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Hours=input("Enter Hours:")
Rate=input("Enter Rate:")
hours=float(Hours)
rate=float(Rate)
if hours <= 40:
    print(hours*rate)
elif hours > 40:
    print("Pay:",40*rate+(hours-40)*1.5*rate)