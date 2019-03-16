from onvif import ONVIFCamera


class PTZTests:
    def __init__(self, cam):
        self.cam = cam
        self.ptz = self.cam.create_ptz_service()

    def GetServiceCapabilities(self):
        try:
            capabilities = self.ptz.GetServiceCapabilities()
            if ((capabilities is None) or (len(capabilities) == 0)):
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'The DUT did not send GetServiceCapabilitiesResponse message',
                'response': str(capabilities)}}
            else:
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None,
                'response': str(capabilities)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented'}}
            else:
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e)}}