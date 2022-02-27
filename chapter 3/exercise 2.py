#program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
Hours=input("Enter Hours:")
Rate=input("Enter Rate:")

try:
    hours=float(Hours)
    rate=float(Rate)
    pay=hours*rate
    print(pay)
except:
    print("Error, please enter numeric input")