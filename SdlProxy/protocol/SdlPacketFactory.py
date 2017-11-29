from protocol import SdlPacket, ServiceType

# create_sdl_packet(version, compression, frame_type, service_type, control_frame_info, session_id, data_length, message_id, payload):


def create_start_service(version, encryption, service_type, session_id, message_id, payload, payload_length):
    return SdlPacket.SdlPacket.create_sdl_packet(version, encryption, SdlPacket.SdlPacket.FRAME_TYPE_CONTROL,
                                                 service_type,
                                                 SdlPacket.SdlPacket.FRAME_INFO_START_SERVICE, session_id,
                                                 payload_length, message_id, payload)


def create_rpc_start_service(encryption):
    return create_start_service(1, encryption, ServiceType.RPC, 0, 0, None, 0);
