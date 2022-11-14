import socket

HOST = '192.168.56.101'    # ����� ������� (���� �� ������� �������� �� ����)
PORT = 5000                # ���� ���������� �������
PROTO = 'udp'              # ������������ �������� (tcp/udp)

if __name__ == '__main__':
    client = None
    if PROTO == 'tcp':
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0) # ������� TCP-�����
    elif PROTO == 'udp':
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=17)  # ������� UDP-�����
    if client is not None:
        client.connect((HOST, PORT))    # ����������� � ��������
        print("Type in something and press enter...")
        while True:
            data = input()                               # ������ ���� �� ��������� ������
            client.send(data.encode('utf-8'))            # �������� ������ �� ������ (� ��������� utf-8)
            response = client.recv(1024).decode('utf-8') # ��������� ������ � ������� � ���������� ����� � ������
            print(response)
            # ���� �� ������� �������� ����� 'bye!' , ��������� ����������
            if response == 'Goodbye, see you later c:':
                break
        print('Connection closed.')
    print('Exit.')

