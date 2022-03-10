import socket
url = input ('Enter a URL to retrieve data:')
surl = url.split('/')

try:
    server = surl[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((str(server), 80))
    url = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    cmd = url.encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)  
        if len(data) < 1:
            break
        print(data.decode(),end='')
    
    mysock.close()

except:
    print ('Invalid URL')