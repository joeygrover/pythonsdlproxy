import json


class RpcStruct:

    parameters = dict()

    def __init__(self):
        self.data = []

    def get_json(self):
        self.parameters = json.dumps(self.parameters)
        return json.loads(self.parameters)
