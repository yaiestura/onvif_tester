from flask import Flask, request, jsonify, send_from_directory, Response
import utils
from Camera import Camera

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def hello():
    return "Hello World!"


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
    return send_from_directory(app.config['SNAPSHOTS_STATIC_PATH'], filename)


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

