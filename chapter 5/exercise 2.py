count = 0
keepgoing = True
nums = []
while keepgoing:
  line = input ('Enter a number:')
  try:
     line = float(line)
     nums.append(line)
     count = count + 1 
  except:
    if line == 'Done' or line == 'done':
      break
    else:
      print ('Invalid Input')
      continue

smallest = min(nums)
largest = max(nums)
print(largest, smallest)