import socket
import threading

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
MAX_MESSAGE_LENGTH = 1024


class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST, PORT))
        t1 = threading.Thread(target=self.send)
        self.name = 'Bad Guy'

        t1.start()
        self.receive()
        self.close()

    def send(self):
        print('Starting to send shit.')
        while True:
            message = '\n' + self.name + ' : ' + input('Next Message: ') + '\n'
            self.socket.sendall(message.encode('utf-8'))

    def receive(self):
        print('Starting to listen.')
        while True:
            message = self.socket.recv(MAX_MESSAGE_LENGTH)
            if message is None:
                print('OH NO IM DEAD')
                break
            print(message.decode('utf-8'))

    def close(self):
        print('This is the end.')
        self.socket.close()


if __name__ == '__main__':
    client = Client()
