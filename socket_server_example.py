import socket
import threading

MAX_MESSAGE_LENGTH = 1024


class Server:
    def __init__(self):
        HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
        self.listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listening_socket.bind((HOST, PORT))
        self.client_socket = None
        self.connected_to_client = False

    def send_to_client(self, message):
        # If this is False it throws an exception.
        assert self.connected_to_client
        self.client_socket.sendall(message.encode('utf-8'))

    def receiving_from_client(self):
        while self.connected_to_client:
            message = self.client_socket.recv(MAX_MESSAGE_LENGTH).decode('utf-8')
            if message is None:
                self.connected_to_client = False
            else:
                print('CLIENT: ' + message)

    def listen(self):
        self.listening_socket.listen()
        self.client_socket, addr = self.listening_socket.accept()
        self.connected_to_client = True

        # I'm opening here a thread that is going to receive messages from the client
        # all the time until the connection is closed.
        t = threading.Thread(target=self.receiving_from_client)
        t.start()

    def close(self):
        self.client_socket.close()
        self.listening_socket.close()


if __name__ == '__main__':
    server = Server()
    server.listen()
    while server.connected_to_client:
        message = input('Please enter a message to send to the client: ')
        server.send_to_client(message)
    server.close()
