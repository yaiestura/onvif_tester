from onvif import ONVIFCamera
from PTZTests import PTZTests

class ImagingTests:

    def __init__(self, cam):
        self.cam = cam
        self.media = self.cam.create_media_service()
        self.ptz = self.cam.create_ptz_service()
        self.imaging = self.cam.create_imaging_service()
        self.vstoken = self.media.GetVideoSources()[0]._token

    def GetImagingSettings(self):
        try:
            response = self.imaging.GetImagingSettings({'VideoSourceToken': self.vstoken})
            if ((response is None) or (len(response) == 0)):
                return {'name': 'GetImagingSettings', 'service': 'Imaging',
                'result': {'supported': False, 'extension': 'The DUT did not send GetImagingSettingsResponse message',
                'response': str(response)}}
            else:
                return {'name': 'GetImagingSettings', 'service': 'Imaging',
                'result': {'supported': True, 'extension': None,
                'response': str(response)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'GetImagingSettings', 'service': 'Imaging',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "", 'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'GetImagingSettings', 'service': 'Imaging',
                'result': {'supported': False, 'extension': str(e),
                'response': ""}}

    def AbsoluteImagingMove(self):
        try:
            token = self.media.GetProfiles()[0]._token
            req_move = self.ptz.create_type('ContinuousMove')
            req_move.ProfileToken = token
            req_stop = self.ptz.create_type('Stop')
            req_stop.ProfileToken = token

            options = self.imaging.GetMoveOptions({'VideoSourceToken': self.vstoken})
            self.imaging.create_type('Move')
            self.imaging.SetImagingSettings({'VideoSourceToken': self.vstoken, 'ImagingSettings': {'Focus': {'AutoFocusMode': 'MANUAL'}}})
            self.imaging.Stop({'VideoSourceToken': self.vstoken})
            x0 = round(self.imaging.GetStatus({'VideoSourceToken': self.vstoken}).FocusStatus20.Position, 2)
            max_x = options.Absolute.Position.Max
            if x0 + (max_x/2) < max_x:
                x1 = x0 + max_x/2
            else:
                x1 = x0 - max_x/2

            self.imaging.Move({'VideoSourceToken': self.vstoken, 'Focus': {'Absolute': {'Position': x1, 'Speed': 0.8}}})
            sleep(2)
            self.imaging.Stop({'VideoSourceToken': self.vstoken})
            x2 = round(imaging.GetStatus({'VideoSourceToken': self.vstoken}).FocusStatus20.Position, 2)
            if abs(x1-x2) == 0 and not x0 == x2 == 0:
                self.imaging.SetImagingSettings(
                    {'VideoSourceToken': self.vstoken, 'ImagingSettings': {'Focus': {'AutoFocusMode': 'AUTO'}}})
                self.cam.left(req_move, req_stop, self.ptz, token)
                self.cam.right(req_move, req_stop, self.ptz, token)
                self.cam.zoom_in(req_move, req_stop, self.ptz, token)
                self.cam.zoom_out(req_move, req_stop, self.ptz, token)
                return {'name': 'AbsoluteImagingMove', 'service': 'Imaging',
                'result': {'supported': False, 'extension': 'Absolute Imaging Move is supported',
                'response': "Absolute Imaging Move is supported", 'report': 'Absolute Imaging Move is supported'}}
            else:
                self.imaging.SetImagingSettings(
                    {'VideoSourceToken': self.vstoken, 'ImagingSettings': {'Focus': {'AutoFocusMode': 'AUTO'}}})
                self.cam.left(req_move, req_stop, self.ptz, token)
                self.cam.right(req_move, req_stop, self.ptz, token)
                self.cam.zoom_in(req_move, req_stop, self.ptz, token)
                self.cam.zoom_out(req_move, req_stop, self.ptz, token)
                return {'name': 'AbsoluteImagingMove', 'service': 'Imaging',
                'result': {'supported': False, 'extension': 'Absolute Imaging Move may be supported, but it cannot be checked.Potential error with coordinates from GetStatus()',
                'response': "Absolute Imaging Move may be supported, but it cannot be checked.Potential error with coordinates from GetStatus()", 'report': 'Absolute Imaging Move may be supported, but it cannot be checked.Potential error with coordinates from GetStatus()'}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'name': 'AbsoluteImagingMove', 'service': 'Imaging',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': "Optional Action Not Implemented",
                'report': 'Optional Action Not Implemented' }}
            else:
                return {'name': 'AbsoluteImagingMove', 'service': 'Imaging',
                'result': {'supported': False, 'extension': str(e),
                'response': "Not Supported", 'report': 'Not Supported'}}