import utils
from core import Camera
from test.CoreTests import Core_Test
from test.EventsTests import Events_Test
from test.AnalyticsTests import Analytics_Test
from test.ImagingTests import Imaging_Test

from flask import (
    Flask, request, jsonify, 
    send_from_directory, Response)


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/api/core_test/<method_name>', methods=['GET'])
def core_test(method_name):
    if request.method == 'GET':
        ip = request.args.get('ip')
        port = int(request.args.get('port'))
        try:
            cam = Core_Test(ip, port, 'admin', 'Supervisor')
        except:
            return jsonify(error = 'ONVIFError, ' + method_name + ' method is not supported')
        try:
            method = getattr(cam, method_name)
            return jsonify(response = method())
        except AttributeError:
            return jsonify(error = 'Sorry, ' + method_name + ' method does not exist')
        except:
            return jsonify(error = 'ONVIFError, ' + method_name + ' method is not supported')

@app.route('/api/events_test/<method_name>', methods=['GET'])
def events_test(method_name):
    if request.method == 'GET':
        ip = request.args.get('ip')
        port = int(request.args.get('port'))
        try:
            cam = Events_Test(ip, port, 'admin', 'Supervisor')
        except:
            return jsonify(error = 'ONVIFError, ' + method_name + ' method is not supported')
        try:
            method = getattr(cam, method_name)
            return jsonify(response = method())
        except AttributeError:
            return jsonify(error = 'Sorry, ' + method_name + ' method does not exist')
        except:
            return jsonify(error = 'ONVIFError, ' + method_name + ' method is not supported')

@app.route('/api/analytics_test/<method_name>', methods=['GET'])
def analytics_test(method_name):
    if request.method == 'GET':
        ip = request.args.get('ip')
        port = int(request.args.get('port'))
        try:
            cam = Analytics_Test(ip, port, 'admin', 'Supervisor')
        except:
            return jsonify(error = 'ONVIFError, ' + method_name + ' method is not supported')
        try:
            method = getattr(cam, method_name)
            return jsonify(response = method())
        except AttributeError:
            return jsonify(error = 'Sorry, ' + method_name + ' method does not exist')
        except:
            return jsonify(error = 'ONVIFError, ' + method_name + ' method is not supported')

@app.route('/api/imaging_test/<method_name>', methods=['GET'])
def imaging_test(method_name):
    if request.method == 'GET':
        ip = request.args.get('ip')
        port = int(request.args.get('port'))
        try:
            cam = Imaging_Test(ip, port, 'admin', 'Supervisor')
        except:
            return jsonify(error = 'ONVIFError, ' + method_name + ' method is not supported')
        try:
            method = getattr(cam, method_name)
            return jsonify(response = method())
        except AttributeError:
            return jsonify(error = 'Sorry, ' + method_name + ' method does not exist')
        except:
            return jsonify(error = 'ONVIFError, ' + method_name + ' method is not supported')

'''
Devices API
'''
@app.route('/api/devices')
def get_devices_list():
    return jsonify(utils.discovery())
    

@app.route('/api/device')
def get_device_info():
    ip = request.args.get('ip')
    port = int(request.args.get('port'))
    cam = Camera(ip, port)
    return jsonify(cam.get_device_info())


@app.route('/snapshots/<path:filename>')
def get_snapshot(filename):
    return send_from_directory(
        app.config['SNAPSHOTS_STATIC_PATH'], filename)


@app.route('/livestream')
def livestream():
    ip = request.args.get('ip')
    port = int(request.args.get('port'))
    cam = Camera(ip, port, 'admin', 'Supervisor')
    url = cam.get_private_stream_url()
    return Response(utils.generate_stream(url),
            mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)