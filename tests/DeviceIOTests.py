from onvif import ONVIFCamera

class DeviceIOTests:    
    def __init__(self, cam):
        self.cam = cam
        self.media = self.cam.create_media_service()
        self.asctoken = self.media.GetProfiles()[0].AudioSourceConfiguration._token
        self.vsctoken = self.media.GetProfiles()[0].VideoSourceConfiguration._token
        self.io = self.cam.create_deviceio_service()
    
    def GetServiceCapabilities(self):
        capabilities = self.io.GetServiceCapabilities()
        if ((capabilities is not None) or (len(capabilities) > 0)):
            return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'deviceio',
            'result': {'supported': True, 'extension': None, 'response': str(capabilities)}}
        else:
            return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'deviceio',
            'result': {'supported': False, 'extension': 'The DUT did not send GetServiceCapabilitiesResponse message',
            'response': str(capabilities)}}

    def GetAudioSourceConfiguration(self):
        response = self.io.GetAudioSourceConfiguration({'AudioSourceToken': self.asctoken})
        if ((response is not None) or (len(response) > 0)):
            return {'test_id': 1, 'name': 'GetAudioSourceConfiguration', 'service': 'deviceio',
            'result': {'supported': True, 'extension': None, 'response': str(response)}}
        else:
            return {'test_id': 1, 'name': 'GetAudioSourceConfiguration', 'service': 'deviceio',
            'result': {'supported': False, 'extension': 'The DUT did not send GetAudioSourceConfigurationResponse message',
            'response': str(response)}}

    def GetAudioSourceConfigurationOptions(self):
        response = self.io.GetAudioSourceConfiguration({'AudioSourceToken': self.asctoken})
        if ((response is not None) or (len(response) > 0)):
            return {'test_id': 2, 'name': 'GetAudioSourceConfigurationOptions', 'service': 'deviceio',
            'result': {'supported': True, 'extension': None, 'response': str(response)}}
        else:
            return {'test_id': 2, 'name': 'GetAudioSourceConfigurationOptions', 'service': 'deviceio',
            'result': {'supported': False, 'extension': 'The DUT did not send GetAudioSourceConfigurationOptionsResponse message',
            'response': str(response)}}

    def GetAudioSources(self):
        response = self.io.GetAudioSources()
        if ((response is not None) or (len(response) > 0)):
            return {'test_id': 3, 'name': 'GetAudioSources', 'service': 'deviceio',
            'result': {'supported': True, 'extension': None, 'response': str(response)}}
        else:
            return {'test_id': 3, 'name': 'GetAudioSources', 'service': 'deviceio',
            'result': {'supported': False, 'extension': 'The DUT did not send GetAudioSourcesResponse message',
            'response': str(response)}}

    def GetDigitalInputs(self):
        response = self.io.GetDigitalInputs()
        if ((response is not None) or (len(response) > 0)):
            return {'test_id': 4, 'name': 'GetDigitalInputs', 'service': 'deviceio',
            'result': {'supported': True, 'extension': None, 'response': str(response)}}
        else:
            return {'test_id': 4, 'name': 'GetDigitalInputs', 'service': 'deviceio',
            'result': {'supported': False, 'extension': 'The DUT did not send GetDigitalInputsResponse message',
            'response': str(response)}}

    def GetRelayOutputs(self):
        response = self.io.GetRelayOutputs()
        if ((response is not None) or (len(response) > 0)):
            return {'test_id': 5, 'name': 'GetRelayOutputs', 'service': 'deviceio',
            'result': {'supported': True, 'extension': None, 'response': str(response)}}
        else:
            return {'test_id': 5, 'name': 'GetRelayOutputs', 'service': 'deviceio',
            'result': {'supported': False, 'extension': 'The DUT did not send GetRelayOutputsResponse message',
            'response': str(response)}}

    def GetSerialPorts(self):
        response = self.io.GetSerialPorts()
        if ((response is not None) or (len(response) > 0)):
            return {'test_id': 5, 'name': 'GetSerialPorts', 'service': 'deviceio',
            'result': {'supported': True, 'extension': None, 'response': str(response)}}
        else:
            return {'test_id': 5, 'name': 'GetSerialPorts', 'service': 'deviceio',
            'result': {'supported': False, 'extension': 'The DUT did not send GetSerialPortsResponse message',
            'response': str(response)}}