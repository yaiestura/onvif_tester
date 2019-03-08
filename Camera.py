from onvif import ONVIFCamera
import requests 


class Camera(ONVIFCamera):
    def __init__(self, ip, port, user='admin', password='Supervisor'):
        super(Camera, self).__init__(ip, port, user, password)
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password


    # TODO: make it json fomatted
    def get_capabilities(self):
        return self.devicemgmt.GetCapabilities()


    def get_device_info(self):
        device_info = self.devicemgmt.GetDeviceInformation()
        return {
            "Manufacturer": device_info.Manufacturer,
            "Model": device_info.Model,
            "Firmware Version": device_info.FirmwareVersion,
            "Serial Number": device_info.SerialNumber,
            "Hardware ID": device_info.HardwareId,

            "snapshot_url": self.get_public_snapshot_uri(),
            "ip": self.ip,
            "port": self.port
        }


    def get_private_snapshot_url(self):
        uri = None
        media_service = self.create_media_service()
        token = media_service.GetProfiles()[0]._token

        try:
            uri = media_service.GetSnapshotUri({'ProfileToken': token}).Uri
        except Exception as e:
            pass

        return uri


    def get_private_stream_url(self):
        uri = None
        media_service = self.create_media_service()
        token = media_service.GetProfiles()[0]._token

        obj = media_service.create_type('GetStreamUri')
        obj.ProfileToken = token
        obj.StreamSetup = {
            'Stream': 'RTP-Unicast', 
            'Transport': {'Protocol': 'RTSP'}
        }

        try:
            uri = media_service.GetStreamUri(obj).Uri
        except Exception as e:
            pass

        return uri


    def get_public_snapshot_uri(self):
        private_uri = self.get_private_snapshot_url()

        if private_uri is not None:
            r = requests.get(private_uri, auth=(self.user, self.password))
            
            if r.ok:
                filename = 'snapshots/' + self.ip + ":" + str(self.port) + '.jpg'
                with open(filename, 'wb') as snapshot:
                    snapshot.write(r.content)
                return filename

        # try to get snapshot from stream
        private_stream_url = self.get_private_stream_url()

        if private_stream_url is not None:
            pass




