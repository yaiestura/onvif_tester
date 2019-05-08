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
                'response': "", 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 0, 'name': 'GetServiceCapabilities', 'service': 'Analytics',
                'result': {'supported': False, 'extension': str(e), 'response': "" }}

    def GetSupportedAnalyticsModules(self):
        try:
            report = ''
            supported_modules = self.analytics.GetSupportedAnalyticsModules({'ConfigurationToken': self.vactoken})
            if ((supported_modules is None) or (len(supported_modules) == 0)):
                return {'test_id': 1, 'name': 'GetSupportedAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'The DUT did not send GetSupportedAnalyticsModulesResponse message',
                'response': str(supported_modules)}}
            else:
                for count, modules in enumerate(supported_modules.AnalyticsModuleDescription):
                    report = report + modules._Name+ '\n'
                report = "Device has {} analytics modules that are supported by the given VideoAnalyticsConfiguration\n".format(count + 1) + report[:-1]
                return {'test_id': 1, 'name': 'GetSupportedAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': True, 'extension': None,
                'response': str(supported_modules), 'report': report}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 1, 'name': 'GetSupportedAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "", 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 1, 'name': 'GetSupportedAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetAnalyticsModules(self):
        try:
            report = ''
            analytics_modules = self.analytics.GetAnalyticsModules({'ConfigurationToken': self.vactoken})
            if ((analytics_modules is None) or (len(analytics_modules) == 0)):
                return {'test_id': 2, 'name': 'GetAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'The DUT did not send GetAnalyticsModulesResponse message',
                'response': str(analytics_modules)}}
            else:
                for count, modules in enumerate(analytics_modules):
                    report = report + modules._Name+ '\n'
                report = "Device has {} currently assigned set of analytics modules of a VideoAnalyticsConfiguration\n".format(count + 1) + report[:-1]
                return {'test_id': 2, 'name': 'GetAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': True, 'extension': None,
                'response': str(analytics_modules), 'report': report}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 2, 'name': 'GetAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "", 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 2, 'name': 'GetAnalyticsModules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': str(e), 'response': "" }}

    def GetSupportedRules(self):
        try:
            report = ''
            supported_rules = self.analytics_rules.GetSupportedRules({'ConfigurationToken': self.vactoken})
            if ((supported_rules is None) or (len(supported_rules) == 0)):
                return {'test_id': 3, 'name': 'GetSupportedRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'The DUT did not send GetSupportedAnalyticsModulesResponse message',
                'response': str(supported_rules)}}
            else:
                for count, rules in enumerate(supported_rules.RuleDescription):
                    report = report + rules._Name + ' Rule'+ '\n'
                report = "Device has {} rules that are supported by the given VideoAnalyticsConfiguration\n".format(count + 1) + report[:-1]
                return {'test_id': 3, 'name': 'GetSupportedRules', 'service': 'Analytics',
                'result': {'supported': True, 'extension': None,
                'response': str(supported_rules), 'report': report}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 3, 'name': 'GetSupportedRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "", 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 3, 'name': 'GetSupportedRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetRules(self):
        try:
            report = ''
            rules_list = self.analytics_rules.GetRules({'ConfigurationToken': self.vactoken})
            if ((rules_list is None) or (len(rules_list) == 0)):
                return {'test_id': 4, 'name': 'GetRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'The DUT did not send GetAnalyticsModulesResponse message',
                'response': str(rules_list)}}
            else:
                for count, rules in enumerate(rules_list):
                    report = report + rules._Name + '\n'
                report = "Device has {} currently assigned set of rules of a VideoAnalyticsConfiguration\n".format(count + 1) + report[:-1]
                return {'test_id': 4, 'name': 'GetRules', 'service': 'Analytics',
                'result': {'supported': True, 'extension': None,
                'response': str(rules_list), 'report': report}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 4, 'name': 'GetRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "", 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 4, 'name': 'GetRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': str(e), 
                'response': "" }}

    def DeleteRules(self):
        try:
            rules = self.analytics_rules.DeleteRules({'ConfigurationToken': self.vactoken, 'RuleName': 'MyLineDetector4'})
            if ((rules is None) or (len(rules) == 0)):
                return {'test_id': 4, 'name': 'DeleteRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'The DUT did not delete Rule MyLineDetector4',
                'response': str(rules)}}
            else:
                return {'test_id': 4, 'name': 'DeleteRules', 'service': 'Analytics',
                'result': {'supported': True, 'extension': None,
                'response': str(rules)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 4, 'name': 'DeleteRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "", 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 4, 'name': 'DeleteRules', 'service': 'Analytics',
                'result': {'supported': False, 'extension': str(e),
                'response': "" }}

#response = analytics.CreateAnalyticsModules({'ConfigurationToken': vactoken, 'AnalyticsModule': {'_Name': 'tt:FieldDetectorEngine', '_Type': 'tt:FieldDetectorEngine', 'Parameters': {'SimpleItem': {'_Name': 'Sensitivity', '_Type': 'xs:integer'}}}})
#response = analytics_rules.DeleteRules({'ConfigurationToken': vactoken, 'RuleName': 'MyLineDetector4'})
