from onvif import ONVIFCamera, exceptions
from time import sleep


class PTZTests:
    def __init__(self, cam):
        self.cam = cam
        self.event_service = self.cam.create_events_service()
        self.ptz = self.cam.create_ptz_service()
        self.media = self.cam.create_media_service()

    def GetCompatibleConfigurations(self):
        try:
            token = self.media.GetProfiles()[0]._token
            self.ptz.create_type('GetCompatibleConfigurations')
            configs = self.ptz.GetCompatibleConfigurations({'ProfileToken': token})
            if ((configs is None) or (len(configs) == 0)):
                return {'test_id': 1, 'name': 'GetCompatibleConfigurations', 'service': 'PTZ',
                'result': {'supported': False,
                'extension': 'The DUT did not send GetCompatibleConfigurationsResponse message',
                'response': str(configs) }}
            else:
                return {'test_id': 1, 'name': 'GetCompatibleConfigurations', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None, 'response': str(configs)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 1, 'name': 'GetCompatibleConfigurations', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "", 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 1, 'name': 'GetCompatibleConfigurations', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetConfiguration(self):
        try:
            ptz_token = self.media.GetProfiles()[0].PTZConfiguration._token
            config = self.ptz.GetConfiguration({'PTZConfigurationToken': ptz_token})
            if ((config is None) or (len(config) == 0)):
                return {'test_id': 2, 'name': 'GetConfiguration', 'service': 'PTZ',
                'result': {'supported': False,
                'extension': 'The DUT did not send GetConfigurationResponse message',
                'response': str(config) }}
            else:
                return {'test_id': 2, 'name': 'GetConfiguration', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None, 'response': str(config)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 2, 'name': 'GetConfiguration', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'test_id': 2, 'name': 'GetConfiguration', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetConfigurationOptions(self):
        try:
            ptz_token = self.media.GetProfiles()[0].PTZConfiguration._token
            configs = self.ptz.GetConfigurationOptions({'ConfigurationToken': ptz_token})
            if ((configs is None) or (len(configs) == 0)):    
                return {'test_id': 3, 'name': 'GetConfigurationOptions', 'service': 'PTZ',
                'result': {'supported': False,
                'extension': 'The DUT did not send GetConfigurationOptionsResponse message',
                'response': str(configs) }}
            else:
                return {'test_id': 3, 'name': 'GetConfigurationOptions', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None, 'response': str(configs)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 3, 'name': 'GetConfigurationOptions', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'test_id': 3, 'name': 'GetConfigurationOptions', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetConfigurations(self):
        try:
            configs = self.ptz.GetConfigurations()
            if ((configs is None) or (len(configs) == 0)):    
                return {'test_id': 4, 'name': 'GetConfigurations', 'service': 'PTZ',
                'result': {'supported': False,
                'extension': 'The DUT did not send GetConfigurationsResponse message',
                'response': str(configs) }}
            else:
                return {'test_id': 4, 'name': 'GetConfigurations', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None, 'response': str(configs) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 4, 'name': 'GetConfigurations', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'test_id': 4, 'name': 'GetConfigurations', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}
    
    def GetNodes(self):
        try:
            nodes = self.ptz.GetNodes()
            if ((nodes is None) or (len(nodes) == 0)):    
                return {'test_id': 5, 'name': 'GetNodes', 'service': 'PTZ',
                'result': {'supported': False,
                'extension': 'The DUT did not send GetNodesResponse message',
                'response': str(nodes) }}
            else:
                return {'test_id': 5, 'name': 'GetNodes', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None, 'response': str(nodes) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 5, 'name': 'GetNodes', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'test_id': 5, 'name': 'GetNodes', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetNode(self):
        try:
            node_token = self.ptz.GetConfigurations()[0].NodeToken
            node = self.ptz.GetNode({'NodeToken': node_token})
            if ((node is None) or (len(node) == 0)):    
                return {'test_id': 6, 'name': 'GetNode', 'service': 'PTZ',
                'result': {'supported': False,
                'extension': 'The DUT did not send GetNodeResponse message',
                'response': str(node) }}
            else:
                return {'test_id': 6, 'name': 'GetNode', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None, 'response': str(node)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 6, 'name': 'GetNode', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'test_id': 6, 'name': 'GetNode', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def AbsoluteMove(self):
        try:
            token = self.media.GetProfiles()[0]._token
            # ptz_token = self.media.GetProfiles() [0].PTZConfiguration._token
            self.ptz.create_type("AbsoluteMove")
            pos = self.ptz.GetStatus({"ProfileToken": token}).Position
            x_z = pos.Zoom._x
            x = pos.PanTilt._x
            y = pos.PanTilt._y
            if x + 0.1 < 1:
                x1 = x + 0.1
            else:
                x1 = x - 0.1
            if y + 0.1 < 1:
                y1 = y + 0.1
            else:
                y1 = y - 0.1
            if x_z + 0.1 < 1:
                x_z1 = x_z + 0.1
            else:
                x_z1 = x_z - 0.1
            # print x_z
            self.ptz.AbsoluteMove({"ProfileToken": token, "Position":
                                  {"PanTilt": {"_x": x1, "_y": y1}, "Zoom": {"_x": x_z1}}})
            sleep(3)
            pos = self.ptz.GetStatus({"ProfileToken": token}).Position
            x_z = pos.Zoom._x
            x = pos.PanTilt._x
            y = pos.PanTilt._y
            dif1 = (round((x1-x), 6))
            dif2 = (round((y1-y), 6))
            dif3 = (round((x_z1-x_z), 6))
            if dif1 == 0.0 and dif2 == 0.0 and dif3 == 0.0:
                result = 'AbsoluteMove is supported, current coordinates: ' + str(x) + ' ' + str(y) + ' ' + str(x_z)
                return {'test_id': 7, 'name': 'AbsoluteMove', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(result)}}
            elif dif1 == 0.0 and dif2 == 0.0 and dif3 != 0.0:
                result = 'AbsoluteMove is supported, but Zoom does not work. Current coordinates: ' \
                           + str(x) + ' ' + str(y) + ' ' + str(x_z)
                return {'test_id': 7, 'name': 'AbsoluteMove', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': 'AbsoluteMove partly supported',
                                   'response': str(result)}}
            else:
                return {'test_id': 7, 'name': 'AbsoluteMove', 'service': 'PTZ',
                        'result': {'supported': False, 'extension': 'AbsoluteMove is not supported, '
                                                                    'camera does not move', 'response': ''}}
        except AttributeError:
            return {'test_id': 7, 'name': 'AbsoluteMove', 'service': 'PTZ',
                    'result': {'supported': False, 'extension': 'AbsoluteMove is not supported, AttributeError ',
                               'response': ''}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 7, 'name': 'AbsoluteMove', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'test_id': 7, 'name': 'AbsoluteMove', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetPresets(self):
        try:
            token = self.media.GetProfiles()[0]._token
            presets = self.ptz.GetPresets({'ProfileToken': token})
            if ((presets is None) or (len(presets) == 0)):    
                return {'test_id': 8, 'name': 'GetPresets', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not send GetPresetsResponse message',
                                'response': str(presets) }}
            else:
                return {'test_id': 8, 'name': 'GetPresets', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(presets)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 8, 'name': 'GetPresets', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'test_id': 8, 'name': 'GetPresets', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}
    
    def CreatePresetTour(self):
        try:
            token = self.media.GetProfiles()[0]._token
            tour = self.ptz.CreatePresetTour({'ProfileToken': token})
            self.ptz.RemovePresetTour({'ProfileToken': token, 'PresetTourToken': tour})
            if ((tour is None) or (len(tour) == 0)):
                return {'test_id': 9, 'name': 'CreatePresetTour', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not send CreatePresetTourResponse message',
                                'response': 'PresetTourToken: ' + str(tour) }}
            else:
                return {'test_id': 9, 'name': 'CreatePresetTour', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': 'PresetTourToken: ' + str(tour) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 9, 'name': 'CreatePresetTour', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'test_id': 9, 'name': 'CreatePresetTour', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetPresetTour(self):
        try:
            token = self.media.GetProfiles()[0]._token
            tour_token = self.ptz.CreatePresetTour({'ProfileToken': token})
            tour = self.ptz.GetPresetTour({'ProfileToken': token, 'PresetTourToken': tour_token})
            self.ptz.RemovePresetTour({'ProfileToken': token, 'PresetTourToken': tour_token})
            if ((tour is None) or (len(tour) == 0)):
                return {'test_id': 10, 'name': 'GetPresetTour', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not send GetPresetTourResponse message',
                                'response': str(tour) }}
            else:
                return {'test_id': 10, 'name': 'GetPresetTour', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(tour)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 10, 'name': 'GetPresetTour', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'test_id': 10, 'name': 'GetPresetTour', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetPresetTours(self):
        try:
            token = self.media.GetProfiles()[0]._token
            tours = self.ptz.GetPresetTours({'ProfileToken': token})
            if ((tours is None) or (len(tours) == 0)):
                return {'test_id': 11, 'name': 'GetPresetTour', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not send GetPresetToursResponse message',
                                'response': str(tours) }}
            else:
                return {'test_id': 11, 'name': 'GetPresetTours', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(tours) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 11, 'name': 'GetPresetTours', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'test_id': 11, 'name': 'GetPresetTours', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetPresetTourOptions(self):
        try:
            token = self.media.GetProfiles()[0]._token
            tour_token = self.ptz.CreatePresetTour({'ProfileToken': token})
            tour = self.ptz.GetPresetTourOptions({'ProfileToken': token, 'PresetTourToken': tour_token})
            self.ptz.RemovePresetTour({'ProfileToken': token, 'PresetTourToken': tour_token})
            if ((tour is None) or (len(tour) == 0)):
                return {'test_id': 12, 'name': 'GetPresetTourOptions', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not send GetPresetTourOptionsResponse message',
                                'response': str(tour) }}
            else:
                return {'test_id': 12, 'name': 'GetPresetTourOptions', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(tour) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 12, 'name': 'GetPresetTourOptions', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'test_id': 12, 'name': 'GetPresetTourOptions', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetServiceCapabilities(self):
        try:
            capabilities = self.ptz.GetServiceCapabilities()
            if ((capabilities is None) or (len(capabilities) == 0)):
                return {'test_id': 13, 'name': 'GetServiceCapabilities', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'The DUT did not send GetServiceCapabilitiesResponse message',
                'response': str(capabilities) }}
            else:
                return {'test_id': 13, 'name': 'GetServiceCapabilities', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None,
                'response': str(capabilities) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 13, 'name': 'GetServiceCapabilities', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "" }}
            else:
                return {'test_id': 13, 'name': 'GetServiceCapabilities', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetStatus(self):
        try:
            token = self.media.GetProfiles()[0]._token
            status = self.ptz.GetStatus({'ProfileToken': token})
            if ((status is None) or (len(status) == 0)):
                return {'test_id': 14, 'name': 'GetStatus', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not send GetStatusResponse message',
                                'response': str(status) }}
            else:
                return {'test_id': 14, 'name': 'GetStatus', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(status) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 14, 'name': 'GetStatus', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented'}}
            else:
                return {'test_id': 14, 'name': 'GetStatus', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def RemovePresetTour(self):
        try:
            token = self.media.GetProfiles()[0]._token
            token_1 = self.ptz.GetPresetTours({'ProfileToken': token})[-1]._token
            tour_token = self.ptz.CreatePresetTour({'ProfileToken': token})
            tour = self.ptz.GetPresetTour({'ProfileToken': token, 'PresetTourToken': tour_token})
            remove = self.ptz.RemovePresetTour({'ProfileToken': token, 'PresetTourToken': tour_token})
            token_2 = self.ptz.GetPresetTours({'ProfileToken': token})[-1]._token
            if (token_1 != token_2):
                return {'test_id': 15, 'name': 'RemovePresetTour', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not removed RemovePresetTour',
                                'response': str(tour) }}
            else:
                return {'test_id': 15, 'name': 'RemovePresetTour', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(tour) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 15, 'name': 'RemovePresetTour', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented'}}
            else:
                return {'test_id': 15, 'name': 'RemovePresetTour', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}