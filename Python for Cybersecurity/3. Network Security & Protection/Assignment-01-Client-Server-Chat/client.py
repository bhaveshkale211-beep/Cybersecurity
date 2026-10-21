import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connecting to server...")
client_socket.connect((HOST, PORT))

print("\nClient started")
print("Server IP Address:", HOST)
print("Server Port Number:", PORT)
print("Connection Status: Connected")

for i in range(3):
    message = input("\nClient: ")
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print("Server:", response)

print("\nChat completed. Closing connection.")

client_socket.close()