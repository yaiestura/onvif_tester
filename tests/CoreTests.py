from onvif import ONVIFCamera, ONVIFError
from utils.probe_match import probe_match
from time import sleep
import time
import re

class CoreTests:
    def __init__(self, cam):
        self.cam = cam

    def GetSupportedServices(self):
        services_list = [
            'Devicemgmt', 'Media', 'Imaging', 'Analytics',
            'PTZ', 'DeviceIO', 'Events', 'Replay',
            'Recording', 'Search', 'Pullpoint', 'Receiver'
        ]

        services_status = []

        for service_name in services_list:
            name = service_name.lower()
            try:
                service = self.cam.get_service(name)
                services_status.append({
                    "name": service_name,
                    "supported": service is not None
                })
            except ONVIFError as e:
                services_status.append({
                    "name": service_name,
                    "supported": False
                })

        return {
            'test_id': 0,
            'service': 'Device',
            'name': 'GetSupportedServices',
            'result': {
                'supported': True,
                'extension': None,
                'response': services_status
            }

        }

    def GetCapabilities(self):
        try:
            capabilities = self.cam.devicemgmt.GetCapabilities()
            if (len(capabilities) > 0):
                return {'test_id': 1, 'name': 'Device Capabilities', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(capabilities)}}
            else:
                return {'test_id': 1, 'name': 'Device Capabilities', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetCapabilitiesResponse message',
                'response': str(capabilities), 'report': 'Not Supported'}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 1, 'name': 'Device Capabilities', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 1, 'name': 'Device Capabilities', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetDiscoveryMode(self):
        try:
            request = self.cam.devicemgmt.GetDiscoveryMode()
            if (request):
                return {'test_id': 2, 'name': 'GetDiscoveryMode', 'service': 'Device',
                'result': {'supported': True, 'extension': 'This operation got the discovery mode of a device',
                'response': str(request), 'report': 'Device currently is {}'.format(str(request)) }}
            else:
                return {'test_id': 2, 'name': 'GetDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetDiscoveryModeResponse message',
                'response': str(request)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 2, 'name': 'GetDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 2, 'name': 'GetDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def SetDiscoveryMode(self):
        try:
            get1 = self.cam.devicemgmt.GetDiscoveryMode()
            if (get1 == 'Discoverable'):
                set1 = self.cam.devicemgmt.SetDiscoveryMode({'DiscoveryMode': 'NonDiscoverable'})
                get2 = self.cam.devicemgmt.GetDiscoveryMode()
                self.cam.devicemgmt.SetDiscoveryMode({'DiscoveryMode': get1})
                if (get1 != get2 ):
                    return {'test_id': 3, 'name': 'SetDiscoveryMode', 'service': 'Device',
                    'result': {'supported': True, 'extension': 'Was Discoverable, Set NonDiscoverable, Left Discoverable',
                    'response': str(set1)}}
                else:
                    return {'test_id': 3, 'name': 'SetDiscoveryMode', 'service': 'Device',
                    'result': {'supported': False, 'extension': 'DiscoveryMode was Discoverable, the DUT did not SetDiscoveryMode as NonDiscoverable',
                    'response': str(set1)}}
            elif (get1 == 'NonDiscoverable'):
                set1 = self.cam.devicemgmt.SetDiscoveryMode({'DiscoveryMode': 'Discoverable'})
                get2 = self.cam.devicemgmt.GetDiscoveryMode()
                self.cam.devicemgmt.SetDiscoveryMode({'DiscoveryMode': get1})
                if (get1 != get2):
                    return {'test_id': 3, 'name': 'SetDiscoveryMode', 'service': 'Device',
                    'result': {'supported': True, 'extension': 'Was NonDiscoverable, Set Discoverable, Left NonDiscoverable',
                    'response': str(set1)}}
                else:
                    return {'test_id': 3, 'name': 'SetDiscoveryMode', 'service': 'Device',
                    'result': {'supported': False, 'extension': 'DiscoveryMode was NonDiscoverable, the DUT did not SetDiscoveryMode as Discoverable',
                    'response': str(set1)}}
            else:
                return {'test_id': 3, 'name': 'SetDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send SetDiscoveryModeResponse message',
                'response': str(set1)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 3, 'name': 'SetDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 3, 'name': 'SetDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetScopes(self):
        try:
            scopes = self.cam.devicemgmt.GetScopes()
            report = ''
            for count, item in enumerate(scopes):
                report = report + item.ScopeItem + '\n'
            report = "Device has {} scope items:\n".format(count+1) + report[:-1]
            if (len(scopes) > 0):
                return {'test_id': 4, 'name': 'GetScopes', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(scopes),
                'report': report}}
            else:
                return {'test_id': 4, 'name': 'GetScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetScopesResponse message. The DUT scope list does not have one or more mandatory scope entry.',
                'response': str(scopes), 'report': 'The DUT did not send GetScopesResponse message\nThe DUT scope list does not have one or more mandatory scope entry.'}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 4, 'name': 'GetScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 4, 'name': 'GetScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def AddScopes(self):
        try:
            item = "onvif://www.onvif.org/add/scope" + str(time.time())
            add = self.cam.devicemgmt.AddScopes({'ScopeItem': item})
            probe_match()
            gett = self.cam.devicemgmt.GetScopes()
            if (gett != []):
                gett = self.cam.devicemgmt.GetScopes()[-1].ScopeItem
            probe_match()
            self.cam.devicemgmt.RemoveScopes({'ScopeItem': item})
            if (item == gett and add is not None):
                return {'test_id': 5, 'name': 'AddScopes', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Added new Configurable Scope: {}'.format(item), 'response': str(add)}}
            if (item == gett and add is None):
                return {'test_id': 5, 'name': 'AddScopes', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Added new Configurable Scope: {}, but DUT did not send a valid AddScopesResponse Message.'.format(item), 'response': str(add)}}
            else:
                return {'test_id': 5, 'name': 'AddScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not add new scope, {}'.format(item), 'response': str(add)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 5, 'name': 'AddScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 5, 'name': 'AddScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def RemoveScopes(self):
        try:
            item = "onvif://www.onvif.org/remove/scope" + str(time.time())
            add = self.cam.devicemgmt.AddScopes({'ScopeItem': item})
            probe_match()
            sleep(1)
            remove = self.cam.devicemgmt.RemoveScopes({'ScopeItem': item})
            probe_match()
            gett = self.cam.devicemgmt.GetScopes()
            if (gett != []):
                gett = self.cam.devicemgmt.GetScopes()[-1].ScopeItem
            if (item != gett and remove is not None):
                return {'test_id': 6, 'name': 'RemoveScopes', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Removed added Configurable Scope: {}'.format(item), 'response': str(remove)}}
            if (item != gett and remove is None):
                return {'test_id': 6, 'name': 'RemoveScopes', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Removed added Configurable Scope: {}, but DUT did not send a valid RemoveScopesResponse Message.'.format(item), 'response': str(remove)}}    
            else:
                return {'test_id': 6, 'name': 'RemoveScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not removed new scope, {}'.format(item), 'response': str(remove)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 6, 'name': 'RemoveScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented'}}
            else:
                return {'test_id': 6, 'name': 'RemoveScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetHostname(self):
        try:
            hostname = self.cam.devicemgmt.GetHostname()
            report = 'Hostname is obtained from DHCP' if hostname.FromDHCP else 'Hostname is obtained not from DHCP\n' + 'Hostname: {}'.format(hostname.Name)
            if (hostname):
                return {'test_id': 7, 'name': 'GetHostname', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(hostname), 'report': report}}
            else:
                return {'test_id': 7, 'name': 'GetHostname', 'service': 'Device',
                'result': {'supported': False, 'extension': 'DUT did not send GetHostnameResponse message.',
                'response': str(hostname)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 7, 'name': 'GetHostname', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 7, 'name': 'GetHostname', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def SetHostname(self):
        try:
            get1 = self.cam.devicemgmt.GetHostname().Name
            name = "Onviftest1"
            set1 = self.cam.devicemgmt.SetHostname({'Name': name})
            get2 = self.cam.devicemgmt.GetHostname().Name
            self.cam.devicemgmt.SetHostname({'Name': get1})
            if (get1 != get2):
                return {'test_id': 8, 'name': 'SetHostname', 'service': 'Device',
                'result': {'supported': True, 'extension': 'The DUT returned "Onvif_test1" as its Hostname after SetHostname.', 'response': str(get2)}}
            else:
                return {'test_id': 8, 'name': 'SetHostname', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not SetHostname to "Onvif_test1"', 'response': str(set1)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 8, 'name': 'SetHostname', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 8, 'name': 'SetHostname', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetNetworkInterfaces(self):
        try:
            netifaces = self.cam.devicemgmt.GetNetworkInterfaces()
            interfaces = []
            for interface in netifaces:
                if hasattr(interface, 'IPv4'):
                    IPv4 = {'Enabled': 'IPv4 interface is enabled' if interface.IPv4.Enabled else 'IPv4 interface is not enabled',
                            'DHCP': 'DHCP is used' if interface.IPv4.Config.DHCP else 'DHCP is not used', 'FromDHCPAddress':
                            interface.IPv4.Config.FromDHCP.Address}
                if hasattr(interface, 'IPv6'):
                    IPv6 = {'Enabled': 'IPv6 interface is enabled' if interface.IPv6.Enabled else 'IPv6 interface is not enabled'}
                data = {'token': interface._token, 'Enabled': '{} interface is enabled'.format(interface.Info.Name)
                if interface.Enabled else '{} interface is not enabled'.format(interface.Info.Name), 'Name': interface.Info.Name,
                'MAC': 'MAC Address is {}'.format(interface.Info.HwAddress), 'MTU': interface.Info.MTU, 'IPv4':IPv4, 'IPv6':IPv6}
                interfaces.append(data)
            if (netifaces != []):
                return {'test_id': 9, 'name': 'GetNetworkInterfaces', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(netifaces),
                'report': str(interfaces) }}
            else:
                return {'test_id': 9, 'name': 'GetNetworkInterfaces', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetNetworkInterfacesResponse message',
                'response': str(netifaces)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 9, 'name': 'GetNetworkInterfaces', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 9, 'name': 'GetNetworkInterfaces', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetDNS(self):
        try:
            dns = self.cam.devicemgmt.GetDNS()
            if (len(dns) > 0):
                return {'test_id': 10, 'name': 'GetDNS', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(dns)}}
            else:
                return {'test_id': 10, 'name': 'GetDNS', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetDNSResponse message.',
                'response': str(dns)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 10, 'name': 'GetDNS', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 10, 'name': 'GetDNS', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetNetworkProtocols(self):
        try:
            protocols = self.cam.devicemgmt.GetNetworkProtocols()
            result = ''
            for protocol in protocols:
                name = protocol.Name
                port =  str(protocol.Port)[str(protocol.Port).find('[')+1:str(protocol.Port).find(']')]
                result += '{}:{}, '.format(name, port)
            if (protocols != []):
                return {'test_id': 11, 'name': 'GetNetworkProtocols', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(protocols),
                'report': result[:-2] }}
            else:
                return {'test_id': 11, 'name': 'GetNetworkProtocols', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetNetworkProtocolsResponse message',
                'response': str(protocols)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 11, 'name': 'GetNetworkProtocols', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 11, 'name': 'GetNetworkProtocols', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetNetworkDefaultGateway(self):
        try:
            def hasNumbers(inputString):
                return any(char.isdigit() for char in inputString)

            gateways = self.cam.devicemgmt.GetNetworkDefaultGateway()
            try:
                ipv4 = gateways.IPv4Address[0]
            except:
                ipv4 = ""
            try:
                ipv6 = gateways.IPv6Address[0]
            except:
                ipv6 = ""

            ipv4_numbers = "" if hasNumbers(ipv4) else "IPv4 gateway address is not valid"
            ipv6_letters = re.search('[a-zA-Z]', ipv6)
            ipv6_numbers = hasNumbers(ipv6)
            ipv6_check = "" if (ipv6_letters and ipv6_numbers) else "IPv6 gateway address is not valid"
            default_route = "(default route)" if ipv4 == "0.0.0.0" else ""
            report = "Device Network Default Gateway\nIPv4: {}{}".format(ipv4, default_route) + (", IPv6: {}\n" if ipv6 != "" else "\n") + ipv4_numbers + '\n' + ("" if ipv6 == "" else ipv6_check)
            if (gateways != []):
                return {'test_id': 12, 'name': 'GetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(gateways),
                'report': report }}
            else:
                return {'test_id': 12, 'name': 'GetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetNetworkDefaultGatewayResponse message',
                'response': str(gateways), 'report': 'Device did not send GetNetworkDefaultGatewayResponse message'}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 12, 'name': 'GetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented'}}
            else:
                return {'test_id': 12, 'name': 'GetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def SetNetworkDefaultGateway(self):
        try:
            default = str(self.cam.devicemgmt.GetNetworkDefaultGateway().IPv4Address[0])
            new = '10.1.0.1'
            set1 = self.cam.devicemgmt.SetNetworkDefaultGateway({'IPv4Address': new})
            get1 = str(self.cam.devicemgmt.GetNetworkDefaultGateway().IPv4Address[0])
            set2 = self.cam.devicemgmt.SetNetworkDefaultGateway({'IPv4Address': default})
            if (get1 == new):
                return {'test_id': 13, 'name': 'SetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': True, 'extension': 'The DUT set new NetworkDefaultGateway IPv4Address as {}'.format(new), 'response': str(set1)}}
            else:
                return {'test_id': 13, 'name': 'SetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not set new NetworkDefaultGateway',
                'response': str(set1)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 13, 'name': 'SetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 13, 'name': 'SetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetDeviceInformation(self):
        try:
            info = self.cam.devicemgmt.GetDeviceInformation()
            if (info != []):
                return {'test_id': 14, 'name': 'GetDeviceInformation', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(info)}}
            if ((not(hasattr(info, 'Manufacturer'))) or (not(hasattr(info, 'Model'))) or (not(hasattr(info, 'SerialNumber'))) or (not(hasattr(info, 'HardwareId'))) or (not(hasattr(info, 'FirmwareVersion')))):
                return {'test_id': 14, 'name': 'GetDeviceInformation', 'service': 'Device',
                'result': {'supported': True, 'extension': 'The DUT did not send one or more mandatory information items in the GetDeviceInformationResponse message',
                'response': str(info)}}
            else:
                return {'test_id': 14, 'name': 'GetDeviceInformation', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetDeviceInformationResponse message',
                'response': str(info)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 14, 'name': 'GetDeviceInformation', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 14, 'name': 'GetDeviceInformation', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetUsers(self):
        try:
            users = self.cam.devicemgmt.GetUsers()
            if (users != []):
                return {'test_id': 15, 'name': 'GetUsers', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(users)}}
            else:
                return {'test_id': 15, 'name': 'GetUsers', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetUsersResponse message.',
                'response': str(users)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 15, 'name': 'GetUsers', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 15, 'name': 'GetUsers', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def CreateUsers(self):
        try:
            i = 0
            f1 = False
            set1 = self.cam.devicemgmt.CreateUsers({'User':{'Username': 'lalalal', 'Password': 'lXj2N_iP9=1dD', 'UserLevel': 'User'}})
            sleep(1)
            get1 = self.cam.devicemgmt.GetUsers()
            for i in range(len(get1)):
                if get1[i].Username == 'lalalal':
                    f1 = True
            if f1:
                sleep(1)
                delete = self.cam.devicemgmt.DeleteUsers({'Username':'lalalal'})
                return {'test_id': 16, 'name': 'CreateUsers', 'service': 'Device',
                'result': {'supported': True, 'extension': 'The DUT created an user with {}'.format('Username: lalalal'), 'response': str(set1)}}
            else:
                return {'test_id': 16, 'name': 'CreateUsers', 'service': 'Device',
                'result': {'supported': True, 'extension': 'The DUT could not create a new user', 'response': str(set1)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 16, 'name': 'CreateUsers', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 16, 'name': 'CreateUsers', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetNTP(self):
        try:
            ntp = self.cam.devicemgmt.GetNTP()
            from_dhcp = "NTP configuration is retrieved by using DHCP\n" if ntp.FromDHCP == True else "NTP configuration is set manually\n"
            if ntp.FromDHCP:
                try:
                    ntp_address = dict(ntp.NTPFromDHCP[0]).items()[0]
                except:
                    ntp_address = None
            else:
                try:
                    ntp_address = dict(ntp.NTPManual[0]).items()[0]
                except:
                    ntp_address = None
            report = from_dhcp + "NTP {} is: {}".format(ntp_address[0], ntp_address[1])
            if (ntp != []):
                return {'test_id': 17, 'name': 'GetNTP', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(ntp),
                'report': report }}
            else:
                return {'test_id': 17, 'name': 'GetNTP', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetNTPResponse message.',
                'response': str(ntp), 'report': 'Device did not send GetNTPResponse message'}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 17, 'name': 'GetNTP', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 17, 'name': 'GetNTP', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetServices(self):
        try:
            services = self.cam.devicemgmt.GetServices({'IncludeCapability': False})
            cap_services = self.cam.devicemgmt.GetServices({'IncludeCapability': True})
            if (services != [] and cap_services != []):
                return {'test_id': 18, 'name': 'GetServices', 'service': 'Device',
                'result': {'supported': True, 'extension': 'The DUT send a valid response in both cases(IncludeCapability)',
                'response': str(services)}}
            else:
                return {'test_id': 18, 'name': 'GetServices', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetServicesResponse message',
                'response': str(services)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 18, 'name': 'GetServices', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 18, 'name': 'GetServices', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetSystemDateAndTime(self):
        try:
            time = self.cam.devicemgmt.GetSystemDateAndTime()
            settings = {'UTCDateTime': '{}.{}.{} {:02d}:{:02d}:{:02d}'.format(
            time.UTCDateTime.Date.Day, time.UTCDateTime.Date.Month, time.UTCDateTime.Date.Year,
            time.UTCDateTime.Time.Hour, time.UTCDateTime.Time.Minute, time.UTCDateTime.Time.Second),
            'LocalDateTime': '{}.{}.{} {:02d}:{:02d}:{:02d}'.format(
            time.LocalDateTime.Date.Day, time.LocalDateTime.Date.Month, time.LocalDateTime.Date.Year,
            time.LocalDateTime.Time.Hour, time.LocalDateTime.Time.Minute, time.LocalDateTime.Time.Second)
            }
            report = ("The time on device is set manully\n" if time.DateTimeType == 'Manual' else "The time on device is set using NTP\n") + ("Daylight savings is currently off, Time zone: {}\n".format(time.TimeZone.TZ) if time.DaylightSavings == False else "Daylight savings is currently on, Time zone: {}\n".format(time.TimeZone.TZ)) + "UTC DateTime is: {}, Local DateTime is: {}".format(settings['UTCDateTime'], settings['LocalDateTime'])

            if (time != []):
                return {'test_id': 19, 'name': 'GetSystemDateAndTime', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(time),
                'report': report}}
            else:
                return {'test_id': 19, 'name': 'GetSystemDateAndTime', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetSystemDateAndTimeResponse message',
                'response': str(time), 'report': 'Device did not send GetSystemDateAndTimeResponse message'}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 19, 'name': 'GetSystemDateAndTime', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 19, 'name': 'GetSystemDateAndTime', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetSystemUris(self):
        try:
            uri = self.cam.devicemgmt.GetSystemUris()
            try:
                log_type = uri.SystemLogUris[0][0].Type
            except:
                log_type = None
            try:
                log_uri = uri.SystemLogUris[0][0].Uri
            except:
                log_uri = None
            try:
                info_uri = uri.SupportInfoUri
            except:
                info_uri = None
            try:
                backup_uri = uri.SystemBackupUri
            except:
                backup_uri = None

            report = "{} log was requested, ".format(log_type) + ("SystemLog uri is: {}\n".format(log_uri) if log_uri is not None
            else "SystemLog uri is empty\n") + ("SupportInfo uri is: {}\n".format(info_uri) if info_uri is not None
            else "SupportInfo uri is empty\n") + ("SystemBackup uri is: {}\n".format(backup_uri) if backup_uri is not None
            else "SystemBackup uri is empty\n")

            if ((len(uri) > 0 or uri != []) and str(uri) != "<empty>"):
                return {'test_id': 20, 'name': 'GetSystemUris', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(uri),
                'report': report}}
            else:
                return {'test_id': 20, 'name': 'GetSystemUris', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetSystemUrisResponse message',
                'response': str(uri), 'report': "Device sent an empty SystemUri message"}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 20, 'name': 'GetSystemUris', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 20, 'name': 'GetSystemUris', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetEndpointReference(self):
        try:
            endpoint = self.cam.devicemgmt.GetEndpointReference()
            if (endpoint != [] or len(endpoint) == 0):
                if (endpoint.GUID is None):
                    return {'test_id': 21, 'name': 'GetEndpointReference', 'service': 'Device',
                    'result': {'supported': True, 'extension': None, 'response': str(endpoint),
                    'report': 'Endpoint Reference address is not valid or null'}}
                else:
                    return {'test_id': 21, 'name': 'GetEndpointReference', 'service': 'Device',
                    'result': {'supported': True, 'extension': None, 'response': str(endpoint),
                    'report': 'Endpoint Reference address is {}'.format(str(endpoint))}}
            else:
                return {'test_id': 21, 'name': 'GetEndpointReference', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetEndpointReferenceResponse message',
                'response': str(endpoint)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 21, 'name': 'GetEndpointReference', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented'}}
            else:
                return {'test_id': 21, 'name': 'GetEndpointReference', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetClientCertificateMode(self):
        try:
            enabled = self.cam.devicemgmt.GetClientCertificateMode()
            if not enabled:
                report = 'Client certificates are not required by device TLS client authentication'
            else:
                report = 'Client certificates are required by device TLS client authentication'
            if ((enabled is None) or (len(enabled) == 0)):
                return {'test_id': 22, 'name': 'GetClientCertificateMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT send a valid response in both cases(IncludeCapability)',
                'response': str(services)}}
            else:
                return {'test_id': 22, 'name': 'GetClientCertificateMode', 'service': 'Device',
                'result': {'supported': True, 'extension': '','response': str(services),
                'report': report }}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 22, 'name': 'GetClientCertificateMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 22, 'name': 'GetClientCertificateMode', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}