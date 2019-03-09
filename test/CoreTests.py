class CoreTests:
	def __init__(self, camera):
		self.camera = camera
		
import csv
from flask import jsonify
from onvif import ONVIFCamera
from Naked.toolshed.shell import execute_js


class Core_Test:
    def __init__(self, ip, port, user, passw):
        self.ip = ip
        self.port = port
        self.user = user
        self.passw = passw
        self.cam = ONVIFCamera(self.ip, self.port, self.user, self.passw)

    def GetSupportedServices(self):
        try:
            devicemgmt_service = self.cam.create_devicemgmt_service()
            dmgmt = 'Supported'
        except:
            dmgmt = 'Not Supported'

        try:
            media_service = self.cam.create_media_service()
            media = 'Supported'
        except:
            media = 'Not Supported'

        try:
            imaging_service = self.cam.create_imaging_service()
            imaging = 'Supported'
        except:
            imaging = 'Not Supported'

        try:
            analytics_service = self.cam.create_analytics_service()
            analytics = 'Supported'
        except:
            analytics = 'Not Supported'

        try:
            ptz_service = self.cam.create_ptz_service()
            ptz = 'Supported'
        except:
            ptz = 'Not Supported'

        try:
            io_service = self.cam.create_deviceio_service()
            io = 'Supported'
        except:
            io = 'Not Supported'

        try:
            events_service = self.cam.create_events_service()
            events = 'Supported'
        except:
            events = 'Not Supported'

        try:
            replay_service = self.cam.create_replay_service()
            replay = 'Supported'
        except:
            replay = 'Not Supported'

        try:
            recording_service = self.cam.create_recording_service()
            recording = 'Supported'
        except:
            recording = 'Not Supported'

        try:
            search_service = self.cam.create_search_service()
            search = 'Supported'
        except:
            search = 'Not Supported'

        try:
            pullpoint_service = self.cam.create_pullpoint_service()
            pullpoint = 'Supported'
        except:
            pullpoint = 'Not Supported'

        try:
            receiver_service = self.cam.create_receiver_service()
            receiver = 'Supported'
        except:
            receiver = 'Not Supported'

        return {id: 0, name: 'GetSupportedServices', service: 'Core',
            result: {[works: True, extension: None, response: {
                'Devicemgmt': dmgmt,
                'Media': media,
                'Imaging': imaging
                'Analytics': analytics
                'PTZ': ptz
                'DeviceIO': io
                'Events': events
                'Replay': replay
                'Recording': recording
                'Search': search
                'Pullpoint': pullpoint
                'Receiver' receiver
            }]}}
        

    def GetCapabilities(self):
        capabilities = self.cam.devicemgmt.GetCapabilities()
        if (len(capabilities) > 0):
            return {id: 1, name: 'GetCapabilities', service: 'Core',
            result: {[works: True, extension: None, response: capabilities]}}
        else:
            return {id: 1, name: 'GetCapabilities', service: 'Core',
            result: {[works: False, extension: 'The DUT did not send GetCapabilitiesResponse message',
            response: capabilities]}}

    def GetDiscoveryMode(self):
        request = self.cam.devicemgmt.GetDiscoveryMode()
        if (request):
             return request + ' GetDiscoveryMode works'
        else:
            return 'GetDiscoveryMode does not work'

    def SetDiscoveryMode(self):
        get1 = self.cam.devicemgmt.GetDiscoveryMode()
        if (get1 == 'Discoverable'):
            set1 = self.cam.devicemgmt.SetDiscoveryMode({'DiscoveryMode': 'NonDiscoverable'})
            get2 = self.cam.devicemgmt.GetDiscoveryMode()
            self.cam.devicemgmt.SetDiscoveryMode({'DiscoveryMode': get1})
            if (get1 != get2 ):
                return 'Left Discoverable, SetDiscoveryMode works'
            else:
                return 'SetDiscoveryMode does not work'
        elif (get1 == 'NonDiscoverable'):
            set1 = self.cam.devicemgmt.SetDiscoveryMode({'DiscoveryMode': 'Discoverable'})
            get2 = self.cam.devicemgmt.GetDiscoveryMode()
            self.cam.devicemgmt.SetDiscoveryMode({'DiscoveryMode': get1})
            if (get1 != get2):
                return 'left Nondiscoverable, SetDiscoveryMode works'
            else:
                return 'SetDiscoveryMode does not work'
        else:
            return 'It seems GetDiscoveryMode does not work'

    def GetScopes(self):
        response = self.cam.devicemgmt.GetScopes()
        if (len(response) > 0):
            #print response
            return 'GetScopes works'
        else:
            return 'GetScopes does not work'

    def AddScopes(self):
        item = "onvif://www.onvif.org/type/test"
        add = self.cam.devicemgmt.AddScopes({'ScopeItem': item})
        execute_js('start_probe.js')
        gett = self.cam.devicemgmt.GetScopes()
        if (gett != []):
            gett = self.cam.devicemgmt.GetScopes()[-1].ScopeItem
        execute_js('start_probe.js')
        self.cam.devicemgmt.RemoveScopes({'ScopeItem': item})
        if (item == gett):
            return 'AddScopes works'
        else:
            return 'AddScopes does not work'

    def RemoveScopes(self):
        item = "onvif://www.onvif.org/type/test"
        add = self.cam.devicemgmt.AddScopes({'ScopeItem': item})
        # execute_js('start_probe.js')
        remove = self.cam.devicemgmt.RemoveScopes({'ScopeItem': item})
        # execute_js('start_probe.js')
        gett = self.cam.devicemgmt.GetScopes()
        if (gett != []):
            gett = self.cam.devicemgmt.GetScopes()[-1].ScopeItem
        if (item != gett):
            return 'RemoveScopes works'
        else:
            return 'RemoveScopes does not work'

    def GetHostname(self):
        name = self.cam.devicemgmt.GetHostname()
        if (name):
            return 'GetHostname works'
        else:
            return 'GetHostname does not work'

    def SetHostname(self):
        get1 = self.cam.devicemgmt.GetHostname().Name
        name = "Onviftest1"
        set1 = self.cam.devicemgmt.SetHostname({'Name': name})
        get2 = self.cam.devicemgmt.GetHostname().Name
        self.cam.devicemgmt.SetHostname({'Name': get1})
        if (get1 != get2):
            return 'SetHostname works'
        else:
            return 'SetHostname does not work'

    def GetNetworkInterfaces(self):
        interfaces = self.cam.devicemgmt.GetNetworkInterfaces()
        if (interfaces != []):
            return 'GetNetworkInterfaces works'
        else:
            return 'GetNetworkInterfaces does not work'

    def GetDNS(self):
        dns = self.cam.devicemgmt.GetDNS()
        #print dns
        if (dns != []):
            return 'GetDNS works'
        else:
            return 'GetDNS does not work'

    def GetNetworkProtocols(self):
        protocols = self.cam.devicemgmt.GetNetworkProtocols()
        if (protocols != []):
            return 'GetNetworkProtocols works'
        else:
            return 'GeetNetworkProtocols does not work'

    def GetNetworkDefaultGateway(self):
        gateways = self.cam.devicemgmt.GetNetworkDefaultGateway()
        #print gateways
        if (gateways != []):
            return 'GetNetworkDefaultGateway works'
        else:
            return 'GetNetworkDefaultGateway does not work'

    def SetNetworkDefaultGateway(self): #"192.168.11.1"
        default = str(self.cam.devicemgmt.GetNetworkDefaultGateway().IPv4Address[0])
        #print default
        new = '10.1.0.1'
        set1 = self.cam.devicemgmt.SetNetworkDefaultGateway({'IPv4Address': new})
        execute_js('start_probe.js')
        get1 = str(self.cam.devicemgmt.GetNetworkDefaultGateway().IPv4Address[0])
        execute_js('start_probe.js')
        self.cam.devicemgmt.SetNetworkDefaultGateway({'IPv4Address': default})
        if (get1 == new):
            return 'SetNetworkDefaultGateway works'
        else:
            return 'SetNetworkDefaultGateway does not work'


    def GetDeviceInformation(self):
        info = self.cam.devicemgmt.GetDeviceInformation()
        if (info != []):
            return 'GetDeviceInformation works'
        else:
            return 'GetDeviceInformation does not work'

    def GetUsers(self):
        users = self.cam.devicemgmt.GetUsers()
        if (users != []):
            return 'GetUsers works'
        else:
            return 'GetUsers does not work'

    def DeleteUsers(self):
        set1 = self.cam.devicemgmt.CreateUsers({'Username': 'ONVIFTest', 'Password': 'lalala', 'UserLevel': 'User'})
        delete = self.cam.devicemgmt.DeleteUsers({'Username':'ONVIFTest'})
        if (delete != []):
            return 'DeleteUsers works'
        else:
            return 'DeleteUsers does not work'

    def GetNTP(self):
        ntp = self.cam.devicemgmt.GetNTP()
        if (ntp != []):
            return 'GetNTP works'
        else:
            return 'GetNTP does not work'

    def GetServices(self):
        services = self.cam.devicemgmt.GetServices()
        if (services != []):
            return 'GetServices works'
        else:
            return 'GetServices does not work'

    def GetSystemDateAndTime(self):
        datetime = self.cam.devicemgmt.GetSystemDateAndTime()
        if (datetime != []):
            return 'GetSystemDateAndTime works'
        else:
            return 'GetSystemDateAndTime does not work'

    def GetSystemUris(self):
        uri = self.cam.devicemgmt.GetSystemUris()
        if (uri != []):
            return 'GetSystemUris works'
        else:
            return 'GetSystemUris does not work'
		