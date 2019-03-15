from onvif import ONVIFCamera

class ReplayTests:    
    def __init__(self, cam):
        self.cam = cam
        self.replay = self.cam.create_replay_service()
    

    def GetServiceCapabilities(self):
        capabilities = self.replay.GetServiceCapabilities()
        if (len(capabilities) > 0):
            return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Replay',
            'result': {'supported': True, 'extension': None, 'response': str(capabilities)}}
        else:
            return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Replay',
            'result': {'supported': False, 'extension': 'The DUT did not send GetServiceCapabilitiesResponse message',
            'response': str(capabilities)}}