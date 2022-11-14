import socket

HOST = '192.168.56.101'    # Адрес сервера (было бы логично поменять на свой)
PORT = 5000                # Порт удаленного сервера
PROTO = 'udp'              # Транспортный протокол (tcp/udp)

if __name__ == '__main__':
    client = None
    if PROTO == 'tcp':
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0) # создаем TCP-сокет
    elif PROTO == 'udp':
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=17)  # создаем UDP-сокет
    if client is not None:
        client.connect((HOST, PORT))    # соединяемся с сервером
        print("Type in something and press enter...")
        while True:
            data = input()                               # читаем ввод из командной строки
            client.send(data.encode('utf-8'))            # посылаем данные на сервер (в кодировке utf-8)
            response = client.recv(1024).decode('utf-8') # принимаем данные с сервера и декодируем байты в строку
            print(response)
            # Если от сервера поступил ответ 'bye!' , закрываем соединение
            if response == 'Goodbye, see you later c:':
                break
        print('Connection closed.')
    print('Exit.')

