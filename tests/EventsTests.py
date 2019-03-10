from onvif import ONVIFCamera
import random
import string
import datetime
import requests


class EventsTests:
    
    def __init__(self, cam):
        self.cam = cam
        self.event_service = self.cam.create_events_service()

    def GetEventProperties(self):
        properties = self.event_service.GetEventProperties()
        topic = str(properties.TopicNamespaceLocation[0])
        status_code = requests.get(topic).status_code
        if(len(properties) > 0):
            return {'test_id': 0, 'name': 'GetEventProperties', 'service': 'Events',
            'result': {'supported': True, 'extension': None, 'response': str(properties)}}
        elif((len(properties) > 0) and (status_code != 200)):
            return {'test_id': 0, 'name': 'GetEventProperties', 'service': 'Events',
            'result': {'supported': True, 'extension': 'DUT does not return a valid topic namespace. Status Code != 200',
			'response': str(properties)}}
        elif((len(properties) > 0) and (len(properties.TopicExpressionDialect) < 2)):
            return {'test_id': 0, 'name': 'GetEventProperties', 'service': 'Events',
            'result': {'supported': True, 'extension': 'None or only one Mandatory TopicExpressionDialects are supported by the DUT',
			'response': str(properties)}}
        elif((len(properties) > 0) and (len(properties.TopicExpressionDialect) < 2) and (status_code != 200)):
            return {'test_id': 0, 'name': 'GetEventProperties', 'service': 'Events',
            'result': {'supported': True, 'extension': 'None or only one Mandatory TopicExpressionDialects are supported by the DUT. DUT does not return a valid topic namespace.',
			'response': str(properties)}}
        elif((len(properties) > 0) and (len(properties.MessageContentFilterDialect) < 1)):
            return {'test_id': 0, 'name': 'GetEventProperties', 'service': 'Events',
            'result': {'supported': True, 'extension': 'Mandatory MessageContentFilterDialect is not supported by the DUT. None or only one Mandatory TopicExpressionDialects are supported by the DUT.',
			'response': str(properties)}}
        elif((len(properties) > 0) and (len(properties.MessageContentFilterDialect) < 1) and (status_code != 200)):
            return {'test_id': 0, 'name': 'GetEventProperties', 'service': 'Events',
            'result': {'supported': True, 'extension': 'Mandatory MessageContentFilterDialect is not supported by the DUT. None or only one Mandatory TopicExpressionDialects are supported by the DUT. DUT does not return a valid topic namespace.',
			'response': str(properties)}}
        elif((len(properties) > 0) and (len(properties.MessageContentFilterDialect) < 1) and (len(properties.TopicExpressionDialect) < 2)):
            return {'test_id': 0, 'name': 'GetEventProperties', 'service': 'Events',
            'result': {'supported': True, 'extension': 'Mandatory MessageContentFilterDialect is not supported by the DUT',
			'response': str(properties)}}
        elif((len(properties) > 0) and (len(properties.MessageContentFilterDialect)) < 1 and (len(properties.TopicExpressionDialect)) < 2 and (status_code != 200)):
            return {'test_id': 0, 'name': 'GetEventProperties', 'service': 'Events',
            'result': {'supported': True, 'extension': 'Mandatory MessageContentFilterDialect is not supported by the DUT. DUT does not return a valid topic namespace.',
			'response': str(properties)}}
        else:
            return {'test_id': 0, 'name': 'GetEventProperties', 'service': 'Events',
            'result': {'supported': False, 'extension': 'The DUT did not send a GetEventPropertiesResponse message',
			'response': str(properties)}}

    def CreatePullPointSubscription(self):
        subs = self.event_service.CreatePullPointSubscription()
        curr = subs.CurrentTime
        term = subs.TerminationTime
        delt = int((term - curr).total_seconds())
        if(subs != []):
            if (delt >= 10):
                return {'test_id': 1, 'name': 'CreatePullPointSubscription', 'service': 'Events',
                'result': {'supported': True, 'extension': 'Valid values for SubscriptionReference CurrentTime and TerminationTime are returned(TerminationTime >= CurrentTime + InitialTerminationTime)',
				'response': str(subs)}}
            else:
                return {'test_id': 1, 'name': 'CreatePullPointSubscription', 'service': 'Events',
                'result': {'supported': False, 'extension': 'Returned response with TerminationTime < CurrentTime + InitialTerminationTime).', 'response': str(subs)}}
        else:
            return {'test_id': 1, 'name': 'CreatePullPointSubscription', 'service': 'Events',
            'result': {'supported': False, 'extension': 'The DUT did not send CreatePullPointSubscriptionResponse message',
			'response': str(subs)}}
			

    def GetServiceCapabilities(self):
        capabilities = self.event_service.GetServiceCapabilities()
        if (len(capabilities) > 0):
            return {'test_id': 2, 'name': 'GetServiceCapabilities', 'service': 'Events',
            'result': {'supported': True, 'extension': None, 'response': str(capabilities)}}
        else:
            return {'test_id': 2, 'name': 'GetServiceCapabilities', 'service': 'Events',
            'result': {'supported': False, 'extension': 'The DUT did not send valid GetServiceCapabilitiesResponse message',
			'response': str(capabilities)}}

    # def PullMessages(self):
    #     self.cam.create_pullpoint_service()
    #     service = self.cam.pullpoint.zeep_client._get_service('EventService')
    #     port = self.cam.pullpoint.zeep_client._get_port(service, 'PullPointSubscription')
    #     port.binding_options['address'] = onvif_camera.xaddrs['http://www.onvif.org/ver10/events/wsdl/PullPointSubscription']
    #     plp = onvif_camera.pullpoint.zeep_client.bind('EventService', 'PullPointSubscription')
    #     response = plp.PullMessages(Timeout = timedelta(seconds = 20), MessageLimit = 100)
    #     return response
