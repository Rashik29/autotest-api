import socket


def server():
    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем его к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Начинаем слушать входящие подключения (максимум 10 в очереди)
    server_socket.listen(10)
    print("Сервер запущен и ждет подключений...")

    # Список для хранения всех сообщений
    all_messages = []

    while True:
        # Принимаем соединение от клиента
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        try:
            # Получаем данные от клиента
            data = client_socket.recv(1024).decode()

            if data:  # Если данные не пустые
                print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

                # Добавляем сообщение в список
                all_messages.append(data)

                # Отправляем клиенту всю историю сообщений, каждое с новой строки
                response = '\n'.join(all_messages)
                client_socket.sendall(response.encode())

        finally:
            # Закрываем соединение с клиентом
            client_socket.close()


if __name__ == '__main__':
    server()