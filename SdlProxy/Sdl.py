from protocol import SdlPacket, ServiceType, SdlPacketFactory
from transport import SdlPsm, WiFiTransport
from session import SdlSession


class Sdl:

    # Create transport, create session
    session = None

    def __init__(self):
        self.data = []
    print(" ***** Creating sample packet ***** ")
    # packet = SdlPacket.SdlPacket.create_sdl_packet(1, False, SdlPacket.SdlPacket.FRAME_TYPE_CONTROL,
    #                                               ServiceType.ServiceType.RPC,
    #                                               SdlPacket.SdlPacket.FRAME_INFO_START_SERVICE, 0, 1, 0, None)
    packet = SdlPacketFactory.create_rpc_start_service(False)
    packet.print_log()
    byte_array = packet.construct_packet()
    psm = SdlPsm.SdlPsm()
    psm.reset()
    print(" ***** Iterating through packet bytes ***** ")

    for i in range(0, len(byte_array)):
        print(byte_array[i])
        did_move = psm.handle_byte(byte_array[i])
        # print("did move:", did_move)
    if psm.get_state() == psm.FINISHED_STATE:
        packet = psm.get_formed_packet()
        print(" ***** Packet completed through PSM ***** ")
        packet.print_log()
    else:
        print("Effing error")

    session = SdlSession.SdlSession()
    print(" ***** Attempting to create TCP connection ***** ")
    tcp = WiFiTransport.TCP()
    tcp.init('m.sdl.tools', 5420, session.handle_packet)
    tcp.connect()
    print(" ***** Connected *****")
    session.init(tcp.write)
    tcp.write(packet.construct_packet())
