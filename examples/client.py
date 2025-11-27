import socket

HOST = "localhost"
PORT = 12345

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        while True:
            text = input("> ")
            
            if (text == "exit"):
                break

            client_socket.send(text.encode())

            data = client_socket.recv(1024)
            if data:
                print(data.decode())

if __name__ == "__main__":
    main()
