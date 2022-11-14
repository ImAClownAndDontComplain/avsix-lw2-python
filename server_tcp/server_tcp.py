#!/usr/bin/python3

# ��������� ������(�� ������ TCP, � ���� ������������ SOCK_STREAM) - 
# � ������������� ����������� �� ������ ��������� TCP, 
# �������� ����� ������, ������� ����� ���� ��������������� - 
# �.�. ���������� ����� � �������� � ���������� ������.

# AF_INET - �������� ���������
# 

import socket  #������������� ������

HOST = ''                 # ������ ������ ��������, ��� ���������� ����� ����������� �� ���� ��������� ������� �����������
PORT = 5000               # ���� ����������


# �������� � TCP �����-������ ������� ������ ����������� 
# ������ �� ������� � ��������� ����, � ����� ������� ������ ����������� 
# ������� ����� (� ���������� ����������) �� ������� �� �������

# a+ - ������ � ������ � ����� �����, ������� � �����
# r - ������, ������� � ������


def get_clients_data(data_str):
    my_file = open("newFile.txt","a+")
    my_file.write(data_str)
    my_file.close()

def show_client_data():
    f = open("newFile.txt","r")
    print(*f)

# ������� ������� �����-�������
def create_listener():
    # proto -��������� ��� ������������� �������, 0 ��������, ��� �� ����� ������ �� ��������� ��� ���� ������ 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)  # ������� TCP-�����
    sock.bind((HOST, PORT))  # ��������� ����� � ������, ��� �� ����� ������� ����������
    print(f'Server is running on {HOST}:{PORT}, press ctrl+c to stop')
    sock.listen(1)  # ������������� ����� �� �������������, ��������� ������ �������
    
    # accept ���������� ������ � ����� ����������: ����� ����� � ����� �������
    conn, addr = sock.accept()
    print(f'Client is connected: {addr}')  # ����� ���������� � �����������
    # ��������� �������� ������ �� ������� � ����������� �����
    while True:
        try:
            data = conn.recv(1024)  # �������� ������ �� ������� (�������� ��)
            data_str = data.decode('utf-8') # ����������� ���������� �� ������� ����� � ������
            print("Client's data: " + data_str)   # ����� ���������� �� ������� ������
            # ���� �� ������� �������� ������� "exit" ��� "close", ��������� ����������
            # ���� �� ������� �������� ������� "show", �� ���������� ��� ���������� �����
            if data_str == "exit" or data_str == "close":
                conn.send(b'Goodbye, see you later c:')
                break   # ��������� ����
            if data_str == "show":
                show_client_data()
                response = "SERVER: OK"
                conn.send(response.encode('utf-8'))
            else:
                get_clients_data(data_str) # ��������� ������ �� ������� � ���������� �� � ����
                response = "SERVER: OK"    # ��������� �� �������� ��������� ������
                conn.send(response.encode('utf-8'))  # � ����� ������� ������������ ���������
        except Exception as error: # ��������� ���������� - ����� ��������� �� ������
            print(error)
            break
    
    conn.close()  # ��������� ����������

if __name__ == '__main__':
    create_listener()

