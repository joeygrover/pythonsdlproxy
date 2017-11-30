from rpc import FunctionId

# TODO fix this thing

UNKNOWN = FunctionId.FunctionId(0, "Unknown")
REGISTER_APP_INTERFACE = FunctionId.FunctionId(1, "RegisterAppInterface")
UNREGISTER_APP_INTERFACE= FunctionId.FunctionId(2, "UnregisterAppInterface")
SET_GLOBAL_PROPERTIES = FunctionId.FunctionId(3, "SetGlobalProperties")
RESET_GLOBAL_PROPERTIES = FunctionId.FunctionId(4, "ResetGlobalProperties")
ADD_COMMAND = FunctionId.FunctionId(5, "AddCommand")
DELETE_COMMAND = FunctionId.FunctionId(6, "DeleteCommand")
ADD_SUB_MENU = FunctionId.FunctionId(7, "AddSubMenu")
DELETE_SUB_MENU = FunctionId.FunctionId(8, "DeleteSubMenu")
CREATE_INTERACTION_CHOICE_SET = FunctionId.FunctionId(9, "CreateInteractionChoiceSet")
PERFORM_INTERACTION = FunctionId.FunctionId(10, "PerformInteraction")
DELETE_INTERACTION_CHOICE_SET = FunctionId.FunctionId(11, "DeleteInteractionChoiceSet")
ALERT = FunctionId.FunctionId(12, "Alert")
SHOW = FunctionId.FunctionId(13, "Show")
SPEAK = FunctionId.FunctionId(14, "Speak")
SET_MEDIA_CLOCK_TIMER = FunctionId.FunctionId(15, "SetMediaClockTimer")
PERFORM_AUDIO_PASS_THRU = FunctionId.FunctionId(16, "PerformAudioPassThru")
END_AUDIO_PASS_THRU = FunctionId.FunctionId(17, "EndAudioPassThru")
SUBSCRIBE_BUTTON = FunctionId.FunctionId(18, "SubscribeButton")
UNSUBSCRIBE_BUTTON = FunctionId.FunctionId(19, "UnsubscribeButton")
SUBSCRIBE_VEHICLE_DATA = FunctionId.FunctionId(20, "SubscribeVehicleData")
UNSUBSCRIBE_VEHICLE_DATA = FunctionId.FunctionId(21, "UnsubscribeVehicleData")
GET_VEHICLE_DATA = FunctionId.FunctionId(22, "GetVehicleData")
READ_DID = FunctionId.FunctionId(23, "ReadDID")
GET_DTCS = FunctionId.FunctionId(24, "GetDTCs")
SCROLLABLE_MESSAGE = FunctionId.FunctionId(25, "ScrollableMessage")
SLIDER = FunctionId.FunctionId(26, "Slider")
SHOW_CONSTANT_TBT = FunctionId.FunctionId(27, "ShowConstantTBT")
ALERT_MANEUVER = FunctionId.FunctionId(28, "AlertManeuver")
UPDATE_TURN_LIST = FunctionId.FunctionId(29, "UpdateTurnList")
CHANGE_REGISTRATION = FunctionId.FunctionId(30, "ChangeRegistration")
GENERIC_RESPONSE = FunctionId.FunctionId(31, "GenericResponse")
PUT_FILE = FunctionId.FunctionId(32, "PutFile")
DELETE_FILE = FunctionId.FunctionId(33, "DeleteFile")
LIST_FILES = FunctionId.FunctionId(34, "ListFiles")
SET_APP_ICON = FunctionId.FunctionId(35, "SetAppIcon")
SET_DISPLAY_LAYOUT = FunctionId.FunctionId(36, "SetDisplayLayout")
DIAGNOSTIC_MESSAGE = FunctionId.FunctionId(37, "DiagnosticMessage")
SYSTEM_REQUEST = FunctionId.FunctionId(38, "SystemRequest")
SEND_LOCATION = FunctionId.FunctionId(39, "SendLocation")
DIAL_NUMBER = FunctionId.FunctionId(40, "DialNumber")

BUTTON_PRESS = FunctionId.FunctionId(41, "ButtonPress")
GET_INTERIOR_VEHICLE_DATA = FunctionId.FunctionId(43, "GetInteriorVehicleData")
SET_INTERIOR_VEHICLE_DATA = FunctionId.FunctionId(44, "SetInteriorVehicleData")

GET_WAY_POINTS = FunctionId.FunctionId(45, "GetWayPoints")
SUBSCRIBE_WAY_POINTS = FunctionId.FunctionId(46, "SubscribeWayPoints")
UNSUBSCRIBE_WAY_POINTS = FunctionId.FunctionId(47, "UnsubscribeWayPoints")
GET_SYSTEM_CAPABILITY = FunctionId.FunctionId(48, "GetSystemCapability")
SEND_HAPTIC_DATA = FunctionId.FunctionId(49, "SendHapticData")

# NOTIFICATIONS
ON_HMI_STATUS = FunctionId.FunctionId(32768, "OnHMIStatus")
ON_APP_INTERFACE_UNREGISTERED = FunctionId.FunctionId(32769, "OnAppInterfaceUnregistered")
ON_BUTTON_EVENT = FunctionId.FunctionId(32770, "OnButtonEvent")
ON_BUTTON_PRESS = FunctionId.FunctionId(32771, "OnButtonPress")
ON_VEHICLE_DATA = FunctionId.FunctionId(32772, "OnVehicleData")
ON_COMMAND = FunctionId.FunctionId(32773, "OnCommand")
ON_TBT_CLIENT_STATE = FunctionId.FunctionId(32774, "OnTBTClientState")
ON_DRIVER_DISTRACTION = FunctionId.FunctionId(32775, "OnDriverDistraction")
ON_PERMISSIONS_CHANGE = FunctionId.FunctionId(32776, "OnPermissionsChange")
ON_AUDIO_PASS_THRU = FunctionId.FunctionId(32777, "OnAudioPassThru")
ON_LANGUAGE_CHANGE = FunctionId.FunctionId(32778, "OnLanguageChange")
ON_KEYBOARD_INPUT = FunctionId.FunctionId(32779, "OnKeyboardInput")
ON_TOUCH_EVENT = FunctionId.FunctionId(32780, "OnTouchEvent")
ON_SYSTEM_REQUEST = FunctionId.FunctionId(32781, "OnSystemRequest")
ON_HASH_CHANGE = FunctionId.FunctionId(32782, "OnHashChange")
ON_INTERIOR_VEHICLE_DATA = FunctionId.FunctionId(32783, "OnInteriorVehicleData")
ON_WAY_POINT_CHANGE = FunctionId.FunctionId(32784, "OnWayPointChange")

ids = {
    1: REGISTER_APP_INTERFACE,
    2: UNREGISTER_APP_INTERFACE,
    3: SET_GLOBAL_PROPERTIES,
    4: RESET_GLOBAL_PROPERTIES,
    5: ADD_COMMAND,
    6: DELETE_COMMAND,
    7: ADD_SUB_MENU,
    8: DELETE_SUB_MENU,
    9: CREATE_INTERACTION_CHOICE_SET,
    10: PERFORM_INTERACTION,
    11: DELETE_INTERACTION_CHOICE_SET,
    12: ALERT,
    13: SHOW,
    14: SPEAK,
    15: SET_MEDIA_CLOCK_TIMER,
    16: PERFORM_AUDIO_PASS_THRU,
    17: END_AUDIO_PASS_THRU,
    18: SUBSCRIBE_BUTTON,
    19: UNSUBSCRIBE_BUTTON,
    20: SUBSCRIBE_VEHICLE_DATA,
    21: UNSUBSCRIBE_VEHICLE_DATA,
    22: GET_VEHICLE_DATA,
    23: READ_DID,
    24: GET_DTCS,
    25: SCROLLABLE_MESSAGE,
    26: SLIDER,
    27: SHOW_CONSTANT_TBT,
    28: ALERT_MANEUVER,
    29: UPDATE_TURN_LIST,
    30: CHANGE_REGISTRATION,
    31: GENERIC_RESPONSE,
    32: PUT_FILE,
    33: DELETE_FILE,
    34: LIST_FILES,
    35: SET_APP_ICON,
    36: SET_DISPLAY_LAYOUT,
    37: DIAGNOSTIC_MESSAGE,
    38: SYSTEM_REQUEST,
    39: SEND_LOCATION,
    40: DIAL_NUMBER,
    41: BUTTON_PRESS,
    # 42: <NA>,
    43: GET_INTERIOR_VEHICLE_DATA,
    44: SET_INTERIOR_VEHICLE_DATA,
    45: GET_WAY_POINTS,
    46: SUBSCRIBE_WAY_POINTS,
    47: UNSUBSCRIBE_WAY_POINTS,
    48: GET_SYSTEM_CAPABILITY,
    49: SEND_HAPTIC_DATA,

    32768: ON_HMI_STATUS,
    32769: ON_APP_INTERFACE_UNREGISTERED,
    32770: ON_BUTTON_EVENT,
    32771: ON_BUTTON_PRESS,
    32772: ON_VEHICLE_DATA,
    32773: ON_COMMAND,
    32774: ON_TBT_CLIENT_STATE,
    32775: ON_DRIVER_DISTRACTION,
    32776: ON_PERMISSIONS_CHANGE,
    32777: ON_AUDIO_PASS_THRU,
    32778: ON_LANGUAGE_CHANGE,
    32779: ON_KEYBOARD_INPUT,
    32780: ON_TOUCH_EVENT,
    32781: ON_SYSTEM_REQUEST,
    32782: ON_HASH_CHANGE,
    32783: ON_INTERIOR_VEHICLE_DATA,
    32784: ON_WAY_POINT_CHANGE,

}


def get_id(raw_id):
    return ids.get(raw_id, UNKNOWN)

