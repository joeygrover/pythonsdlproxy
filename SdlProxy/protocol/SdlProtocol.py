class SdlProtocol:

    V1_V2_MTU_SIZE = 1500
    V3_V4_MTU_SIZE = 131072;
    V1_HEADER_SIZE = 8
    v2_HEADER_SIZE = 12

    def __init__(self):
        self.data = []
