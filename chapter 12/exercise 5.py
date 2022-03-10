import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
total_bdata = b''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break

    total_bdata = total_bdata + data
    
total_bdata = total_bdata.split(b"\r\n\r\n")
total_bdata = total_bdata [1]
total_bdata = total_bdata.decode()
print (total_bdata)

mysock.close()