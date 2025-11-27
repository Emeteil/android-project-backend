import socket

HOST = "localhost"
PORT = 12345

def main():    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        client_socket, address = server_socket.accept()
        print(f"Клиент подключился с адресом: {address}")

        with client_socket:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break

                message = data.decode()
                print(f"Клиент отправил: {message}")

                client_socket.send(f"Ответ сервера на: {message}".encode())

        print("Сервер завершает работу")


if __name__ == "__main__":
    main()