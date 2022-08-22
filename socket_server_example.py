import socket
import threading

MAX_MESSAGE_LENGTH = 1024


class Server:
    def __init__(self):
        HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
        self.listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listening_socket.bind((HOST, PORT))
        self.client_sockets = []
        self.should_listen = True

    def receiving_from_client(self, index):
        while self.should_listen:
            print('Received message.')
            message = self.client_sockets[index].recv(MAX_MESSAGE_LENGTH)

            # If message is None meaning the client disconnected.
            if message is None:
                del self.client_sockets[index]
                break
            else:
                for socket in self.client_sockets:
                    socket.sendall(message)

    def listen(self):
        print('Started listening')
        # I'm calling this function only once
        # this calling means this is a listening socket.
        self.listening_socket.listen()
        while True:
            new_socket, addr = self.listening_socket.accept()
            print('New client added : {}'.format(addr))

            self.client_sockets.append(new_socket)
            index_of_socket = len(self.client_sockets) - 1

            # I'm opening here a thread that is going to receive messages from the client
            # all the time until the connection is closed.
            t = threading.Thread(target=self.receiving_from_client, args=(index_of_socket,))
            t.start()


if __name__ == '__main__':
    server = Server()
    server.listen()
