import socket

# Создание клиентского сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
client_socket.connect(('localhost', 8000))

# Отправка запроса
request = b"Hello, server!"
client_socket.send(request)

# Получение ответа
response = client_socket.recv(1024)
print(response.decode())

# Закрытие соединения
client_socket.close()
