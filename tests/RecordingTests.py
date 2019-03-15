from onvif import ONVIFCamera

class RecordingTests:    
    def __init__(self, cam):
        self.cam = cam
        self.recording = self.cam.create_recording_service()
    

    def GetServiceCapabilities(self):
        capabilities = self.recording.GetServiceCapabilities()
        if (len(capabilities) > 0):
            return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Recording',
            'result': {'supported': True, 'extension': None, 'response': str(capabilities)}}
        else:
            return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Recording',
            'result': {'supported': False, 'extension': 'The DUT did not send GetServiceCapabilitiesResponse message',
            'response': str(capabilities)}}
