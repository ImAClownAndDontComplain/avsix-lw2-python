#!/usr/bin/python3

import socket

# Дейтаграммные сокеты(на основе UDP, в коде обозначаются SOCK_DGRAM) не требуют
# установления явного соединения между ними. Сообщение отправляется указанному сокету и,
# соответственно, может получаться от указанного сокета.

HOST = ''                 # Пустая строка означает, что соединения будут приниматься на всех доступных сетевых интерфейсах
PORT = 5000              # Порт соединения

# Функция запуска сокет-сервера
def create_listener():
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=17)  # создаем UDP-сокет
    conn.bind((HOST, PORT))  # связываем сокет с портом, где он будет ожидать подключение
    print(f'Server is running on {HOST}:{PORT}, please, press ctrl+c to stop')
    # запускаем ожидание команд от клиента в бесконечном цикле
    while True:
        try:
            data, addr = conn.recvfrom(1024)  # ожидаем данные от клиента (максимум 1024 байт)
            data_str = data.decode('utf-8') # преобразуем полученные от клиента байты в строку
            print("FROM CLIENT: " + data_str)  # вывод полученных от клиента данных
            # Если от клиента получена команда "exit" или "close", закрываем соединение
            if data_str == "exit" or data_str == "close":
                conn.sendto(b'Goodbye? see you later c:', addr)
                break   # прерываем цикл
            else:
                response = "SERVER: OK"    # сообщение об успешном получении данных
                conn.sendto(response.encode('utf-8'), addr)  # в ответ клиенту отправляем сообщение
        except Exception as error:
            print(error)
            break
    conn.close()  # закрываем соединение

if __name__ == '__main__':
    create_listener()
