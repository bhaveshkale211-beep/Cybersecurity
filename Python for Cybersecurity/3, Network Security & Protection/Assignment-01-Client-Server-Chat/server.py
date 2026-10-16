import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server started")
print("IP Address:", HOST)
print("Port Number:", PORT)
print("Waiting for client connection...")

connection, address = server_socket.accept()

print("\nClient connected!")
print("Client IP Address:", address[0])
print("Client Port:", address[1])
print("Connection Status: Connected")

for i in range(3):
    message = connection.recv(1024).decode()

    if not message:
        break

    print("\nClient:", message)

    response = input("Server: ")
    connection.send(response.encode())

print("\nChat completed. Closing connection.")

connection.close()
server_socket.close()