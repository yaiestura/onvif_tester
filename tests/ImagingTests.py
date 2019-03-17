from onvif import ONVIFCamera


class ImagingTests:
    
    def __init__(self, cam):
        self.cam = cam
        self.media = self.cam.create_media_service()
        self.imaging = self.cam.create_imaging_service()
        self.vstoken = self.media.GetVideoSources()[0]._token

    def GetImagingSettings(self):
        try:
            response = self.imaging.GetImagingSettings({'VideoSourceToken': self.vstoken})
            if ((response is None) or (len(response) == 0)):
                return {'test_id': 0, 'name': 'GetImagingSettings', 'service': 'Imaging',
                'result': {'supported': False, 'extension': 'The DUT did not send GetImagingSettingsResponse message',
                'response': str(response)}}
            else:
                return {'test_id': 0, 'name': 'GetImagingSettings', 'service': 'Imaging',
                'result': {'supported': True, 'extension': None,
                'response': str(response)}}
        except Exception as e:
            if str(e) == 'Optional Action Not Implemented':
                return {'test_id': 0, 'name': 'GetImagingSettings', 'service': 'Imaging',
                'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
                'response': ""}}
            else:
                return {'test_id': 0, 'name': 'GetImagingSettings', 'service': 'Imaging',
                'result': {'supported': False, 'extension': str(e),
                'response': ""}}

#     def GetOptions(self):
#         response = self.imaging.GetOptions({'VideoSourceToken': self.vstoken})
#         if (response != []):
#             if (hasattr(response.BacklightCompensation, 'Level') and response.BacklightCompensation.Level.Min > response.BacklightCompensation.Level.Max):
#                 return 'GetOptions works, BackLightCompensation.Level: Min > Max', response
#             elif (hasattr(response, 'Brightness') and response.Brightness.Min > response.Brightness.Max):
#                 return 'GetOptions works, Brightness: Min > Max', response
#             elif (hasattr(response, 'ColorSaturation') and response.ColorSaturation.Min > response.ColorSaturation.Max):
#                 return 'GetOptions works, ColorSaturation: Min > Max', response
#             elif (hasattr(response, 'Contrast') and response.Contrast.Min > response.Contrast.Max):
#                 return 'GetOptions works, Contrast: Min > Max', response
#             elif (hasattr(response, 'Exposure')):
#                 if(hasattr(response.Exposure, 'MinExposureTime') and response.Exposure.MinExposureTime.Min > response.Exposure.MinExposureTime.Max):
#                     return 'GetOptions works, Exposure.MinExposureTime: Min > Max', response
#                 elif(hasattr(response.Exposure, 'MaxExposureTime') and response.Exposure.MaxExposureTime.Min > response.Exposure.MaxExposureTime.Max):
#                     return 'GetOptions works, Exposure.MaxExposureTime: Min > Max', response
#                 elif(hasattr(response.Exposure, 'MinGain') and response.Exposure.MinGain.Min > response.Exposure.MinGain.Max):
#                     return 'GetOptions works, Exposure.MinGain: Min > Max', response
#                 elif(hasattr(response.Exposure, 'MaxGain') and response.Exposure.MaxGain.Min > response.Exposure.MaxGain.Max):
#                     return 'GetOptions works, Exposure.MaxGain: Min > Max', response
#             else:
#                 return 'GetOptions works', response
#         else:
#             return 'GetOptions does not work', response

#     def GetServiceCapabilities(self):
#         response = self.imaging.GetServiceCapabilities()
#         if (response != []):
#             return 'GetServiceCapabilities works', response
#         else:
#             return 'GetServiceCapabilities does not work', response

#     def GetMoveOptions(self):
#         response = self.imaging.GetMoveOptions({'VideoSourceToken': self.vstoken})

#     def GetStatus(self):
#         response = self.imaging.GetStatus({'VideoSourceToken': self.vstoken})

#     def GetSnapshotUri(self):
#         token = self.media.GetProfiles()[0]._token
#         response = self.media.GetSnapshotUri({'ProfileToken': token}).Uri

# #tester = Imaging_Test('192.168.15.43', 80, 'admin', 'Supervisor')
# #tests = [func for func in dir(Imaging_Test) if callable(getattr(Imaging_Test, func)) and not func.startswith("__")]
# #print tests