import utils
from core import Camera
from tests import CoreTests, EventsTests, AnalyticsTests, ImagingTests
from flask_cors import CORS
from tests.Testing import Tests

from flask import (
    Flask, request, jsonify, 
    send_from_directory, Response)


app = Flask(__name__)
app.config.from_object('config')
CORS(app)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/api/<test_type>_test/<method_name>') 
@utils.cam_required
def run_test(*args, **kwargs):
    cam = kwargs['ctx']['cam']
    test_type = kwargs['test_type']
    method_name = kwargs['method_name']
    test = Tests()
    return test.service_test(cam, test_type, method_name)


@app.route('/api/tests') 
@utils.cam_required
def tests(*args, **kwargs):
    cam = kwargs['ctx']['cam']
    test = Tests()
    return jsonify(response = test.avaliable_tests(cam.get_supported_services()))
 

'''
Devices API
'''
@app.route('/api/devices')
def get_devices_list():
    return jsonify(utils.discovery())
    

@app.route('/api/device')
@utils.cam_required
def get_device_info(*args, **kwargs):
    cam = kwargs['ctx']['cam']
    return jsonify(cam.get_device_info())


'''
Serving data from device
'''
@app.route('/snapshots/<path:filename>')
def get_snapshot(filename):
    return send_from_directory(
        app.config['SNAPSHOTS_STATIC_PATH'], filename)


@app.route('/livestream')
@utils.cam_required
def livestream(*args, **kwargs):
    cam = kwargs['ctx']['cam']
    url = cam.get_private_stream_url()
    return Response(utils.generate_stream(url),
            mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)