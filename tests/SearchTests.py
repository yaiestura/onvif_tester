from onvif import ONVIFCamera

class SearchTests:    
    def __init__(self, cam):
        self.cam = cam
        self.search = self.cam.create_search_service()
    

    def GetServiceCapabilities(self):
        capabilities = self.search.GetServiceCapabilities()
        if (len(capabilities) > 0):
            return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Search',
            'result': {'supported': True, 'extension': None, 'response': str(capabilities)}}
        else:
            return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Search',
            'result': {'supported': False, 'extension': 'The DUT did not send GetServiceCapabilitiesResponse message',
            'response': str(capabilities)}}