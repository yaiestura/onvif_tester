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
                return {'name': 'GetCompatibleConfigurations', 'service': 'PTZ',
                'result': {'supported': False,
                'extension': 'The DUT did not send GetCompatibleConfigurationsResponse message',
                'response': str(configs) }}
            else:
                return {'name': 'GetCompatibleConfigurations', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None, 'response': str(configs)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetCompatibleConfigurations', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "", 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetCompatibleConfigurations', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetConfiguration(self):
        try:
            ptz_token = self.media.GetProfiles()[0].PTZConfiguration._token
            config = self.ptz.GetConfiguration({'PTZConfigurationToken': ptz_token})
            if ((config is None) or (len(config) == 0)):
                return {'name': 'GetConfiguration', 'service': 'PTZ',
                'result': {'supported': False,
                'extension': 'The DUT did not send GetConfigurationResponse message',
                'response': str(config) }}
            else:
                return {'name': 'GetConfiguration', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None, 'response': str(config)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetConfiguration', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'name': 'GetConfiguration', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetConfigurationOptions(self):
        try:
            ptz_token = self.media.GetProfiles()[0].PTZConfiguration._token
            configs = self.ptz.GetConfigurationOptions({'ConfigurationToken': ptz_token})
            if ((configs is None) or (len(configs) == 0)):    
                return {'name': 'GetConfigurationOptions', 'service': 'PTZ',
                'result': {'supported': False,
                'extension': 'The DUT did not send GetConfigurationOptionsResponse message',
                'response': str(configs) }}
            else:
                return {'name': 'GetConfigurationOptions', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None, 'response': str(configs)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetConfigurationOptions', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'name': 'GetConfigurationOptions', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetConfigurations(self):
        try:
            configs = self.ptz.GetConfigurations()
            if ((configs is None) or (len(configs) == 0)):    
                return {'name': 'GetConfigurations', 'service': 'PTZ',
                'result': {'supported': False,
                'extension': 'The DUT did not send GetConfigurationsResponse message',
                'response': str(configs) }}
            else:
                return {'name': 'GetConfigurations', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None, 'response': str(configs) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetConfigurations', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'name': 'GetConfigurations', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetNodes(self):
        try:
            nodes = self.ptz.GetNodes()
            if ((nodes is None) or (len(nodes) == 0)):
                return {'name': 'GetNodes', 'service': 'PTZ',
                'result': {'supported': False,
                'extension': 'The DUT did not send GetNodesResponse message',
                'response': str(nodes) }}
            else:
                return {'name': 'GetNodes', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None, 'response': str(nodes) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetNodes', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'name': 'GetNodes', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetNode(self):
        try:
            node_token = self.ptz.GetConfigurations()[0].NodeToken
            node = self.ptz.GetNode({'NodeToken': node_token})
            if ((node is None) or (len(node) == 0)):    
                return {'name': 'GetNode', 'service': 'PTZ',
                'result': {'supported': False,
                'extension': 'The DUT did not send GetNodeResponse message',
                'response': str(node) }}
            else:
                return {'name': 'GetNode', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None, 'response': str(node)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetNode', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'name': 'GetNode', 'service': 'PTZ',
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
                return {'name': 'AbsoluteMove', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(result)}}
            elif dif1 == 0.0 and dif2 == 0.0 and dif3 != 0.0:
                result = 'AbsoluteMove is supported, but Zoom does not work. Current coordinates: ' \
                           + str(x) + ' ' + str(y) + ' ' + str(x_z)
                return {'name': 'AbsoluteMove', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': 'AbsoluteMove partly supported',
                                   'response': str(result)}}
            else:
                return {'name': 'AbsoluteMove', 'service': 'PTZ',
                        'result': {'supported': False, 'extension': 'AbsoluteMove is not supported, '
                                                                    'camera does not move', 'response': ''}}
        except AttributeError:
            return {'name': 'AbsoluteMove', 'service': 'PTZ',
                    'result': {'supported': False, 'extension': 'AbsoluteMove is not supported, AttributeError ',
                               'response': ''}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'AbsoluteMove', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'name': 'AbsoluteMove', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetPresets(self):
        try:
            token = self.media.GetProfiles()[0]._token
            presets = self.ptz.GetPresets({'ProfileToken': token})
            if ((presets is None) or (len(presets) == 0)):    
                return {'name': 'GetPresets', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not send GetPresetsResponse message',
                                'response': str(presets) }}
            else:
                return {'name': 'GetPresets', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(presets)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetPresets', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'name': 'GetPresets', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def CreatePresetTour(self):
        try:
            token = self.media.GetProfiles()[0]._token
            tour = self.ptz.CreatePresetTour({'ProfileToken': token})
            self.ptz.RemovePresetTour({'ProfileToken': token, 'PresetTourToken': tour})
            if ((tour is None) or (len(tour) == 0)):
                return {'name': 'CreatePresetTour', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not send CreatePresetTourResponse message',
                                'response': 'PresetTourToken: ' + str(tour) }}
            else:
                return {'name': 'CreatePresetTour', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': 'PresetTourToken: ' + str(tour) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'CreatePresetTour', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'name': 'CreatePresetTour', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetPresetTour(self):
        try:
            token = self.media.GetProfiles()[0]._token
            tour_token = self.ptz.CreatePresetTour({'ProfileToken': token})
            tour = self.ptz.GetPresetTour({'ProfileToken': token, 'PresetTourToken': tour_token})
            self.ptz.RemovePresetTour({'ProfileToken': token, 'PresetTourToken': tour_token})
            if ((tour is None) or (len(tour) == 0)):
                return {'name': 'GetPresetTour', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not send GetPresetTourResponse message',
                                'response': str(tour) }}
            else:
                return {'name': 'GetPresetTour', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(tour)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetPresetTour', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'name': 'GetPresetTour', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetPresetTours(self):
        try:
            token = self.media.GetProfiles()[0]._token
            tours = self.ptz.GetPresetTours({'ProfileToken': token})
            if ((tours is None) or (len(tours) == 0)):
                return {'name': 'GetPresetTour', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not send GetPresetToursResponse message',
                                'response': str(tours) }}
            else:
                return {'name': 'GetPresetTours', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(tours) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetPresetTours', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'name': 'GetPresetTours', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetPresetTourOptions(self):
        try:
            token = self.media.GetProfiles()[0]._token
            tour_token = self.ptz.CreatePresetTour({'ProfileToken': token})
            tour = self.ptz.GetPresetTourOptions({'ProfileToken': token, 'PresetTourToken': tour_token})
            self.ptz.RemovePresetTour({'ProfileToken': token, 'PresetTourToken': tour_token})
            if ((tour is None) or (len(tour) == 0)):
                return {'name': 'GetPresetTourOptions', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not send GetPresetTourOptionsResponse message',
                                'response': str(tour) }}
            else:
                return {'name': 'GetPresetTourOptions', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(tour) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetPresetTourOptions', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': "" }}
            else:
                return {'name': 'GetPresetTourOptions', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetServiceCapabilities(self):
        try:
            capabilities = self.ptz.GetServiceCapabilities()
            if ((capabilities is None) or (len(capabilities) == 0)):
                return {'name': 'GetServiceCapabilities', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'The DUT did not send GetServiceCapabilitiesResponse message',
                'response': str(capabilities) }}
            else:
                return {'name': 'GetServiceCapabilities', 'service': 'PTZ',
                'result': {'supported': True, 'extension': None,
                'response': str(capabilities) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetServiceCapabilities', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "" }}
            else:
                return {'name': 'GetServiceCapabilities', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def GetStatus(self):
        try:
            token = self.media.GetProfiles()[0]._token
            status = self.ptz.GetStatus({'ProfileToken': token})
            if ((status is None) or (len(status) == 0)):
                return {'name': 'GetStatus', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not send GetStatusResponse message',
                                'response': str(status) }}
            else:
                return {'name': 'GetStatus', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(status) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetStatus', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented'}}
            else:
                return {'name': 'GetStatus', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def RemovePresetTour(self):
        try:
            token = self.media.GetProfiles()[0]._token
            token_1 = self.ptz.GetPresetTours({'ProfileToken': token})[-1]._token
            tour_token = self.ptz.CreatePresetTour({'ProfileToken': token})
            sleep(0.5)
            tour = self.ptz.GetPresetTour({'ProfileToken': token, 'PresetTourToken': tour_token})
            remove = self.ptz.RemovePresetTour({'ProfileToken': token, 'PresetTourToken': tour_token})
            sleep(0.5)
            token_2 = self.ptz.GetPresetTours({'ProfileToken': token})[-1]._token
            if (token_1 != token_2):
                return {'name': 'RemovePresetTour', 'service': 'PTZ',
                        'result': {'supported': False,
                                'extension': 'The DUT did not removed RemovePresetTour',
                                'response': str(tour) }}
            else:
                return {'name': 'RemovePresetTour', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': None, 'response': str(tour) }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'RemovePresetTour', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented'}}
            else:
                return {'name': 'RemovePresetTour', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': ""}}

    def ContinuousMove(self):

        try:
            token = self.media.GetProfiles()[0]._token
            req_move = self.ptz.create_type('ContinuousMove')
            req_move.ProfileToken = token
            req_stop = self.ptz.create_type('Stop')
            req_stop.ProfileToken = token

            def left(req_move, req_stop, ptz, token):
                sleep(0.3)
                self.ptz.Stop(req_stop)
                pos1 = self.cam.returnpos(ptz, token).x
                req_move.Velocity.Zoom._x = 0.0
                req_move.Velocity.PanTilt._x = -0.5
                req_move.Velocity.PanTilt._y = 0.0
                self.ptz.ContinuousMove(req_move)
                sleep(1)
                self.ptz.Stop(req_stop)
                sleep(0.3)
                pos2 = self.cam.returnpos(ptz, token).x
                return pos1 - pos2

            def right(req_move, req_stop, ptz, token):
                sleep(0.3)
                self.ptz.Stop(req_stop)
                pos1 = self.cam.returnpos(ptz, token).x
                req_move.Velocity.Zoom._x = 0.0
                req_move.Velocity.PanTilt._x = 0.5
                req_move.Velocity.PanTilt._y = 0.0
                self.ptz.ContinuousMove(req_move)
                sleep(1)
                self.ptz.Stop(req_stop)
                sleep(0.3)
                pos2 = self.cam.returnpos(ptz, token).x
                return pos1 - pos2

            def zoom_in(req_move, req_stop, ptz, token):
                sleep(0.3)
                self.ptz.Stop(req_stop)
                pos1 = self.cam.returnpos(ptz, token).x_z
                req_move.Velocity.PanTilt._x = 0.0
                req_move.Velocity.PanTilt._y = 0.0
                req_move.Velocity.Zoom._x = 0.1
                self.ptz.ContinuousMove(req_move)
                sleep(1)
                self.ptz.Stop(req_stop)
                sleep(0.3)
                pos2 = self.cam.returnpos(ptz, token).x_z
                return pos1 - pos2

            def zoom_out(req_move, req_stop, ptz, token):
                sleep(0.3)
                self.ptz.Stop(req_stop)
                pos1 = self.cam.returnpos(ptz, token).x_z
                req_move.Velocity.PanTilt._x = 0.0
                req_move.Velocity.PanTilt._y = 0.0
                req_move.Velocity.Zoom._x = -0.1
                self.ptz.ContinuousMove(req_move)
                sleep(1)
                self.ptz.Stop(req_stop)
                sleep(0.3)
                pos2 = self.cam.returnpos(ptz, token).x_z
                return pos1 - pos2

            pos = self.cam.returnpos(self.ptz, token)
            # print 'x ', pos.x, ' y ', pos   .y, ' z ', pos.x_z
            if pos is False:
                return {'name': 'ContinuousMove', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Continuous Move is not supported',
                 'response': "Continuous Move is not supported", 'report': 'Continuous Move is not supported'}}
            elif pos.x is not False and pos.y is not False:
                if round(left(req_move, req_stop, self.ptz, token), 1) + round(right(req_move, req_stop, self.ptz, token), 1) == 0:
                    if pos.x_z is False:
                        return {'name': 'ContinuousMove', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': 'Continuous Move is partly supported, zoom does not work',
                        'response': 'Continuous Move is partly supported, zoom does not work, current coordinates: {}'.format(pos),
                        'report': 'Continuous Move is partly supported, zoom does not work, current coordinates: {}'.format(pos)}}
                    elif (round(zoom_in(req_move, req_stop, self.ptz, token), 1) + round(zoom_out(req_move, req_stop, self.ptz, token), 1)) == 0:
                        return {'name': 'ContinuousMove', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': 'Continuous Move is supported',
                        'response': "Continuous Move is supported, current coordinates: {}".format(pos), 'report': 'Continuous Move is supported, current coordinates: {}'.format(pos)}}
                    elif (round(zoom_out(req_move, req_stop, self.ptz, token), 1) + round(zoom_in(req_move, req_stop, self.ptz, token), 1)) == 0:
                        return {'name': 'ContinuousMove', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': 'Continuous Move is supported',
                        'response': "Continuous Move is supported, current coordinates: {}".format(pos),
                        'report': "Continuous Move is supported, current coordinates: {}".format(pos)}}
                    else:
                        return {'name': 'ContinuousMove', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': 'Continuous Move is partly supported, zoom does not work',
                        'response': 'Continuous Move is partly supported, zoom does not work, current coordinates: {}'.format(pos),
                        'report': 'Continuous Move is partly supported, zoom does not work, current coordinates: {}'.format(pos)}}
                elif round(right(req_move, req_stop, self.ptz, token), 1) + round(left(req_move, req_stop, self.ptz, token), 1) == 0:
                    if pos.x_z is False:
                        return {'name': 'ContinuousMove', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': 'Continuous Move is partly supported, zoom does not work',
                        'response': 'Continuous Move is partly supported, zoom does not work, current coordinates: {}'.format(pos),
                        'report': 'Continuous Move is partly supported, zoom does not work, current coordinates: {}'.format(pos)}}
                    elif round(zoom_in(req_move, req_stop, self.ptz, token), 1) + round(zoom_out(req_move, req_stop, self.ptz, token), 1) == 0:
                        return {'name': 'ContinuousMove', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': 'Continuous Move is supported',
                        'response': "Continuous Move is supported, current coordinates: {}".format(pos),
                        'report': "Continuous Move is supported, current coordinates: {}".format(pos)}}
                    elif round(zoom_out(req_move, req_stop, self.ptz, token), 1) + round(zoom_in(req_move, req_stop, self.ptz, token), 1) == 0:
                        return {'name': 'ContinuousMove', 'service': 'PTZ',
                        'result': {'supported': True, 'extension': 'Continuous Move is supported',
                        'response': "Continuous Move is supported, current coordinates: {}".format(pos),
                        'report': "Continuous Move is supported, current coordinates: {}".format(pos)}}
                    else:
                        return {'name': 'ContinuousMove', 'service': 'PTZ',
                        'result': {'supported': False, 'extension': 'Continuous Move is not supported',
                        'response': "Continuous Move is not supported", 'report': 'Continuous Move is not supported'}}
                else:
                    return {'name': 'ContinuousMove', 'service': 'PTZ',
                    'result': {'supported': False, 'extension': 'Continuous Move is not supported. Camera does not move',
                    'response': "Continuous Move is not supported. Camera does not move",
                    'report': 'Continuous Move is not supported. Camera does not move'}}
            elif pos.x is False and pos.y is False and pos.x_z >= 0:
                if round(zoom_in(req_move, req_stop, ptz, token), 1) + round(zoom_out(req_move, req_stop, self.ptz, token), 1) == 0:
                    return {'name': 'ContinuousMove', 'service': 'PTZ',
                    'result': {'supported': True, 'extension': 'Continuous Move is partly supported, only zoom works',
                    'response': 'Continuous Move is partly supported, only zoom works, current coordinates: {}'.format(pos),
                    'report': 'Continuous Move is partly supported, only zoom works, current coordinates: {}'.format(pos)}}
                elif round(zoom_out(req_move, req_stop, ptz, token), 1) + round(zoom_in(req_move, req_stop, self.ptz, token), 1) == 0:
                    return {'name': 'ContinuousMove', 'service': 'PTZ',
                    'result': {'supported': True, 'extension': 'Continuous Move is partly supported, only zoom works',
                    'response': 'Continuous Move is partly supported, only zoom works, current coordinates: {}'.format(pos),
                    'report': 'Continuous Move is partly supported, only zoom works, current coordinates: {}'.format(pos)}}
                else:
                    return {'name': 'ContinuousMove', 'service': 'PTZ',
                    'result': {'supported': False, 'extension': 'Continuous Move is not supported',
                    'response': "Continuous Move is not supported", 'report': 'Continuous Move is not supported'}}
            else:
                return {'name': 'ContinuousMove', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Continuous Move is not supported',
                 'response': "Continuous Move is not supported", 'report': 'Continuous Move is not supported'}}

        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'ContinuousMove', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "Optional Action Not Implemented", 'report': 'Optional Action Not Implemented'}}
            else:
                return {'name': 'ContinuousMove', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e), 'response': "Continuous Move is not supported",
                'report': 'Continuous Move is not supported'}}

    def RelativeMove(self):
        try:
            token = self.media.GetProfiles()[0]._token
            rel_move = self.ptz.create_type('RelativeMove')
            rel_move.ProfileToken = token
            req_stop = self.ptz.create_type('Stop')
            req_stop.ProfileToken = token

            node = self.ptz.GetNodes()[0]

            def move_x(x, token, req_stop, rel_move, ptz):
                ptz.Stop(req_stop)
                pos1 = self.cam.returnpos(ptz, token).x
                rel_move.Translation.PanTilt._x = x
                rel_move.Translation.PanTilt._y = 0
                rel_move.Translation.Zoom._x = 0
                ptz.RelativeMove(rel_move)
                sleep(1)
                ptz.Stop(req_stop)
                pos2 = self.cam.returnpos(ptz, token).x
                # print 'Pan ' + str(pos1 - pos2)
                return pos1 - pos2

            def move_y(y, token, req_stop, rel_move, ptz):
                ptz.Stop(req_stop)
                pos1 = self.cam.returnpos(ptz, token).y
                rel_move.Translation.PanTilt._x = 0
                rel_move.Translation.PanTilt._y = y
                rel_move.Translation.Zoom._x = 0
                ptz.RelativeMove(rel_move)
                sleep(1)
                ptz.Stop(req_stop)
                pos2 = self.cam.returnpos(ptz, token).y
                # print 'Tilt ' + str(pos1 - pos2)
                return pos1 - pos2

            def move_z(z, token, req_stop, rel_move, ptz):
                ptz.Stop(req_stop)
                pos1 = self.cam.returnpos(ptz, token).x_z
                rel_move.Translation.PanTilt._x = 0
                rel_move.Translation.PanTilt._y = 0
                rel_move.Translation.Zoom._x = z
                ptz.RelativeMove(rel_move)
                sleep(1)
                ptz.Stop(req_stop)
                pos2 = self.cam.returnpos(ptz, token).x_z
                # print 'Zoom ' + str(pos1 - pos2)
                return pos1 - pos2

            d = 0.05
            pos = self.cam.returnpos(self.ptz, token)
            movx = movy = movz = False
            if pos.x is not False:
                try:
                    mov1 = round(move_x(d, token, req_stop, rel_move, self.ptz), 2)
                    mov2 = round(move_x(-d, token, req_stop, rel_move, self.ptz), 2)
                    if mov1 + mov2 == 0 and not mov1 == mov2 == 0:
                        movx = True
                    else:
                        mov3 = round(move_x(-d, token, req_stop, rel_move, self.ptz), 2)
                        mov4 = round(move_x(d, token, req_stop, rel_move, self.ptz), 2)
                        if mov3 + mov4 == 0 and not mov3 == mov4 == 0:
                            movx = True
                except exceptions.ONVIFError:
                    movx = False
            if pos.y is not False:
                try:
                    mov1 = round(move_y(d, token, req_stop, rel_move, self.ptz), 2)
                    mov2 = round(move_y(-d, token, req_stop, rel_move, self.ptz), 2)
                    if mov1 + mov2 == 0 and not mov1 == mov2 == 0:
                        movy = True
                    else:
                        mov3 = round(move_y(-d, token, req_stop, rel_move, self.ptz), 2)
                        mov4 = round(move_y(d, token, req_stop, rel_move, self.ptz), 2)
                        if mov3 + mov4 == 0 and not mov3 == mov4 == 0:
                            movy = True
                except exceptions.ONVIFError:
                    movy = False
            if pos.x_z is not False:
                try:
                    mov1 = round(move_z(-0.2, token, req_stop, rel_move, self.ptz), 2)
                    mov2 = round(move_z(0.2, token, req_stop, rel_move, self.ptz), 2)
                    # print 'mov1 ' + str(mov1) + ' mov2 ' + str(mov2)
                    if mov1 + mov2 == 0 and not mov1 == mov2 == 0:
                        movz = True
                    else:
                        mov3 = round(move_z(0.2, token, req_stop, rel_move, self.ptz), 2)
                        mov4 = round(move_z(-0.2, token, req_stop, rel_move, self.ptz), 2)
                        if mov3 + mov4 == 0 and not mov3 == mov4 == 0:
                            movz = True
                except exceptions.ONVIFError:
                    movz = False

            if movx and movz and movy:
                return {'name': 'RelativeMove', 'service': 'PTZ',
                'result': {'supported': True, 'extension': 'Relative Move is supported',
                'response': 'Relative Move is supported',
                'report': 'Relative Move is supported'}}
            elif movx and movy and not movz:
                return {'name': 'RelativeMove', 'service': 'PTZ',
                'result': {'supported': True,
                'extension': 'Relative Move is supported partly, only PanTilt works',
                'response': 'Relative Move is supported partly, only PanTilt works',
                'report': 'Relative Move is supported partly, only PanTilt works'}}
            elif movx and movz and not movy:
                return {'name': 'RelativeMove', 'service': 'PTZ',
                'result': {'supported': True,
                'extension': 'Relative Move is supported partly, only PanZoom works',
                'response': 'Relative Move is supported partly, only PanZoom works',
                'report': 'Relative Move is supported partly, only PanZoom works'}}
            elif movy and movz and not movx:
                return {'name': 'RelativeMove', 'service': 'PTZ',
                'result': {'supported': True,
                'extension': 'Relative Move is supported partly, only TiltZoom works',
                'response': 'Relative Move is supported partly, only TiltZoom works',
                'report': 'Relative Move is supported partly, only TiltZoom works'}}
            elif movz and not movx and not movy:
                return {'name': 'RelativeMove', 'service': 'PTZ',
                'result': {'supported': True,
                'extension': 'Relative Move is supported partly, only Zoom works',
                'response': 'Relative Move is supported partly, only Zoom works',
                'report': 'Relative Move is supported partly, only Zoom works'}}
            elif movy and not movx and not movz:
                return {'name': 'RelativeMove', 'service': 'PTZ',
                'result': {'supported': True,
                'extension': 'Relative Move is supported partly, only Tilt works',
                'response': 'Relative Move is supported partly, only Tilt works',
                'report': 'Relative Move is supported partly, only Tilt works'}}
            elif movx and not movy and not movz:
                return {'name': 'RelativeMove', 'service': 'PTZ',
                'result': {'supported': True,
                'extension': 'Relative Move is supported partly, only Pan works',
                'response': 'Relative Move is supported partly, only Pan works',
                'report': 'Relative Move is supported partly, only Pan works'}}
            else:
                return {'name': 'RelativeMove', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Relative Move is not supported',
                'response': "Relative Move is not supported",
                'report': 'Relative Move is not supported'}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'RelativeMove', 'service': 'PTZ',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "Optional Action Not Implemented",
                'report': 'Optional Action Not Implemented'}}
            else:
                return {'name': 'RelativeMove', 'service': 'PTZ',
                'result': {'supported': False, 'extension': str(e),
                'response': "Relative Move is not supported",
                'report': 'Relative Move is not supported'}}