import socket

class RigNetCtl():
    def __init__(self, hostname = "127.0.0.1", port = 4532):
        self._host = hostname
        self._port = port
        self._sock = None


    def connect(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((self._host, self._port))


    def _sendcommand(self, data):
        if not self._sock:
            raise ConnectionError("Not connected")

        self._sock.sendall(data.encode())
        data = self._sock.recv(128)

        return data.decode()


    def get_frequency(self):
        return int(self._sendcommand("f"))


    def get_mode(self):
        return self._sendcommand("m")
