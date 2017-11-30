from rpc import FunctionIds, FunctionId
import json


class RpcStruct:

    parameters = dict()
    rpc_type = 0
    correlation_id = 0
    function_id = None
    params = {}
    json_object = None

    def init_with_bytes(self, raw_bytes):
        self.parse_bytes(raw_bytes)

    def get_json(self):
        self.parameters = json.dumps(self.parameters)
        return json.loads(self.parameters)

    def parse_bytes(self, raw_bytes):
        binary_frame_header = raw_bytes[0:12]
        self.rpc_type = binary_frame_header[0] >> 4

        function_id = (binary_frame_header[0] & 0x0F) << 24  # TODO check if this is right with the mask
        function_id += (binary_frame_header[1] & 0xFF) << 16
        function_id += (binary_frame_header[2] & 0xFF) << 8
        function_id += binary_frame_header[3] & 0xFF

        self.function_id = FunctionIds.get_id(function_id)

        self.correlation_id = (binary_frame_header[4] & 0xFF) << 24
        self.correlation_id += (binary_frame_header[5] & 0xFF) << 16
        self.correlation_id += (binary_frame_header[6] & 0xFF) << 8
        self.correlation_id += binary_frame_header[7] & 0xFF

        json_size = (binary_frame_header[8] & 0xFF) << 24
        json_size += (binary_frame_header[9] & 0xFF) << 16
        json_size += (binary_frame_header[10] & 0xFF) << 8
        json_size += binary_frame_header[11] & 0xFF

        json_bytes = raw_bytes[12:(12+json_size)].decode('utf-8')

        self.json_object = json.loads(json_bytes)

    def encode(self):
        self.json_object = json.dumps(self.params, ensure_ascii=False)
        print(self.json_object)
        buffer = bytearray()

        buffer.append(((self.function_id.function_id & 0x0F000000) >> 24) + (self.rpc_type << 4))
        buffer.append(((self.function_id.function_id & 0x00FF0000) >> 16))
        buffer.append(((self.function_id.function_id & 0x0000FF00) >> 8))
        buffer.append((self.function_id.function_id & 0x000000FF))

        buffer.append(((self.correlation_id & 0xFF000000) >> 24))
        buffer.append(((self.correlation_id & 0x00FF0000) >> 16))
        buffer.append(((self.correlation_id & 0x0000FF00) >> 8))
        buffer.append((self.correlation_id & 0x000000FF))

        json_size = len(self.json_object)

        buffer.append(((json_size & 0xFF000000) >> 24))
        buffer.append(((json_size & 0x00FF0000) >> 16))
        buffer.append(((json_size & 0x0000FF00) >> 8))
        buffer.append((json_size & 0x000000FF))

        buffer.extend(self.json_object.encode())

        print('lol packet: ', buffer)
        return buffer

    def print_values(self):
        print('RPC Type: ', self.rpc_type)
        print('correlation_id: ', self.correlation_id)
        print('function_id: ', self.function_id.name)
        print('json_object: ', self.json_object)
