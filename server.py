import utils
from core import Camera
from tests import CoreTests, EventsTests, AnalyticsTests, ImagingTests


from flask import (
    Flask, request, jsonify, 
    send_from_directory, Response)


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/api/core_test/<method_name>')
@utils.cam_required
def core_test(*args, **kwargs):
    cam = kwargs['ctx']['cam']
    method_name = kwargs['method_name']

    core_tests = CoreTests(cam)
    method = getattr(core_tests, method_name)
    return jsonify(response = method())
    
    # try:
    #     method = getattr(core_tests, method_name)
    #     return jsonify(response = method())
    # except AttributeError:
    #     return jsonify(error = 'Sorry, ' + method_name + ' method does not exist')
    # except Exception  as e:

    #     return jsonify(error = 'ONVIFError, ' + method_name + ' method is not supported.' + e)

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