class SdlPacket:

    HEADER_SIZE = 12
    HEADER_SIZE_V1 = 8  # Backwards
    ENCRYPTION_MASK = 0x08  # 4th lowest bit

    FRAME_TYPE_CONTROL = 0x00
    FRAME_TYPE_SINGLE = 0x01
    FRAME_TYPE_FIRST = 0x02
    FRAME_TYPE_CONSECUTIVE = 0x03

    # Service Type
    SERVICE_TYPE_CONTROL = 0x00
    # RESERVED 0x01 - 0x06
    SERVICE_TYPE_RPC = 0x07
    # RESERVED 0x08 - 0x09
    SERVICE_TYPE_PCM = 0x0A
    SERVICE_TYPE_VIDEO = 0x0B
    # RESERVED 0x0C - 0x0E
    SERVICE_TYPE_BULK_DATA = 0x0F
    # RESERVED 0x10 - 0xFF

    # Frame Info
    # Control Frame Info
    FRAME_INFO_HEART_BEAT = 0x00
    FRAME_INFO_START_SERVICE = 0x01
    FRAME_INFO_START_SERVICE_ACK = 0x02
    FRAME_INFO_START_SERVICE_NAK = 0x03
    FRAME_INFO_END_SERVICE = 0x04
    FRAME_INFO_END_SERVICE_ACK = 0x05
    FRAME_INFO_END_SERVICE_NAK = 0x06
    # 0x07-0xFD are reserved
    FRAME_INFO_SERVICE_DATA_ACK = 0xFE
    FRAME_INFO_HEART_BEAT_ACK = 0xFF

    FRAME_INFO_FINAL_CONNESCUTIVE_FRAME = 0x00

    # Most others
    FRAME_INFO_RESERVED = 0x00

    version = 0
    encryption = False
    frameType = -1
    serviceType = -1
    frameInfo = -1
    sessionId = -1
    dataSize = 0
    messageId = -1

    payload = None
    # TODO  Deal with this later HashMap <String, Object > bsonPayload;

    def __init__(self):
        self.data = []

    @staticmethod
    def create_sdl_packet(version, compression, frame_type, service_type, control_frame_info, session_id, data_length, message_id, payload):
        packet = SdlPacket()
        packet.version = version
        packet.compression = compression
        packet.frameType = frame_type
        packet.serviceType = service_type
        packet.frameInfo = control_frame_info
        packet.sessionId = session_id
        packet.dataSize = data_length
        packet.messageId = message_id
        packet.payload = payload
        return packet

    @staticmethod
    def get_encryption_bit(encryption):
        if encryption:
            return SdlPacket.ENCRYPTION_MASK
        else:
            return 0

    def print_log(self):
        print("version: ", self.version)
        print("encryption: ", self.encryption)
        print("frame type: ", self.frameType)
        print("service type: ", self.serviceType)
        print("frame info: ", self.frameInfo)
        print("session id: ", self.sessionId)
        print("data length: ", self.dataSize)
        print("message id: ", self.messageId)
        print("payload : ", self.payload)

    def construct_packet(self):
        size = 0
        if self.version == 1:
            size = self.HEADER_SIZE_V1 + self.dataSize
        else:
            size = self.HEADER_SIZE + self.dataSize

        # buffer = bytearray(size)  # TODO look into bytes over bytearray
        buffer = bytearray()

        buffer.append((self.version << 4) + SdlPacket.get_encryption_bit(self.encryption) + self.frameType)
        buffer.append(self.serviceType)
        buffer.append(self.frameInfo)
        buffer.append(self.sessionId)

        buffer.append(((self.dataSize & 0xFF000000) >> 24))
        buffer.append(((self.dataSize & 0x00FF0000) >> 16))
        buffer.append(((self.dataSize & 0x0000FF00) >> 8))
        buffer.append((self.dataSize & 0x000000FF))

        if self.version > 1:
            buffer.append(((self.messageId & 0xFF000000) >> 24))
            buffer.append(((self.messageId & 0x00FF0000) >> 16))
            buffer.append(((self.messageId & 0x0000FF00) >> 8))
            buffer.append((self.messageId & 0x000000FF))
        if self.payload is not None and len(self.payload) > 0:
            for i in range(0, len(self.payload)):
                buffer.append(self.payload[i])  # TODO there's got to be a better way
        return buffer











