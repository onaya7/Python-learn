hours = int(input('Enter hours:'))
rate =  int(input('Enter rate:'))


def computepay(hours,rate):
 pay =('Your pay this month:' + str((hours + hours/2) * rate))
 return pay 
x = computepay(hours,rate)
print(x)
