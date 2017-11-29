from protocol import SdlPacket, ServiceType


class SdlSession:

    session_id = 0
    hash_id = None
    service_dict = {ServiceType.RPC: False, ServiceType.CONTROL: True,
                    ServiceType.AUDIO: False, ServiceType.VIDEO: False, ServiceType.BULK_DATA: False}

    # Callback to write out packets
    write_packet = None

    def init(self,write_packet):
        self.write_packet = write_packet

    def handle_packet(self, packet:SdlPacket.SdlPacket):
        if packet.frameType == SdlPacket.SdlPacket.FRAME_TYPE_CONTROL:
            self.handle_control_packet(packet)
        elif packet.frameType == SdlPacket.SdlPacket.FRAME_TYPE_SINGLE:
            self.handle_single_frame_packet(packet)
        elif packet.frameType == SdlPacket.SdlPacket.FRAME_TYPE_FIRST:
            self.handle_first_packet(packet)
        elif packet.frameType == SdlPacket.SdlPacket.FRAME_TYPE_CONSECUTIVE:
            self.handle_consecutive_packet(packet)
        else:
            print("No idea what this packet is: ", packet.frameType)

    def handle_control_packet(self, packet:SdlPacket.SdlPacket):
        print("Handling control packet in session")
        if packet.frameInfo == SdlPacket.SdlPacket.FRAME_INFO_START_SERVICE_ACK:
                # We have connected and created our session
                if packet.serviceType == ServiceType.RPC:
                    self.service_dict[ServiceType.RPC] = True
                    self.service_dict[ServiceType.BULK_DATA] = True
                    self.session_id = packet.sessionId
                    if packet.version < 5:
                        self.hash_id = packet.payload
                    # else TODO
                else:
                    self.service_dict[packet.serviceType] = True

        elif packet.frameInfo == SdlPacket.SdlPacket.FRAME_INFO_START_SERVICE_NAK:
            print("There was an error trying to start service")

        elif packet.frameInfo == SdlPacket.SdlPacket.FRAME_INFO_END_SERVICE_ACK:
            if packet.serviceType == ServiceType.RPC:
                self.session_id = 0


    def handle_single_frame_packet(self, packet):
        print("Handling single frame packet in session")

    def handle_first_packet(self, packet):
        print("Handling first packet in session")

    def handle_consecutive_packet(self, packet):
        print("Handling consecutive packet in session")

    def handle_rpc(self,packet:SdlPacket.SdlPacket):
        print("Handling RPC packet in session")



