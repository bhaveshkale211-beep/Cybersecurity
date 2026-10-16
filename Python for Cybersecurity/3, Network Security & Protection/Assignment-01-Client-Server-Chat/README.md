# Assignment 01 — Client-Server Chat Application Using Python Sockets

My first go at network programming. Two small Python programs, a server and a client, connect to each other over TCP, swap three messages, and then both close the connection. Everything runs on my own computer, but it's the same mechanism real network software uses to talk between machines.

## The scenario

As a junior cybersecurity analyst, build a basic communication system between two systems. The server waits for a connection, the client connects and sends messages typed by the user, and the server answers each one.

## How the two scripts line up

| Step | Server (`server.py`) | Client (`client.py`) |
|---|---|---|
| 1 | Creates a TCP socket | Creates a TCP socket |
| 2 | `bind()` to `127.0.0.1`, port `5000` | |
| 3 | `listen()` for incoming connections | |
| 4 | `accept()` and waits for a client | `connect()` to `127.0.0.1`, port `5000` |
| 5 | `recv()` a message, shows it, then `send()`s a reply | `send()` a message, then `recv()` the reply |
| 6 | Repeats step 5 three times | Repeats step 5 three times |
| 7 | Closes the connection and the socket | Closes the socket |

Some details that made it click:

- **`127.0.0.1` is localhost**, the computer talking to itself. That's why both programs can run on one machine and still behave the way they would on two separate ones.
- **Port 5000 is fixed on the server.** The client's own port is picked automatically by the operating system. It was `53763` in my run, and the server prints it when the client connects. It's different on every run.
- **Sockets send bytes, not text.** That's why the scripts call `.encode()` before sending and `.decode()` after receiving.
- **`SOCK_STREAM` is what makes the socket TCP**, and `AF_INET` means IPv4.

## The code

The full scripts are [`server.py`](./server.py) and [`client.py`](./client.py). The important parts:

**Server**

```python
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

connection, address = server_socket.accept()

for i in range(3):
    message = connection.recv(1024).decode()

    if not message:
        break

    print("\nClient:", message)

    response = input("Server: ")
    connection.send(response.encode())
```

**Client**

```python
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

for i in range(3):
    message = input("\nClient: ")
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print("Server:", response)
```

## Running it

Two terminals, server first, then client:

```
python server.py
python client.py
```

### 1. Server started, then a client connects

`ls` shows the two scripts (810 and 587 bytes). Then `python server.py` prints the IP and port and sits at `Waiting for client connection...`. Once the client connects, the server reports the client's IP (`127.0.0.1`) and its port (`53763`).

![Server started and client connected](./screenshots/01-server-started-and-client-connected.png)

### 2. The client side

`python client.py` connects and shows the server's IP, port and `Connection Status: Connected`, then waits at the `Client:` prompt for the first message.

![Client connected to the server](./screenshots/02-client-connected-to-server.png)

### 3. Both sides together

Server on the left (PowerShell), client on the right (VS Code terminal). Three messages go from the client to the server, and three replies come back. The client port is `53763` here too, the same as in the first screenshot, so it's one continuous run.

![Server and client chat side by side](./screenshots/03-server-and-client-chat-side-by-side.png)

### 4. Ending

After the third exchange both programs print `Chat completed. Closing connection.` and return to the prompt.

![Chat completed](./screenshots/04-chat-completed-connection-closed.png)

## Things worth knowing

- **Start the server first.** If the client runs while nothing is listening on port 5000, it stops straight away with a `ConnectionRefusedError`.
- **The server's replies aren't automatic.** `input("Server: ")` waits for a person to type, and the client just waits until they do. So it's really two people chatting through two terminals, not a bot answering.
- **It's exactly three exchanges.** Both loops use `range(3)`, then both sides close.
- **Only one client is served.** The server calls `accept()` once and shuts down after the chat.
- **An early disconnect is handled.** If the client closes without sending anything, `recv()` returns an empty result, `if not message: break` ends the loop, and the server closes cleanly.
- **`recv(1024)` doesn't mean "one message".** TCP is a stream of bytes with no message boundaries. Testing with a single 3000-byte `send()` showed it arriving on the server as three separate "messages" of 1024, 1024 and 952 bytes. It works here because every message is short and each side waits for its turn.
- **Nothing is encrypted.** The messages travel as plain bytes. On localhost that doesn't matter, but between two real machines anyone who could capture the traffic (like in the Wireshark assignment) could read the chat. It's the same plain-text problem as Telnet. Wrapping the socket in TLS with Python's `ssl` module would be the next step.

## Files in this folder

| File | What it is |
|---|---|
| `server.py` | The server |
| `client.py` | The client |
| `screenshots/` | Screenshots of both programs running |
