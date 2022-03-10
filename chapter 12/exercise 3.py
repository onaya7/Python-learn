import urllib.request, urllib.parse, urllib.error
url = input ('Please enter a URL to retrieve data:')
fhand = urllib.request.urlopen(url)
counts = dict()
data_total = ''
for line in fhand:
    words = line.decode()
    data_total = data_total + words
print (data_total[:3000])
print (len(data_total[:3000]))