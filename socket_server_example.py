import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
# The maximum is 65,535 (2^16 -1)

# I'm creating here a socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding this socket to a specific port.
s.bind((HOST, PORT))

# Start listening to incoming requests.
s.listen()

print('Im starting to listen please connect me')

# Blocking function meaning until a client is going to connect to the server
# I'm going to be stuck here.

conn, addr = s.accept()

with conn:
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)

s.close()
