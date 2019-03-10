from onvif import ONVIFCamera


class AnalyticsTests:
    def __init__(self, ip, port, user, passw):
        self.ip = ip
        self.port = port
        self.user = user
        self.passw = passw
        self.cam = ONVIFCamera(self.ip, self.port, self.user, self.passw)
        self.media = self.cam.create_media_service()
        self.analytics = self.cam.create_analytics_service()
        self.analytics_rules = self.cam.create_analytics_rules_service()
        self.vactoken = self.media.GetProfiles()[0].VideoAnalyticsConfiguration._token        

    def GetServiceCapabilities(self):
        capabilities = self.analytics.GetServiceCapabilities()
        if (len(capabilities) > 0):
            return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Analytics',
            'result': {'supported': True, 'extension': None, 'response': str(capabilities)}}
        else:
            return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Analytics',
            'result': {'supported': False, 'extension': 'The DUT did not send GetServiceCapabilitiesResponse message',
            'response': str(capabilities)}}

    def GetSupportedAnalyticsModules(self):
        supported_modules = self.analytics.GetSupportedAnalyticsModules({'ConfigurationToken': self.vactoken})
        if (supported_modules != []):
            return {'test_id': 1, 'name': 'GetSupportedAnalyticsModules', 'service': 'Analytics',
            'result': {'supported': True, 'extension': None, 'response': str(supported_modules)}}
        else:
            return {'test_id': 1, 'name': 'GetSupportedAnalyticsModules', 'service': 'Analytics',
            'result': {'supported': False, 'extension': 'The DUT did not send GetSupportedAnalyticsModulesResponse message',
            'response': str(supported_modules)}}

    def GetAnalyticsModules(self):
        modules = self.analytics.GetAnalyticsModules({'ConfigurationToken': self.vactoken})
        if (modules != []):
            return {'test_id': 2, 'name': 'GetAnalyticsModules', 'service': 'Analytics',
            'result': {'supported': True, 'extension': None, 'response': str(modules)}}
        else:
            return {'test_id': 2, 'name': 'GetAnalyticsModules', 'service': 'Analytics',
            'result': {'supported': False, 'extension': 'The DUT did not send GetAnalyticsModulesResponse message',
            'response': str(modules)}}

    def GetSupportedRules(self):
        supported_rules = self.analytics_rules.GetSupportedRules({'ConfigurationToken': self.vactoken})
        if (supported_rules != []):
            return {'test_id': 7, 'name': 'GetSupportedRules', 'service': 'Analytics',
            'result': {'supported': True, 'extension': None, 'response': str(supported_rules)}}
        else:
            return {'test_id': 7, 'name': 'GetSupportedRules', 'service': 'Analytics',
            'result': {'supported': False, 'extension': 'The DUT did not send GetSupportedAnalyticsModulesResponse message',
            'response': str(supported_rules)}}

    def GetRules(self):
        rules = self.analytics_rules.GetRules({'ConfigurationToken': self.vactoken})
        if (rules != []):
            return {'test_id': 8, 'name': 'GetRules', 'service': 'Analytics',
            'result': {'supported': True, 'extension': None, 'response': str(rules)}}
        else:
            return {'test_id': 8, 'name': 'GetRules', 'service': 'Analytics',
            'result': {'supported': False, 'extension': 'The DUT did not send GetAnalyticsModulesResponse message',
            'response': str(rules)}}

#response = analytics.CreateAnalyticsModules({'ConfigurationToken': vactoken, 'AnalyticsModule': {'_Name': 'tt:FieldDetectorEngine', '_Type': 'tt:FieldDetectorEngine', 'Parameters': {'SimpleItem': {'_Name': 'Sensitivity', '_Type': 'xs:integer'}}}})
#response = analytics_rules.DeleteRules({'ConfigurationToken': vactoken, 'RuleName': 'MyLineDetector4'})
