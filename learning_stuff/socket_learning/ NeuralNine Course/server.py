import socket

# HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_IP = "localhost"
HOST_PORT = 8826

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST_IP, HOST_PORT))
server.listen()


while True:
    # read the tcp request connection
    communication_socket, address = server.accept()
    print(f"Connected to {address}")

    # read the tcp request message
    message = communication_socket.recv(1024).decode("utf-8")
    print(f"Message From Client : {message}")

    # answer the tcp request
    communication_socket.send("I've Got Your Message".encode("utf-8"))
    communication_socket.close()
    print(f"communication with address {address} is closed ! ")
