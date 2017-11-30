from protocol import SdlPacket, ServiceType
from rpc import RpcStruct, RegisterAppInterface


class SdlSession:

    session_id = 0
    version = 1
    hash_id = None
    service_dict = {ServiceType.RPC: False, ServiceType.CONTROL: True,
                    ServiceType.AUDIO: False, ServiceType.VIDEO: False, ServiceType.BULK_DATA: False}

    # Callback to write out packets
    write_packet = None

    def init(self, write_packet):
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
                    self.version = packet.version
                    if packet.version < 5:
                        self.hash_id = packet.payload
                    # else TODO
                    # Service started send RAI
                    rai = RegisterAppInterface.RegisterAppInterface()
                    rai.init_with_dummy_data()
                    payload = rai.encode()
                    packet = SdlPacket.SdlPacket.create_sdl_packet(self.version, False, SdlPacket.SdlPacket.FRAME_TYPE_SINGLE,
                                                                   ServiceType.RPC, 0x00, self.session_id, len(payload), 2,
                                                                   payload)
                    print('Attempting to write RAI packet: ', packet.construct_packet())
                    self.write_packet(packet.construct_packet())


                else:
                    self.service_dict[packet.serviceType] = True

        elif packet.frameInfo == SdlPacket.SdlPacket.FRAME_INFO_START_SERVICE_NAK:
            print("There was an error trying to start service")

        elif packet.frameInfo == SdlPacket.SdlPacket.FRAME_INFO_END_SERVICE_ACK:
            if packet.serviceType == ServiceType.RPC:
                self.session_id = 0


    def handle_single_frame_packet(self, packet):
        print("Handling single frame packet in session")
        struct = RpcStruct.RpcStruct()
        struct.init_with_bytes(packet.payload)
        struct.print_values()

    def handle_first_packet(self, packet):
        print("Handling first packet in session")

    def handle_consecutive_packet(self, packet):
        print("Handling consecutive packet in session")

    def handle_rpc(self,packet:SdlPacket.SdlPacket):
        print("Handling RPC packet in session")



