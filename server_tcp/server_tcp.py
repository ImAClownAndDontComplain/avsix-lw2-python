#!/usr/bin/python3

# Потоковые сокеты(на основе TCP, в коде обозначаются SOCK_STREAM) - 
# с установленным соединением на основе протокола TCP, 
# передают поток байтов, который может быть двунаправленным - 
# т.е. приложение может и получать и отправлять данные.

# AF_INET - интернет протоколы
# 

import socket  #установленный модуль

HOST = ''                 # Пустая строка означает, что соединения будут приниматься на всех доступных сетевых интерфейсах
PORT = 5000               # Порт соединения


# Добавить в TCP сокет-сервер функцию записи поступающих 
# данных от клиента в отдельный файл, а также функцию вывода содержимого 
# данного файла (в клиентское приложение) по команде от клиента

# a+ - чтение и запись в конец файла, каретка в конце
# r - чтение, каретка в начале


def get_clients_data(data_str):
    my_file = open("newFile.txt","a+")
    my_file.write(data_str)
    my_file.close()

def show_client_data():
    f = open("newFile.txt","r")
    print(*f)

# Функция запуска сокет-сервера
def create_listener():
    # proto -мпротокол для использования сокетом, 0 означает, что он будет выбран по умолчанию для типа сокета 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)  # создаем TCP-сокет
    sock.bind((HOST, PORT))  # связываем сокет с портом, где он будет ожидать соединение
    print(f'Server is running on {HOST}:{PORT}, press ctrl+c to stop')
    sock.listen(1)  # устанавливаем сокет на прослушивание, указываем размер очереди
    
    # accept возвращает кортеж с двумя элементами: новый сокет и адрес клиента
    conn, addr = sock.accept()
    print(f'Client is connected: {addr}')  # вывод информации о подключении
    # запускаем ожидание команд от клиента в бесконечном цикле
    while True:
        try:
            data = conn.recv(1024)  # ожидание данных от клиента (максимум Кб)
            data_str = data.decode('utf-8') # преобразуем полученные от клиента байты в строку
            print("Client's data: " + data_str)   # вывод полученных от клиента данных
            # Если от клиента получена команда "exit" или "close", закрываем соединение
            # Если от клиента получена команда "show", то показываем ему содержимое файла
            if data_str == "exit" or data_str == "close":
                conn.send(b'Goodbye, see you later c:')
                break   # прерываем цикл
            if data_str == "show":
                show_client_data()
                response = "SERVER: OK"
                conn.send(response.encode('utf-8'))
            else:
                get_clients_data(data_str) # получение данных от клиента и сохранение их в файл
                response = "SERVER: OK"    # сообщение об успешном получении данных
                conn.send(response.encode('utf-8'))  # в ответ клиенту отправляется сообщение
        except Exception as error: # обработка исключений - вывод сообщения об ошибке
            print(error)
            break
    
    conn.close()  # закрываем соединение

if __name__ == '__main__':
    create_listener()

