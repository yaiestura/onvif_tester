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
                return {'name': 'GetCapabilities', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(capabilities)}}
            else:
                return {'name': 'GetCapabilities', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetCapabilitiesResponse message',
                'response': str(capabilities), 'report': 'Not Supported'}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetCapabilities', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetCapabilities', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetDiscoveryMode(self):
        try:
            request = self.cam.devicemgmt.GetDiscoveryMode()
            if (request):
                return {'name': 'GetDiscoveryMode', 'service': 'Device',
                'result': {'supported': True, 'extension': 'This operation got the discovery mode of a device',
                'response': str(request), 'report': 'Device currently is {}'.format(str(request)) }}
            else:
                return {'name': 'GetDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetDiscoveryModeResponse message',
                'response': str(request), 'report': 'Not Supported'}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def SetDiscoveryMode(self):
        try:
            get1 = self.cam.devicemgmt.GetDiscoveryMode()
            if (get1 == 'Discoverable'):
                set1 = self.cam.devicemgmt.SetDiscoveryMode({'DiscoveryMode': 'NonDiscoverable'})
                get2 = self.cam.devicemgmt.GetDiscoveryMode()
                self.cam.devicemgmt.SetDiscoveryMode({'DiscoveryMode': get1})
                if (get1 != get2 ):
                    return {'name': 'SetDiscoveryMode', 'service': 'Device',
                    'result': {'supported': True, 'extension': 'Was Discoverable, Set NonDiscoverable, Left Discoverable',
                    'response': str(set1)}}
                else:
                    return {'name': 'SetDiscoveryMode', 'service': 'Device',
                    'result': {'supported': False, 'extension': 'DiscoveryMode was Discoverable, the DUT did not SetDiscoveryMode as NonDiscoverable',
                    'response': str(set1)}}
            elif (get1 == 'NonDiscoverable'):
                set1 = self.cam.devicemgmt.SetDiscoveryMode({'DiscoveryMode': 'Discoverable'})
                get2 = self.cam.devicemgmt.GetDiscoveryMode()
                self.cam.devicemgmt.SetDiscoveryMode({'DiscoveryMode': get1})
                if (get1 != get2):
                    return {'name': 'SetDiscoveryMode', 'service': 'Device',
                    'result': {'supported': True, 'extension': 'Was NonDiscoverable, Set Discoverable, Left NonDiscoverable',
                    'response': str(set1)}}
                else:
                    return {'name': 'SetDiscoveryMode', 'service': 'Device',
                    'result': {'supported': False, 'extension': 'DiscoveryMode was NonDiscoverable, the DUT did not SetDiscoveryMode as Discoverable',
                    'response': str(set1)}}
            else:
                return {'name': 'SetDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send SetDiscoveryModeResponse message',
                'response': str(set1)}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'SetDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'SetDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetScopes(self):
        try:
            scopes = self.cam.devicemgmt.GetScopes()
            report = ''
            for count, item in enumerate(scopes):
                report = report + item.ScopeItem + '\n'
            report = "Device has {} scope items:\n".format(count+1) + report[:-1]
            if (len(scopes) > 0):
                return {'name': 'GetScopes', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(scopes),
                'report': report}}
            else:
                return {'name': 'GetScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetScopesResponse message. The DUT scope list does not have one or more mandatory scope entry.',
                'response': str(scopes), 'report': 'The DUT did not send GetScopesResponse message\nThe DUT scope list does not have one or more mandatory scope entry.'}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetScopes', 'service': 'Device',
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
                return {'name': 'AddScopes', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Added new Configurable Scope: {}'.format(item), 'response': str(add)}}
            if (item == gett and add is None):
                return {'name': 'AddScopes', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Added new Configurable Scope: {}, but DUT did not send a valid AddScopesResponse Message.'.format(item), 'response': str(add)}}
            else:
                return {'name': 'AddScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not add new scope, {}'.format(item), 'response': str(add)}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'AddScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'AddScopes', 'service': 'Device',
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
                return {'name': 'RemoveScopes', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Removed added Configurable Scope: {}'.format(item), 'response': str(remove)}}
            if (item != gett and remove is None):
                return {'name': 'RemoveScopes', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Removed added Configurable Scope: {}, but DUT did not send a valid RemoveScopesResponse Message.'.format(item), 'response': str(remove)}}    
            else:
                return {'name': 'RemoveScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not removed new scope, {}'.format(item), 'response': str(remove)}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'RemoveScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented'}}
            else:
                return {'name': 'RemoveScopes', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetHostname(self):
        try:
            hostname = self.cam.devicemgmt.GetHostname()
            report = 'Hostname is obtained from DHCP' if hostname.FromDHCP else 'Hostname is obtained not from DHCP\n' + 'Hostname: {}'.format(hostname.Name)
            if (hostname):
                return {'name': 'GetHostname', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(hostname), 'report': report}}
            else:
                return {'name': 'GetHostname', 'service': 'Device',
                'result': {'supported': False, 'extension': 'DUT did not send GetHostnameResponse message.',
                'response': str(hostname)}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetHostname', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetHostname', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def SetHostname(self):
        try:
            get1 = self.cam.devicemgmt.GetHostname().Name
            name = "Onviftest1"
            set1 = self.cam.devicemgmt.SetHostname({'Name': name})
            get2 = self.cam.devicemgmt.GetHostname().Name
            self.cam.devicemgmt.SetHostname({'Name': get1})
            if (get1 != get2):
                return {'name': 'SetHostname', 'service': 'Device',
                'result': {'supported': True, 'extension': 'The DUT returned "Onvif_test1" as its Hostname after SetHostname.', 'response': str(get2)}}
            else:
                return {'name': 'SetHostname', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not SetHostname to "Onvif_test1"', 'response': str(set1)}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'SetHostname', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'SetHostname', 'service': 'Device',
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
                return {'name': 'GetNetworkInterfaces', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(netifaces),
                'report': str(interfaces) }}
            else:
                return {'name': 'GetNetworkInterfaces', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetNetworkInterfacesResponse message',
                'response': str(netifaces)}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetNetworkInterfaces', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetNetworkInterfaces', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetDNS(self):
        try:
            dns = self.cam.devicemgmt.GetDNS()
            from_dhcp = "DNS configuration is obtained by using DHCP\n" if dns.FromDHCP == True else "DNS configuration is set manually\n"
            domain = "The domain to search if the Hostname is not fully qualified is: {}\n".format(dns.SearchDomain) if hasattr(dns, 'SearchDomain') else ''
            items = ""
            if dns.FromDHCP:
                for item in dns.FromDHCP:
                    try:
                        ipv4 = item.IPv4Address
                        items += 'IPv4Address is: {}\n'.format(ipv4)
                    except:
                        ipv4 = ''
                        items += ipv4
                    try:
                        ipv6 = item.IPv6Address
                        items += 'IPv6Address is: {}\n'.format(ipv6)
                    except:
                        ipv6 = ''
                        items += ipv6
            else:
                for item in dns.DNSManual:
                    try:
                        ipv4 = item.IPv4Address
                        items += 'IPv4Address is: {}\n'.format(ipv4)
                    except:
                        ipv4 = ''
                        items += ipv4
                    try:
                        ipv6 = item.IPv6Address
                        items += 'IPv6Address is: {}\n'.format(ipv6)
                    except:
                        ipv6 = ''
                        items += ipv6

            report = from_dhcp + domain + "DNS configuration is: {}\n".format(items)
            if (dns != []):
                return {'name': 'GetDNS', 'service': 'Device',
                        'result': {'supported': True, 'extension': None, 'response': str(dns),
                                'report': report}}
            else:
                return {'name': 'GetDNS', 'service': 'Device',
                        'result': {'supported': False, 'extension': 'The DUT did not send GetDNSResponse message.',
                                'response': str(dns), 'report': 'Device did not send GetDNSResponse message'}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetDNS', 'service': 'Device',
                        'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                                'response': '', 'report': 'Optional Action Not Implemented'}}
            else:
                return {'name': 'GetDNS', 'service': 'Device',
                        'result': {'supported': False, 'extension': str(e), 'response': 'DNS Information is not supported',
                        'report': 'DNS Information is not supported'}}

    def GetNetworkProtocols(self):
        try:
            protocols = self.cam.devicemgmt.GetNetworkProtocols()
            result = ''
            for protocol in protocols:
                name = protocol.Name
                port =  str(protocol.Port)[str(protocol.Port).find('[')+1:str(protocol.Port).find(']')]
                result += '{}:{}, '.format(name, port)
            if (protocols != []):
                return {'name': 'GetNetworkProtocols', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(protocols),
                'report': result[:-2] }}
            else:
                return {'name': 'GetNetworkProtocols', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetNetworkProtocolsResponse message',
                'response': str(protocols)}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetNetworkProtocols', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetNetworkProtocols', 'service': 'Device',
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
                return {'name': 'GetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(gateways),
                'report': report }}
            else:
                return {'name': 'GetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetNetworkDefaultGatewayResponse message',
                'response': str(gateways), 'report': 'Device did not send GetNetworkDefaultGatewayResponse message'}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented'}}
            else:
                return {'name': 'GetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def SetNetworkDefaultGateway(self):
        try:
            default = str(self.cam.devicemgmt.GetNetworkDefaultGateway().IPv4Address[0])
            new = '10.1.0.1'
            set1 = self.cam.devicemgmt.SetNetworkDefaultGateway({'IPv4Address': new})
            get1 = str(self.cam.devicemgmt.GetNetworkDefaultGateway().IPv4Address[0])
            set2 = self.cam.devicemgmt.SetNetworkDefaultGateway({'IPv4Address': default})
            if (get1 == new):
                return {'name': 'SetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': True, 'extension': 'The DUT set new NetworkDefaultGateway IPv4Address as {}'.format(new), 'response': str(set1)}}
            else:
                return {'name': 'SetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not set new NetworkDefaultGateway',
                'response': str(set1)}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'SetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'SetNetworkDefaultGateway', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetDeviceInformation(self):
        try:
            report = 'Device Information from Manufacturer:\n'
            info = self.cam.devicemgmt.GetDeviceInformation()
            report += 'The manufacturer of the device is: {}\n'.format(info.Manufacturer)
            report += 'The device model is: {}\n'.format(info.Model)
            report += 'The firmware version in the device is: {}\n'.format(info.FirmwareVersion)
            report += 'The serial number of the device is: {}\n'.format(info.SerialNumber)
            report += 'The hardware ID of the device is: {}\n'.format(info.HardwareId)
            if (info != []):
                return {'name': 'GetDeviceInformation', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(info),
                'report': report}}
            else:
                return {'name': 'GetDeviceInformation', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetDeviceInformationResponse message',
                'response': str(info), 'report': 'The device did not send DeviceInformation message'}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetDeviceInformation', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetDeviceInformation', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': 'The device did not send DeviceInformation message',
                'report': 'The device did not send DeviceInformation message'}}

    def GetUsers(self):
        try:
            users_list = ''
            report = 'Current users on device:\n'
            users = self.cam.devicemgmt.GetUsers()
            for user in users:
                users_list += user.Username + ', '
            report += users_list[:-2]
            if (users != []):
                return {'name': 'GetUsers', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(users),
                'report': report}}
            else:
                return {'name': 'GetUsers', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetUsersResponse message.',
                'response': str(users), 'report': 'Device can not retreive users'}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetUsers', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetUsers', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': 'Device can not retreive users',
                'report': 'Device can not retreive users'}}

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
                return {'name': 'CreateUsers', 'service': 'Device',
                'result': {'supported': True, 'extension': 'The DUT created an user with {}'.format('Username: lalalal'), 'response': str(set1)}}
            else:
                return {'name': 'CreateUsers', 'service': 'Device',
                'result': {'supported': True, 'extension': 'The DUT could not create a new user', 'response': str(set1)}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'CreateUsers', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'CreateUsers', 'service': 'Device',
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
                return {'name': 'GetNTP', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(ntp),
                'report': report }}
            else:
                return {'name': 'GetNTP', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetNTPResponse message.',
                'response': str(ntp), 'report': 'Device did not send GetNTPResponse message'}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetNTP', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetNTP', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetServices(self):
        try:
            services = self.cam.devicemgmt.GetServices({'IncludeCapability': False})
            cap_services = self.cam.devicemgmt.GetServices({'IncludeCapability': True})
            if (services != [] and cap_services != []):
                return {'name': 'GetServices', 'service': 'Device',
                'result': {'supported': True, 'extension': 'The DUT send a valid response in both cases(IncludeCapability)',
                'response': str(services)}}
            else:
                return {'name': 'GetServices', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetServicesResponse message',
                'response': str(services)}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetServices', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetServices', 'service': 'Device',
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
                return {'name': 'GetSystemDateAndTime', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(time),
                'report': report}}
            else:
                return {'name': 'GetSystemDateAndTime', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetSystemDateAndTimeResponse message',
                'response': str(time), 'report': 'Device did not send GetSystemDateAndTimeResponse message'}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetSystemDateAndTime', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented', 
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetSystemDateAndTime', 'service': 'Device',
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
                return {'name': 'GetSystemUris', 'service': 'Device',
                'result': {'supported': True, 'extension': None, 'response': str(uri),
                'report': report}}
            else:
                return {'name': 'GetSystemUris', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetSystemUrisResponse message',
                'response': str(uri), 'report': "Device sent an empty SystemUri message"}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetSystemUris', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetSystemUris', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetEndpointReference(self):
        try:
            endpoint = self.cam.devicemgmt.GetEndpointReference()
            if (endpoint != [] or len(endpoint) == 0):
                if (endpoint.GUID is None):
                    return {'name': 'GetEndpointReference', 'service': 'Device',
                    'result': {'supported': True, 'extension': None, 'response': str(endpoint),
                    'report': 'Endpoint Reference address is not valid or null'}}
                else:
                    return {'name': 'GetEndpointReference', 'service': 'Device',
                    'result': {'supported': True, 'extension': None, 'response': str(endpoint),
                    'report': 'Endpoint Reference address is {}'.format(str(endpoint))}}
            else:
                return {'name': 'GetEndpointReference', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send GetEndpointReferenceResponse message',
                'response': str(endpoint)}}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetEndpointReference', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented'}}
            else:
                return {'name': 'GetEndpointReference', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetClientCertificateMode(self):
        try:
            enabled = self.cam.devicemgmt.GetClientCertificateMode()
            if not enabled:
                report = 'Client certificates are not required by device TLS client authentication'
            else:
                report = 'Client certificates are required by device TLS client authentication'
            if ((enabled is None) or (len(enabled) == 0)):
                return {'name': 'GetClientCertificateMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send a valid response in both cases(IncludeCapability)',
                'response': str(services)}}
            else:
                return {'name': 'GetClientCertificateMode', 'service': 'Device',
                'result': {'supported': True, 'extension': '','response': str(services),
                'report': report }}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetClientCertificateMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetClientCertificateMode', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': ''}}

    def GetDot11Capabilities(self):
        try:
            report = 'Wireless IEEE802.11 standart capabilities:\n'
            dot11 = self.cam.devicemgmt.GetDot11Capabilities()
            try:
                tkip = dot11.TKIP
                tkip_report = 'Temporal Key Integrity Protocol (TKIP) security protocol algorithm supported\n' if tkip == True else 'Temporal Key Integrity Protocol (TKIP) security protocol algorithm is not supported\n'
            except:
                tkip_report += ''
            try:
                scan = dot11.ScanAvailableNetworks
                scan_report = 'Device supports ScanAvailableIEEE802.11Networks operation\n' if scan == True else 'Device does not support ScanAvailableIEEE802.11Networks operation\n'
            except:
                scan_report = ''
            try:
                conf = dot11.MultipleConfiguration
                conf_report = 'Device supports multiple alternative IEEE 802.11 configurations\n' if conf == True else 'Device does not support multiple alternative IEEE 802.11 configurations\n'
            except:
                conf_report = ''
            try:
                adhoc = dot11.AdHocStationMode
                adhoc_report = 'Device supports the AdHoc station mode\n' if adhoc == True else 'Device does not support the AdHoc station mode\n'
            except:
                adhoc_report = ''
            try:
                wep = dot11.WEP
                wep_report = 'Device supports the WEP security mode' if wep == True else 'Device does not support the WEP security mode'
            except:
                wep_report = ''

            report += tkip_report
            report += scan_report
            report += conf_report
            report += adhoc_report
            report += wep_report

            if ((dot11 is None) or (dot11 == [])):
                return {'name': 'GetDot11Capabilities', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send a valid response GetDot11CapabilitiesResponseMessage',
                'response': str(dot11)}}
            else:
                return {'name': 'GetDot11Capabilities', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Wireless IEEE802.11 standart capabilities:',
                'response': str(dot11), 'report': report }}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetDot11Capabilities', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetDot11Capabilities', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': '',
                'report': 'Not Supported'}}

    def GetDot1XConfigurations(self):
        try:
            report = 'IEEE 802.1X configuration capabilities:\n'
            dot1x = self.cam.devicemgmt.GetDot1XConfigurations()
            try:
                token = dot1x.Dot1XConfigurationToken
                token_report = 'Dot1X Configuration Token is: {}\n'.format(token)
            except:
                token_report += ''
            try:
                identity = dot1x.Identity
                identity_report = 'Identity is: {}\n'.format(identity)
            except:
                identity_report = ''
            try:
                eap = dot1x.EAPMethod
                eap_report = 'EAP Method type whic is defined in IANA EAP Registry: {}'.format(eap)
            except:
                eap_report = ''

            if token_report == '' and identity_report == '' and eap_report == '':
                report = 'IEEE 802.1X configuration capabilities are not specified'

            report += token_report
            report += identity_report
            report += eap_report

            if ((dot1x is None) or (dot1x == [])):
                return {'name': 'GetDot1XConfigurations', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send a valid response GetDot1XConfigurationsResponseMessage',
                'response': str(dot11)}}
            else:
                return {'name': 'GetDot1XConfigurations', 'service': 'Device',
                'result': {'supported': True, 'extension': 'IEEE 802.1X configuration capabilities:',
                'response': str(dot11), 'report': report }}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetDot1XConfigurations', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetDot1XConfigurations', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': '',
                'report': 'Not Supported'}}

    def GetDPAddresses(self):
        try:
            report = 'Remote DP address(es) configured on device:\n'
            dp = self.cam.devicemgmt.GetDPAddresses()
            try:
                getipv4_1 = self.cam.devicemgmt.GetDPAddresses()[0].IPv4Address
                sleep(0.5)
                setipv4_1 = self.cam.devicemgmt.SetDPAddresses({'DPAddress': {'Type': 'IPv4', 'IPv4Address': '192.168.15.244'}})
                sleep(1)
                getipv4_2 = self.cam.devicemgmt.GetDPAddresses()[0].IPv4Address
                sleep(1)
                setipv4_2 = self.cam.devicemgmt.SetDPAddresses({'DPAddress': {'Type': 'IPv4', 'IPv4Address': getipv4_1}})
                sleep(0.5)
                getipv4_3 = self.cam.devicemgmt.GetDPAddresses()[0].IPv4Address
                if (getipv4_2 != getipv4_1):
                    report += 'Device default DP IPv4 address is: {}\nDevice supports changing DPAddress using SetDPAddresses\n'.format(getipv4_1)
                else:
                    report += 'Device default DP IPv4 address is: {}\nDevice does not supports changing DPAddress using SetDPAddresses\n'.format(getipv4_1)
            except:
                report += "Device does not support remote DP IPv4 addresses"
            try:
                getipv6_1 = self.cam.devicemgmt.GetDPAddresses()[0].IPv6Address
                sleep(0.5)
                setipv6_1 = self.cam.devicemgmt.SetDPAddresses({'DPAddress': {'Type': 'IPv6', 'IPv6Address': '2001:0db8:85a3:0000:0000:8a2e:0370:7334'}})
                sleep(1)
                getipv6_2 = self.cam.devicemgmt.GetDPAddresses()[0].IPv6Address
                sleep(1)
                setipv6_2 = self.cam.devicemgmt.SetDPAddresses({'DPAddress': {'Type': 'IPv6', 'IPv6Address': getipv4_1}})
                sleep(0.5)
                getipv6_3 = self.cam.devicemgmt.GetDPAddresses()[0].IPv6Address
                if (getipv6_2 != getipv6_1):
                    report += 'Device default DP IPv6 address is: {}\nDevice supports changing DPAddress using SetDPAddresses\n'.format(getipv6_1)
                else:
                    report += 'Device default DP IPv6 address is: {}\nDevice does not supports changing DPAddress using SetDPAddresses\n'.format(getipv6_1)
            except:
                report = "Device does not support remote DP IPv6 addresses"

            if ((dp is None) or (dp == [])):
                return {'name': 'GetDPAddresses', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send a valid response GetDPAddressesResponseMessage',
                'response': str(dp), 'report': 'Not Supported'}}
            else:
                return {'name': 'GetDPAddresses', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Remote DP address(es) configured on device:',
                'response': str(dp), 'report': report }}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetDPAddresses', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetDPAddresses', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': '',
                'report': 'Not Supported'}}

    def GetGeoLocation(self):
        try:
            report = 'Remote DP address(es) configured on device:\n'
            location = self.cam.devicemgmt.GetGeoLocation()
            if ((location is None) or (location == [])):
                return {'name': 'GetGeoLocation', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send a valid response GetGeoLocationResponseMessage',
                'response': str(location), 'report': 'GeoLocation configuration is not supported by device'}}
            else:
                return {'name': 'GetGeoLocation', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Remote DP address(es) configured on device:',
                'response': str(location), 'report': 'Device supports GeoLocation configuration' }}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetGeoLocation', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetGeoLocation', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': '',
                'report': 'GeoLocation configuration is not supported by device'}}

    def GetRemoteDiscoveryMode(self):
        try:
            report = ''
            remote_discovery = self.cam.devicemgmt.GetRemoteDiscoveryMode()
            if remote_discovery:
                report += 'Remote Discovery mode of a device is supported\nDevice is {} using Remote Discovery'.format(remote_discovery)

            if ((not remote_discovery) or (remote_discovery is None) or (remote_discovery == [])):
                return {'name': 'GetRemoteDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send a valid response GetRemoteDiscoveryModeResponseMessage',
                'response': str(remote_discovery), 'report': 'Remote discovery mode is not supported by the device'}}
            else:
                return {'name': 'GetRemoteDiscoveryMode', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Remote Discovery mode of a device:',
                'response': str(remote_discovery), 'report': report }}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetRemoteDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetRemoteDiscoveryMode', 'service': 'Device',
                'result': {'supported': False, 'extension': str(e), 'response': '',
                'report': 'Remote discovery mode is not supported by the device'}}

    def SendAuxiliaryCommand(self):
        try:
            send = self.cam.devicemgmt.SendAuxiliaryCommand({'AuxiliaryCommand': 'tt:Wiper|On'})
            sleep(1)
            resend =  self.cam.devicemgmt.SendAuxiliaryCommand({'AuxiliaryCommand': 'tt:Wiper|Off'})
            return {'name': 'SendAuxiliaryCommand', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Auxiliary Commands are supported by the device',
                'response': 'Auxiliary Commands are supported by the device', 'report': 'Auxiliary Commands are supported by the device' }}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'SendAuxiliaryCommand', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'SendAuxiliaryCommand', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Auxiliary Commands are not supported by the device',
                 'response': 'Auxiliary Commands are not supported by the device',
                'report': 'Auxiliary Commands are not supported by the device'}}

    def GetIPAddressFilter(self):
        def __eq__(self, other):
            try:
                ipv4_self = self.IPv4Address
                ipv4_other =  other.IPv4Address
            except:
                ipv4_self = None
                ipv4_other = None
            try:
                ipv6_self = self.IPv6Address
                ipv6_other =  other.IPv6Address
            except:
                ipv6_self = None
                ipv6_other = None
            return self.Type == other.Type and ipv4_self == ipv4_other and ipv6_self == ipv6_other
        try:
            report = 'IP address ACL filter configuration:\n'
            get1 = self.cam.devicemgmt.GetIPAddressFilter()
            try:
                ipv4 = 'IPv4 address: {}'.format(get1.IPv4Address)
            except:
                ipv4 = 'IPv4 address filter is not specified'
            try:
                ipv6 = 'IPv6 address: {}'.format(get1.IPv6Address)
            except:
                ipv6 = 'IPv6 address filter is not specified'
            if get1:
                report += 'Device supports Access Control List based on IP filtering rules (denied or allowed)\nDefault configuration:\nType: {}, {}, {}\n'.format(get1.Type, ipv4, ipv6)
            else:
                report += 'Device does not support Access Control List based on IP filtering rules (denied or allowed)\n'
            set1 = self.cam.devicemgmt.SetIPAddressFilter({'IPAddressFilter': {'Type': 'Deny','IPv4Address': {'Address': '10.0.222.33', 'PrefixLength': 24}}})
            get2 = self.cam.devicemgmt.GetIPAddressFilter()
            if get2 != get1:
                report += 'Device supports Manual Access Control List configuration. Set Deny Rule with IPv4: 10.0.222.33\\24\n'
            else:
                report += 'Device does not support Manual Access Control List configuration. Tried to set Deny Rule with IPv4: 10.0.222.33\\24\n'

            del1 = self.cam.devicemgmt.RemoveIPAddressFilter({'IPAddressFilter': {'Type': 'Deny','IPv4Address': {'Address': '10.0.222.33', 'PrefixLength': 24}}})
            get3 = self.cam.devicemgmt.GetIPAddressFilter()
            if __eq__(get1, get3):
                report += 'Device supports Deletion of Access Control List rules. Device successfully removed Deny set Rule'
            else:
                report += 'Device does no support Deletion of Access Control List rules. Device did not remove Deny set Rule'
            if ((not get1) or (get1 is None) or (get1 == [])):
                return {'name': 'GetIPAddressFilter', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send a valid response GetIPAddressFilterResponseMessage',
                'response': str(remote_user), 'report': 'Device does not support Access Control List based on IP filtering rules (denied or allowed)'}}
            else:
                return {'name': 'GetIPAddressFilter', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Device supports Access Control List:',
                'response': str(get1) + '\n' + str(get2), 'report': report }}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetIPAddressFilter', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetIPAddressFilter', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Device does not support Access Control List based on IP filtering rules (denied or allowed)',
                'response': 'Device does not support Access Control List based on IP filtering rules (denied or allowed)',
                'report': 'Device does not support Access Control List based on IP filtering rules (denied or allowed)'}}

    def GetZeroConfiguration(self):
        try:
            report = ''
            get1 = self.cam.devicemgmt.GetZeroConfiguration()
            addresses = 'The zero-configuration IPv4 address(es): {}'.format((", ".join(get1.Addresses)))
            interface = get1.InterfaceToken
            enabled = True if get1.Enabled == False else False
            report_enabled = 'Zero Configuration currently is Enabled' if get1.Enabled == True else 'Zero Configuration currently is not Enabled'
            report += 'Current device Zero Configuration is:\n'
            report += 'Network interface: {}\n{}\n{}\n'.format(interface, report_enabled, addresses)
            set1 = self.cam.devicemgmt.SetZeroConfiguration({'InterfaceToken': interface, 'Enabled': enabled})
            sleep(1)
            get2 = self.cam.devicemgmt.GetZeroConfiguration()
            if get2.Enabled != get1.Enabled:
                bool_enabled = 'Disabled' if get1.Enabled == True else 'Enabled'
                report += 'Zero Configuration could be enabled or disabled manually using SetZeroConfiguration\nZero Configuration has been {} and Reset to default'.format(bool_enabled)
            else:
                report += 'Zero Configuration could not be enabled or disabled manually using SetZeroConfiguration\n'
            sleep(1)
            set2 = self.cam.devicemgmt.SetZeroConfiguration({'InterfaceToken': interface, 'Enabled': get1.Enabled})
            if ((not get1) or (get1 is None) or (get1 == [])):
                return {'name': 'GetZeroConfiguration', 'service': 'Device',
                'result': {'supported': False, 'extension': 'The DUT did not send a valid response GetZeroConfigurationResponseMessage',
                'response': str(remote_user), 'report': 'Device does not support Zero Configuration'}}
            else:
                return {'name': 'GetZeroConfiguration', 'service': 'Device',
                'result': {'supported': True, 'extension': 'Device supports Zero Configuration:',
                'response': str(get1) + '\n' + str(get2), 'report': report }}
        except Exception as e:
            if ((str(e) == 'Optional Action Not Implemented') or (str(e) == 'This optional method is not implemented')):
                return {'name': 'GetZeroConfiguration', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': '', 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetZeroConfiguration', 'service': 'Device',
                'result': {'supported': False, 'extension': 'Device does not support Zero Configuration',
                'response': 'Device does not support Zero Configuration',
                'report': 'Device does not support Zero Configuration'}}