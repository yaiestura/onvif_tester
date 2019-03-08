from flask import Flask, request, jsonify
import utils
from Camera import Camera

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)

