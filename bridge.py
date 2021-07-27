from __future__ import print_function

from os import close
from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin

from keepkeylib import client
app = Flask(__name__)

import json
import binascii

from keepkeylib.client import KeepKeyClient, KeepKeyDebuglinkClient
from keepkeylib.transport_webusb import WebUsbTransport
from keepkeylib import messages_pb2 as messages

PACKET_SIZE = 64

kkClient = None
respData = None

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def initDevice():
    # List all connected KeepKeys on USB
    devices = WebUsbTransport.enumerate()

    # Check whether we found any
    if len(devices) == 0:
        return None

    # Use first connected device
    transport = WebUsbTransport(devices[0])

    # Creates object for manipulating KeepKey
    client = KeepKeyClient(transport)

    return client

def closeDevice(client):
    client.close()
    return


#@app.route('/', methods=['GET', 'POST'])

@app.route('/init')
def initKK():
    global kkClient
    if (kkClient == None):
        kkClient = initDevice()
    else:
        pass
    if (kkClient == None):
        data = "No KeepKey found"
    else:
        data = kkClient.features
        
    return Response(str(data), status=200, mimetype='application/json')


@app.route('/ping')
def pingKK():
    global kkClient
    if (kkClient == None):
        kkClient = initDevice()
    else:
        pass
    if (kkClient == None):
        data = "No KeepKey found"
        return Response(str(data), status=200, mimetype='application/json')

    else:
        data = kkClient.features

    ping = kkClient.call(messages.Ping(message='Duck, a bridge!', button_protection = True))
        
    return Response(str(ping), status=200, mimetype='application/json')

@app.route('/exchange/<string:kind>', methods=['GET', 'POST'])
@cross_origin()
def rest_api(kind):
    global kkClient
    global respData

    if (kkClient == None):
        kkClient = initDevice()
    else:
        pass

    if (kkClient == None):
        data = "No KeepKey found"
        return Response(str(data), status=200, mimetype='application/json')

    print("init done")
    if request.method == 'POST':
        content = request.get_json(silent=True)
        print("post content")
        print(content)
        msg = bytearray.fromhex(content["data"])
        #msg = content
        kkClient.call_bridge(msg)
        return Response('{}', status=200, mimetype='application/json')

    if request.method == 'GET':
        # print("raw resp")
        # data = str(respData)
        # #data = bytes.hex(respData)
        # #body = '{"data":"' + binascii.hexlify(data).decode("utf-8") + '"}'
        # body = json.dumps('{"data":"' + data + '"}')
        # print("get resp")
        # print(body)
        # return Response(body, status=200, mimetype='application/json')
        # data = {}
        # data['data'] = respData
        # body = json.dumps(data)
        # print("get resp")
        # print(body)
        #respData = str(respData)
        data = kkClient.call_bridge_read()
        print('body')
        body = '{"data":"' + binascii.hexlify(data).decode("utf-8") + '"}'
        print(body)
        #body = '{"data":"' + data + '"}'
        print('get it')
        print(body)
        return Response(body, status=200, mimetype='application/json')

    return Response('{}', status=404, mimetype='application/json')



# @app.after_request
# def after(response):
#     header = response.headers
#     header['Access-Control-Allow-Origin'] = '*'
#     return response


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)

