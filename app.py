from __future__ import print_function
from ssh2.session import Session
import socket

HOST = "192.168.27.100"
PORT = 22
TIMEOUT = 30
USERNAME = "test"
PASSWORD = "123456"


def remote_server(name):
    print("start remote")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.settimeout(TIMEOUT)

        session = Session()
        session.handshake(sock)
        session.userauth_password(USERNAME, PASSWORD)
        channel = session.open_session()
        channel.execute('/usr/bin/tail -n 100 /home/test/myfile.log')
        size, data = channel.read()

        result = ""
        while size > 0:
            result += data.decode("utf-8")
            size, data = channel.read()

        channel.close()
        return result

    except Exception as e:
        print("Could not remote to ")
        print(e)
    finally:
        print("end remote")


if __name__ == '__main__':
    str = remote_server('PyCharm')
    print(str)
