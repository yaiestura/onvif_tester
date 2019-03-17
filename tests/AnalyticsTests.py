from onvif import ONVIFCamera


class AnalyticsTests:
    def __init__(self, cam):
        self.cam = cam
        self.media = self.cam.create_media_service()
        self.analytics = self.cam.create_analytics_service()
        self.analytics_rules = self.cam.create_analytics_rules_service()
        self.vactoken = self.media.GetProfiles()[0].VideoAnalyticsConfiguration._token

    def GetServiceCapabilities(self):
        try:
            capabilities = self.analytics.GetServiceCapabilities()
            if ((capabilities is None) or (len(capabilities) == 0)):
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'The DUT did not send GetServiceCapabilitiesResponse message',
                'response': str(capabilities)}}
            else:
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Analytics',
                'result': {'supported': True, 'extension': None,
                'response': str(capabilities)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "" }}
            else:
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Analytics',
                'result': {'supported': False, 'extension': str(e), 'response': "" }}

    def GetSupportedAnalyticsModules(self):
        try:
            supported_modules = self.analytics.GetSupportedAnalyticsModules({'ConfigurationToken': self.vactoken})
            if ((supported_modules is None) or (len(supported_modules) == 0)):
                return {'test_id': 1, 'name': 'GetSupportedAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'The DUT did not send GetSupportedAnalyticsModulesResponse message',
                'response': str(supported_modules)}}
            else:
                return {'test_id': 1, 'name': 'GetSupportedAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': True, 'extension': None,
                'response': str(supported_modules)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 1, 'name': 'GetSupportedAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "" }}
            else:
                return {'test_id': 1, 'name': 'GetSupportedAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetAnalyticsModules(self):
        try:
            modules = self.analytics.GetAnalyticsModules({'ConfigurationToken': self.vactoken})
            if ((modules is None) or (len(modules) == 0)):
                return {'test_id': 2, 'name': 'GetAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'The DUT did not send GetAnalyticsModulesResponse message',
                'response': str(modules)}}
            else:
                return {'test_id': 2, 'name': 'GetAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': True, 'extension': None,
                'response': str(modules)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 2, 'name': 'GetAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "" }}
            else:
                return {'test_id': 2, 'name': 'GetAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': str(e), 'response': "" }}

    def GetSupportedRules(self):
        try:
            supported_rules = self.analytics_rules.GetSupportedRules({'ConfigurationToken': self.vactoken})
            if ((supported_rules is None) or (len(supported_rules) == 0)):
                return {'test_id': 3, 'name': 'GetSupportedRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'The DUT did not send GetSupportedAnalyticsModulesResponse message', 'response': str(supported_rules)}}
            else:
                return {'test_id': 3, 'name': 'GetSupportedRules', 'service': 'Analytics',
                'result': {'supported': True, 'extension': None,
                'response': str(supported_rules)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 3, 'name': 'GetSupportedRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "" }}
            else:
                return {'test_id': 3, 'name': 'GetSupportedRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetRules(self):
        try:
            rules = self.analytics_rules.GetRules({'ConfigurationToken': self.vactoken})
            if ((rules is None) or (len(rules) == 0)):
                return {'test_id': 4, 'name': 'GetRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'The DUT did not send GetAnalyticsModulesResponse message',
                'response': str(rules)}}
            else:
                return {'test_id': 4, 'name': 'GetRules', 'service': 'Analytics',
                'result': {'supported': True, 'extension': None,
                'response': str(rules)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 4, 'name': 'GetRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'test_id': 4, 'name': 'GetRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': str(e), 
                'response': "" }}

    def DeleteRules(self):
        try:
            rules = self.analytics_rules.DeleteRules({'ConfigurationToken': self.vactoken, 'RuleName': 'MyLineDetector4'})
            if ((rules is None) or (len(rules) == 0)):
                return {'test_id': 4, 'name': 'GetRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'The DUT did not delete Rule MyLineDetector4',
                'response': str(rules)}}
            else:
                return {'test_id': 4, 'name': 'GetRules', 'service': 'Analytics',
                'result': {'supported': True, 'extension': None,
                'response': str(rules)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 4, 'name': 'GetRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "" }}
            else:
                return {'test_id': 4, 'name': 'GetRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': str(e),
                'response': "" }}

#response = analytics.CreateAnalyticsModules({'ConfigurationToken': vactoken, 'AnalyticsModule': {'_Name': 'tt:FieldDetectorEngine', '_Type': 'tt:FieldDetectorEngine', 'Parameters': {'SimpleItem': {'_Name': 'Sensitivity', '_Type': 'xs:integer'}}}})
#response = analytics_rules.DeleteRules({'ConfigurationToken': vactoken, 'RuleName': 'MyLineDetector4'})
