from onvif import ONVIFCamera


class DeviceIOTests:
    def __init__(self, cam):
        self.cam = cam
        self.media = self.cam.create_media_service()
        self.io = self.cam.create_deviceio_service()

    def GetServiceCapabilities(self):
        try:
            capabilities = self.io.GetServiceCapabilities()
            if ((capabilities is None) or (len(capabilities) == 0)):
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'The DUT did not send GetServiceCapabilitiesResponse message',
                'response': str(capabilities)}}
            else:
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'deviceio',
                'result': {'supported': True, 'extension': None,
                'response': str(capabilities)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
				'response': "" }}
            else:
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'deviceio',
                'result': {'supported': False, 'extension': str(e), 'response': "" }}

    def GetAudioSourceConfiguration(self):
        try:
            asctoken = self.media.GetProfiles()[0].AudioSourceConfiguration._token
            response = self.io.GetAudioSourceConfiguration({'AudioSourceToken': asctoken})
            if ((response is None) or (len(response) == 0)):
                return {'test_id': 1, 'name': 'GetAudioSourceConfiguration', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'The DUT did not send GetAudioSourceConfigurationResponse message',
                'response': str(response)}}
            else:
                return {'test_id': 1, 'name': 'GetAudioSourceConfiguration', 'service': 'deviceio',
                'result': {'supported': True, 'extension': None,
                'response': str(response)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 1, 'name': 'GetAudioSourceConfiguration', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
				'response': "" }}
            else:
                return {'test_id': 1, 'name': 'GetAudioSourceConfiguration', 'service': 'deviceio',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetAudioSourceConfigurationOptions(self):
        try:
            asctoken = self.media.GetProfiles()[0].AudioSourceConfiguration._token
            response = self.io.GetAudioSourceConfiguration({'AudioSourceToken': asctoken})
            if ((response is None) or (len(response) == 0)):
                return {'test_id': 2, 'name': 'GetAudioSourceConfigurationOptions', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'The DUT did not send GetAudioSourceConfigurationOptionsResponse message',
                'response': str(response)}}
            else:
                return {'test_id': 2, 'name': 'GetAudioSourceConfigurationOptions', 'service': 'deviceio',
                'result': {'supported': True, 'extension': None,
                'response': str(response)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 2, 'name': 'GetAudioSourceConfigurationOptions', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
				'response': "" }}
            else:
                return {'test_id': 2, 'name': 'GetAudioSourceConfigurationOptions', 'service': 'deviceio',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetAudioSources(self):
        try:
            response = self.io.GetAudioSources()
            if ((response is None) or (len(response) == 0)):
                return {'test_id': 3, 'name': 'GetAudioSources', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'The DUT did not send GetAudioSourcesResponse message',
                'response': str(response)}}
            else:
                return {'test_id': 3, 'name': 'GetAudioSources', 'service': 'deviceio',
                'result': {'supported': True, 'extension': None,
                'response': str(response)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 3, 'name': 'GetAudioSources', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
				'response': "" }}
            else:
                return {'test_id': 3, 'name': 'GetAudioSources', 'service': 'deviceio',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetDigitalInputs(self):
        try:
            response = self.io.GetDigitalInputs()
            if ((response is None) or (len(response) == 0)):
                return {'test_id': 4, 'name': 'GetDigitalInputs', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'The DUT did not send GetDigitalInputsResponse message',
                'response': str(response)}}
            else:
                return {'test_id': 4, 'name': 'GetDigitalInputs', 'service': 'deviceio',
                'result': {'supported': True, 'extension': None,
                'response': str(response)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 4, 'name': 'GetDigitalInputs', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
				'response': "" }}
            else:
                return {'test_id': 4, 'name': 'GetDigitalInputs', 'service': 'deviceio',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetRelayOutputs(self):
        try:
            response = self.io.GetRelayOutputs()
            if ((response is None) or (len(response) == 0)):
                return {'test_id': 5, 'name': 'GetRelayOutputs', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'The DUT did not send GetRelayOutputsResponse message',
                'response': str(response)}}
            else:
                return {'test_id': 5, 'name': 'GetRelayOutputs', 'service': 'deviceio',
                'result': {'supported': True, 'extension': None,
                'response': str(response)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 5, 'name': 'GetRelayOutputs', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
				'response': ""}}
            else:
                return {'test_id': 5, 'name': 'GetRelayOutputs', 'service': 'deviceio',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetSerialPorts(self):
        try:
            response = self.io.GetSerialPorts()
            if ((response is None) or (len(response) == 0)):
                return {'test_id': 6, 'name': 'GetSerialPorts', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'The DUT did not send GetSerialPortsResponse message',
                'response': str(response)}}
            else:
               return {'test_id': 6, 'name': 'GetSerialPorts', 'service': 'deviceio',
               'result': {'supported': True, 'extension': None,
               'response': str(response)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 6, 'name': 'GetSerialPorts', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
				'response': ""}}
            else:
                 return {'test_id': 6, 'name': 'GetSerialPorts', 'service': 'deviceio',
                 'result': {'supported': False, 'extension': str(e),
				 'response': ""}}

    def GetVideoOutputs(self):
        try:
            response = self.io.GetVideoOutputs()
            if ((response is None) or (len(response) == 0)):
                return {'test_id': 7, 'name': 'GetVideoOutputs', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'The DUT did not send GetVideoOutputsResponse message',
                'response': str(response)}}
            else:
                return {'test_id': 7, 'name': 'GetVideoOutputs', 'service': 'deviceio',
                'result': {'supported': True, 'extension': None,
                'response': str(response)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 7, 'name': 'GetVideoOutputs', 'service': 'deviceio',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
				'response': ""}}
            else:
                return {'test_id': 7, 'name': 'GetVideoOutputs', 'service': 'deviceio',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}
