file_name = input("Enter a file name: ")
lines = [line.strip('\n') for line in open(file_name, 'r')
         if line.startswith("From ")]
who_from_dict = {}

for line in lines:
    line = line.split()
    email = line[1]
    domain = email.split("@")[1]
    who_from_dict[domain] = who_from_dict.get(domain, 0) + 1

print (who_from_dict)