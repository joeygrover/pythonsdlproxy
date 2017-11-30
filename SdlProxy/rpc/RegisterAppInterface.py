from rpc import RpcStruct, FunctionIds


class RegisterAppInterface(RpcStruct.RpcStruct):

    def __init__(self):
        self.correlation_id = 65529
        self.function_id = FunctionIds.REGISTER_APP_INTERFACE
        self.rpc_type = 0

    def init_with_dummy_data(self):
        self.params['syncMsgVersion'] = {'majorVersion': 4, 'minorVersion': 5, 'patchVersion': 0 }   # TODO check into
        self.params['appName'] = 'Dummy'
        self.params['appID'] = '5234523452'
        self.params['isMediaApplication'] = True
        self.params['languageDesired'] = 'EN-US'   # TODO check into
        self.params['hmiDisplayLanguageDesired'] = 'EN-US'   # TODO check into



