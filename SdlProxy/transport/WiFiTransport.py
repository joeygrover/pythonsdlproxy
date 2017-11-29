from transport import SdlPsm
import socket
import threading


class TCP:
    BUFFER_SIZE = 4096

    ip = 0
    port = 0
    sock = None
    client_handler = None
    interrupted = False

    handle_packet = None

    def __init__(self):
        self.data = []

    def init(self, ip, port, callback):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock = socket.socket()
        self.ip = ip
        self.port = port
        self.handle_packet = callback

    def connect(self):
        if self.sock is not None:
            self.sock.connect((self.ip, self.port))
            self.client_handler = threading.Thread(
                target=self.read_data, args=()
            )
            self.client_handler.start()

    def read_data(self):
        psm = SdlPsm.SdlPsm();
        while not self.interrupted:
            data = self.sock.recv(self.BUFFER_SIZE)
            print("Read data: ", data)
            if data is not None:
                for i in range(0,len(data)):
                    psm.handle_byte(data[i])
                    if psm.get_state() == psm.FINISHED_STATE:
                        packet = psm.get_formed_packet()
                        packet.print_log()
                        psm.reset()
                        if self.handle_packet is not None:
                            self.handle_packet(packet)
                    elif psm.get_state() == psm.ERROR_STATE:
                        psm.reset()

    def write(self, data):
        if self.sock is not None and self.interrupted is not True:
            self.sock.send(data)

    def stop(self):
        if self.sock is not None and self.client_handler is not None:
            self.interrupted = True
            self.sock.close()


