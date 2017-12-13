from protocol import SdlPacket, SdlProtocol


class SdlPsm:

    # PSM States
    START_STATE = 0x0
    SERVICE_TYPE_STATE = 0x02
    CONTROL_FRAME_INFO_STATE = 0x03
    SESSION_ID_STATE = 0x04
    DATA_SIZE_1_STATE = 0x05
    DATA_SIZE_2_STATE = 0x06
    DATA_SIZE_3_STATE = 0x07
    DATA_SIZE_4_STATE = 0x08
    MESSAGE_1_STATE = 0x09
    MESSAGE_2_STATE = 0x0A
    MESSAGE_3_STATE = 0x0B
    MESSAGE_4_STATE = 0x0C
    DATA_PUMP_STATE = 0x0D
    FINISHED_STATE = 0xFF
    ERROR_STATE = -1

    FIRST_FRAME_DATA_SIZE = 0x08
    VERSION_MASK = 0xF0  # 4 highest bits
    COMPRESSION_MASK = 0x08  # 4th lowest bit
    FRAME_TYPE_MASK = 0x07  # 3 lowest bits

    # member vars
    state = START_STATE
    version = 0
    compression = False
    frameType = -1
    serviceType = -1
    controlFrameInfo = -1
    sessionId = -1
    dumpSize = 0
    dataLength = 0
    messageId = 0

    payload = bytes([])

    def __init__(self):
        self.data = []

    @staticmethod
    def pseudo_break():
        return

    def reset(self):
        self.state = self.START_STATE
        self.version = 0
        self.compression = False
        self.frameType = -1
        self.serviceType = -1
        self.controlFrameInfo = -1
        self.sessionId = -1
        self.dumpSize = 0
        self.dataLength = 0
        self.messageId = 0

        self.payload = bytes([])

    def handle_byte(self,data):
        # print("Current state: ", self.state)
        self.state = self.transition_on_input(data, self.state)
        if self.state == self.ERROR_STATE:
            return False
        else:
            return True

    def transition_on_input(self, raw_byte, state):
        if state == self.START_STATE:
            self.version = (raw_byte & self.VERSION_MASK) >> 4
            # Log.trace(TAG, "Version: " + version);
            if self.version == 0: # It should never be 0
                return self.ERROR_STATE

            self.compression = (1 == ((raw_byte & self.COMPRESSION_MASK) >> 3))

            self.frameType = raw_byte & self.FRAME_TYPE_MASK
            # Log.trace(TAG, raw_byte + " = Frame Type: " + frameType);

            # These are known versions supported by this library.
            if (self.version < 1 or self.version > 5) and self.frameType != SdlPacket.SdlPacket.FRAME_TYPE_CONTROL:
                return self.ERROR_STATE

            if self.frameType < SdlPacket.SdlPacket.FRAME_TYPE_CONTROL \
                    or self.frameType > SdlPacket.SdlPacket.FRAME_TYPE_CONSECUTIVE:
                return self.ERROR_STATE

            # We made it through.
            return self.SERVICE_TYPE_STATE
        elif state == self.SERVICE_TYPE_STATE:
            self.serviceType = (raw_byte & 0xFF)
            return self.CONTROL_FRAME_INFO_STATE

        elif state == self.CONTROL_FRAME_INFO_STATE:
            self.controlFrameInfo = raw_byte & 0xFF
            if self.frameType == SdlPacket.SdlPacket.FRAME_TYPE_CONTROL or self.frameType == SdlPacket.SdlPacket.FRAME_TYPE_CONSECUTIVE:
                self.pseudo_break()
            elif self.frameType == SdlPacket.SdlPacket.FRAME_TYPE_SINGLE \
                    or self.frameType == SdlPacket.SdlPacket.FRAME_TYPE_FIRST:
                # Fall through since they are both the same
                if self.controlFrameInfo != 0x00:
                    return self.ERROR_STATE
            else:
                return self.ERROR_STATE

            return self.SESSION_ID_STATE
        elif state == self.SESSION_ID_STATE:
            self.sessionId = (raw_byte & 0xFF)
            return self.DATA_SIZE_1_STATE
        elif state == self.DATA_SIZE_1_STATE:
            # First data size byte
            self.dataLength += (raw_byte & 0xFF) << 24  # 3 bytes x 8 bits
            return self.DATA_SIZE_2_STATE
        elif state == self.DATA_SIZE_2_STATE:
            self.dataLength += (raw_byte & 0xFF) << 16  # 2 bytes x 8 bits
            return self.DATA_SIZE_3_STATE
        elif state == self.DATA_SIZE_3_STATE:
            self.dataLength += (raw_byte & 0xFF) << 8  # 1 byte x 8 bits
            return self.DATA_SIZE_4_STATE
        elif state == self.DATA_SIZE_4_STATE:
            self.dataLength += raw_byte & 0xFF
            if self.frameType == SdlPacket.SdlPacket.FRAME_TYPE_SINGLE or self.frameType == SdlPacket.SdlPacket.FRAME_TYPE_CONSECUTIVE:
                SdlPsm.pseudo_break()
            elif self.frameType == SdlPacket.SdlPacket.FRAME_TYPE_CONTROL:
                # Ok, well here's some interesting bit of knowledge.
                # Because the start session request is from the phone with no knowledge of version it sends out a
                # v1 packet.THEREFORE there is no message id field.
                # ** ** Now you know and knowing is half the battle ** **
                if self.version == 1 and self.controlFrameInfo == SdlPacket.SdlPacket.FRAME_INFO_START_SERVICE:
                    if self.dataLength == 0:
                        return self.FINISHED_STATE  # We are done if we don't have any payload
                    if self.dataLength <= SdlProtocol.SdlProtocol.V1_V2_MTU_SIZE - SdlProtocol.SdlProtocol.V1_HEADER_SIZE:
                        self.payload = bytearray(self.dataLength)
                    else:
                        return self.ERROR_STATE
                    self.dumpSize = self.dataLength
                    return self.DATA_PUMP_STATE
            elif self.frameType == SdlPacket.SdlPacket.FRAME_TYPE_FIRST:
                if self.dataLength == self.FIRST_FRAME_DATA_SIZE:
                    SdlPsm.pseudo_break()
                else:
                    return self.ERROR_STATE

            if self.version == 1:  # Version 1 packets will not have message id's
                if self.dataLength == 0:
                    return self.FINISHED_STATE # We are done if we don't have any payload
                if self.dataLength <= SdlProtocol.SdlProtocol.V1_V2_MTU_SIZE - SdlProtocol.SdlProtocol.V1_HEADER_SIZE:
                    self.payload =  bytearray(self.dataLength)
                else :
                    return self.ERROR_STATE
                self.dumpSize = self.dataLength
                return self.DATA_PUMP_STATE
            else:
                return self.MESSAGE_1_STATE
        elif state == self.MESSAGE_1_STATE:
            self.messageId += (raw_byte & 0xFF) << 24 # 3bytesx8bits
            return self.MESSAGE_2_STATE
        elif state == self.MESSAGE_2_STATE:
            self.messageId += (raw_byte & 0xFF) << 16 # 2bytesx8bits
            return self.MESSAGE_3_STATE
        elif state == self.MESSAGE_3_STATE:
            self.messageId += (raw_byte & 0xFF) << 8 # 1bytex8bits
            return self.MESSAGE_4_STATE
        elif state == self.MESSAGE_4_STATE:
            self.messageId += raw_byte & 0xFF
            if self.dataLength == 0:
                return self.FINISHED_STATE; # We are done if we don't have any payload
            # TODO We might need a try/catch or w/e the hell it is in python for OOM
            try:
                self.payload = bytearray(self.dataLength)
            except Exception:
                return self.ERROR_STATE
            self.dumpSize = self.dataLength
            return self.DATA_PUMP_STATE
        elif state == self.DATA_PUMP_STATE:
            self.payload[self.dataLength - self.dumpSize] = raw_byte;
            self.dumpSize -= 1  # Do we have any more bytes to  read in?
            if self.dumpSize > 0:
                return self.DATA_PUMP_STATE
            elif self.dumpSize == 0:
                return self.FINISHED_STATE
            else:
                return self.ERROR_STATE
        elif state == self.FINISHED_STATE: # We shouldn't be here...Should have been reset
            return self.ERROR_STATE
        else:
            return self.ERROR_STATE

    def get_formed_packet(self):
        if self.state == self.FINISHED_STATE:
            return SdlPacket.SdlPacket.create_sdl_packet(self.version, self.compression, self.frameType, self.serviceType,
                                                         self.controlFrameInfo, self.sessionId, self.dataLength, self.messageId,
                                                         self.payload)
        else:
            return None

    def get_state(self):
        return self.state
