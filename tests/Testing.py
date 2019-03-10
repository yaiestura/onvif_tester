from . import *
from flask import jsonify


class Tests(object):
    def service_test(self, cam, test_type, method_name):

        test_types = {
            'analytics': AnalyticsTests, 'core': CoreTests, 'deviceio': DeviceIOTests,
            'events': EventsTests, 'imaging': ImagingTests, 'media': MediaTests,
            'ptz': PTZTests, 'pullpoint': PullpointTests, 'recording': RecordingTests,
            'replay': ReplayTests, 'search': SearchTests }

        if test_type in test_types:
            test = test_types[test_type](cam)
        else:
            return jsonify(response = 'Sorry, Service with name {} does not exist.'.format(test_type))

        try:
            method = getattr(test, method_name)

        except AttributeError:
            return jsonify(response = 'Sorry, method with name ' + method_name + ' does not exist.')
        
        except Exception as e:
            return jsonify(response = 'ONVIFError, ' + method_name + ' method is not supported, ' + e)
        
        return jsonify(response = method())
