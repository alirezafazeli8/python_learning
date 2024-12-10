import socket

HOST_IP = "localhost"
HOST_PORT = 8826

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the ip
client.connect((HOST_IP, HOST_PORT))
client.send("Hi Alireza ! ".encode("utf-8"))
print(client.recv(1024).decode("utf-8"))
