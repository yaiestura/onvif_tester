from onvif import ONVIFCamera


class ReplayTests:
    def __init__(self, cam):
        self.cam = cam
        self.replay = self.cam.create_replay_service()

    def GetServiceCapabilities(self):
        try:
            capabilities = self.replay.GetServiceCapabilities()
            if ((capabilities is None) or (len(capabilities) == 0)):
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Replay',
                'result': {'supported': False, 'extension': 'The DUT did not send GetServiceCapabilitiesResponse message',
                'response': str(capabilities)}}
            else:
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Replay',
                'result': {'supported': True, 'extension': None,
                'response': str(capabilities)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Replay',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented'}}
            else:
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Replay',
                'result': {'supported': False, 'extension': str(e)}}

    def GetReplayConfiguration(self):
        try:
            configuration = self.replay.GetReplayConfiguration()
            if ((configuration is None) or (len(configuration) == 0)):
                return {'test_id': 1, 'name': 'GetReplayConfiguration', 'service': 'Replay',
                'result': {'supported': False, 'extension': 'The DUT did not send Mandatory GetReplayConfigurationResponse message',
                'response': str(configuration)}}
            else:
                return {'test_id': 1, 'name': 'GetReplayConfiguration', 'service': 'Replay',
                'result': {'supported': True, 'extension': None,
                'response': str(configuration)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 1, 'name': 'GetReplayConfiguration', 'service': 'Replay',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented'}}
            else:
                return {'test_id': 1, 'name': 'GetReplayConfiguration', 'service': 'Replay',
                'result': {'supported': False, 'extension': str(e)}}

    def SetReplayConfiguration(self):
        try:
            timeout1 = self.replay.GetReplayConfiguration().SessionTimeout
            response = self.replay.SetReplayConfiguration({'Configuration': {'SessionTimeout': 'PT25S'}})
            timeout2 = self.replay.GetReplayConfiguration().SessionTimeout
            back = self.replay.SetReplayConfiguration({'Configuration': {'SessionTimeout': timeout1}})
            timeout3 = self.replay.GetReplayConfiguration().SessionTimeout
            if (timeout2 == timeout1):
			    return {'test_id': 2, 'name': 'SetReplayConfiguration', 'service': 'Replay',
                'result': {'supported': False, 'extension': 'The DUT did not set SetReplayConfiguration SessionTimeout to PT25S',
                'response': 'Response: '+ str(response) + 'Set Timeout failed, ' + str(timeout2)}}        
            elif ((timeout2 != timeout1) and (response is None)):
                return {'test_id': 2, 'name': 'SetReplayConfiguration', 'service': 'Replay',
                'result': {'supported': True, 'extension': 'The DUT SetReplayConfiguration SessionTimeout to PT25S, but did not send valid SetReplayConfigurationResponse message',
                'response': 'Response: '+ str(response) + ', set Timeout to ' + str(timeout2) + ', returned back to ' + str(timeout3)}}
            elif ((timeout2 != timeout1) and (response is not None)):
                return {'test_id': 2, 'name': 'SetReplayConfiguration', 'service': 'Replay',
                'result': {'supported': True, 'extension': None,
                'response': 'Response: '+ str(response) + ', set Timeout to ' + str(timeout2) + ', returned back to ' + str(timeout3)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 2, 'name': 'SetReplayConfiguration', 'service': 'Replay',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented'}}
            else:
                return {'test_id': 2, 'name': 'SetReplayConfiguration', 'service': 'Replay',
                'result': {'supported': False, 'extension': str(e)}}