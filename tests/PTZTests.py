from onvif import ONVIFCamera

class PTZTests:    
    def __init__(self, cam):
        self.cam = cam
        self.ptz = self.cam.create_ptz_service()
    

    def GetServiceCapabilities(self):
        capabilities = self.ptz.GetServiceCapabilities()
        if (len(capabilities) > 0):
            return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'PTZ',
            'result': {'supported': True, 'extension': None, 'response': str(capabilities)}}
        else:
            return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'PTZ',
            'result': {'supported': False, 'extension': 'The DUT did not send GetServiceCapabilitiesResponse message',
            'response': str(capabilities)}}