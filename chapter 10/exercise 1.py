import re

count = 0                               # Initialize variables

input_exp = input('Enter a regular expression: ')
reg_exp = str(input_exp)                # Regular Expressions are strings
fname = 'mbox.txt'
fhand = open(fname)

for line in fhand:
    line = line.rstrip()

    # Only counts if something was found
    if re.findall(reg_exp, line) != []:
        count += 1

print(fname + ' had ' + str(count) + ' lines that matched ' + reg_exp)