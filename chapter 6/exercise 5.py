import numbers


str = 'X-DSPAM-Confidence:0.8475'
start = str.find(':')
number=str[start+1:]
print(float(number))
