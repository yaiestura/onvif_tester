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
                'response': "", 'report': 'Optional Action Not Implemented' }}
            else:
                return {'test_id': 0, 'name': 'GetImagingSettings', 'service': 'Imaging',
                'result': {'supported': False, 'extension': str(e),
                'response': ""}}

    # def ContinuousFocusMove(self):
    #     options = self.imaging.GetMoveOptions({'VideoSourceToken': self.vstoken})
    #     self.imaging.create_type('Move')
    #     try:
    #         options.Continuous
    #     except AttributeError:
    #         return {'test_id': 1, 'name': 'ContinuousFocusMove', 'service': 'Imaging',
    #         'result': {'supported': False, 'extension': 'Continuous Focus Move is not supported.\\nNot listed in MoveOptions',
    #         'response': "", 'report': 'Continuous Focus Move is not supported.\\nNot listed in MoveOptions' }}
    #     max_speed = options.Continuous.Speed.Max

    #     self.imaging.SetImagingSettings({'VideoSourceToken': self.vstoken, 'ImagingSettings': {'Focus': {'AutoFocusMode': 'MANUAL'}}})
    #     self.imaging.Stop({'VideoSourceToken': self.vstoken})
    #     x0 = self.imaging.GetStatus({'VideoSourceToken': self.vstoken}).FocusStatus20.Position
    #     if x0 + (max_speed/2) < max_speed:
    #         x1 = x0 + max_speed/2
    #     else:
    #         x1 = x0 - max_speed/2
    #     try:
    #         self.imaging.Move({'VideoSourceToken': self.vstoken, 'Focus': {'Continuous': {'Speed': x1}}})
    #         sleep(1)
    #         self.imaging.Stop({'VideoSourceToken': self.vstoken})
    #         x2 = self.imaging.GetStatus({'VideoSourceToken': vstoken}).FocusStatus20.Position
    #         # print 'x0 ', x0, ' x1 ', x1, ' x2 ', x2
    #         if abs(x1 - x2) == 0.4 and not x0 == x2 == 0:
    #             self.imaging.SetImagingSettings(
    #                 {'VideoSourceToken': self.vstoken, 'ImagingSettings': {'Focus': {'AutoFocusMode': 'AUTO'}}})
    #             return {'test_id': 1, 'name': 'ContinuousFocusMove', 'service': 'Imaging',
    #             'result': {'supported': True, 'extension': 'Continuous Focus Move is supported',
    #             'response': "", 'report': 'Continuous Focus Move is supported' }}
    #         else:
    #             self.imaging.SetImagingSettings(
    #                 {'VideoSourceToken': self.vstoken, 'ImagingSettings': {'Focus': {'AutoFocusMode': 'AUTO'}}})
    #             return {'test_id': 1, 'name': 'ContinuousFocusMove', 'service': 'Imaging',
    #             'result': {'supported': False, 'extension': 'Continuous imaging may be supported, but it cannot be checked.\\nPotential error with coordinates from GetStatus()',
    #             'response': "", 'report': 'Continuous imaging may be supported, but it cannot be checked.\\nPotential error with coordinates from GetStatus()' }}
    #     except AttributeError:  # Catching error
    #         self.imaging.SetImagingSettings(
    #             {'VideoSourceToken': self.vstoken, 'ImagingSettings': {'Focus': {'AutoFocusMode': 'AUTO'}}})
    #         return {'test_id': 1, 'name': 'ContinuousFocusMove', 'service': 'Imaging',
    #         'result': {'supported': False, 'extension': 'Continuous Focus Move is not supported, AttributeError',
    #         'response': "", 'report': 'Continuous Focus Move is not supported' }}
    #     except Exception as e:
    #         if str(e) == 'Optional Action Not Implemented':
    #             return {'test_id': 1, 'name': 'ContinuousFocusMove', 'service': 'Imaging',
    #             'result': {'supported': False, 'extension': 'Optional Action Not Implemented',
    #             'response': "", 'report': 'Optional Action Not Implemented' }}

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