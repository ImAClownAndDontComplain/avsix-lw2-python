#!/usr/bin/python3

import socket

# ������������� ������(�� ������ UDP, � ���� ������������ SOCK_DGRAM) �� �������
# ������������ ������ ���������� ����� ����. ��������� ������������ ���������� ������ �,
# ��������������, ����� ���������� �� ���������� ������.

HOST = ''                 # ������ ������ ��������, ��� ���������� ����� ����������� �� ���� ��������� ������� �����������
PORT = 5000              # ���� ����������

# ������� ������� �����-�������
def create_listener():
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=17)  # ������� UDP-�����
    conn.bind((HOST, PORT))  # ��������� ����� � ������, ��� �� ����� ������� �����������
    print(f'Server is running on {HOST}:{PORT}, please, press ctrl+c to stop')
    # ��������� �������� ������ �� ������� � ����������� �����
    while True:
        try:
            data, addr = conn.recvfrom(1024)  # ������� ������ �� ������� (�������� 1024 ����)
            data_str = data.decode('utf-8') # ����������� ���������� �� ������� ����� � ������
            print("FROM CLIENT: " + data_str)  # ����� ���������� �� ������� ������
            # ���� �� ������� �������� ������� "exit" ��� "close", ��������� ����������
            if data_str == "exit" or data_str == "close":
                conn.sendto(b'Goodbye? see you later c:', addr)
                break   # ��������� ����
            else:
                response = "SERVER: OK"    # ��������� �� �������� ��������� ������
                conn.sendto(response.encode('utf-8'), addr)  # � ����� ������� ���������� ���������
        except Exception as error:
            print(error)
            break
    conn.close()  # ��������� ����������

if __name__ == '__main__':
    create_listener()
