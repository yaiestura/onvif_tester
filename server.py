import utils
from core import Camera
from tests import CoreTests, EventsTests, AnalyticsTests, ImagingTests, Tests
from flask_cors import CORS
import json
from pprint import pprint


from flask import (
    Flask, request, jsonify, 
    send_from_directory, Response, render_template)


app = Flask(__name__,
 static_folder = 'templates/build/static',
 template_folder="templates/build")

app.config.from_object('config')
CORS(app)


@app.route('/info')
def index():
    return jsonify(api_avaliable_routes=[
        '/api/<test_type>_test/<method_name>',
        '/api/tests',
        '/api/devices',
        '/api/device',
        '/snapshots/<path:filename>',
        '/livestream'
    ])


@app.route('/api/<test_type>_test/<method_name>', methods=['POST']) 
@utils.cam_required
def run_test(*args, **kwargs):
    cam = kwargs['ctx']['cam']
    test_type = kwargs['test_type']
    method_name = kwargs['method_name']
    test = Tests(cam)
    return jsonify(test.service_test(test_type, method_name))


@app.route('/api/tests') 
@utils.cam_required
def tests(*args, **kwargs):
    cam = kwargs['ctx']['cam']
    test = Tests(cam)
    return jsonify(test.avaliable_tests())


@app.route('/api/report', methods=['GET', 'POST'])
def report():
    tested_data = json.loads(request.data)
    pprint(tested_data)
    #generate_report(tested_data)
    return jsonify(response={'url': '/path/to/report.pdf'})

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


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def spa(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)