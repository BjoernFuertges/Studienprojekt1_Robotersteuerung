
from flask import Flask, render_template, url_for
import requests

import grpc
from protos_generated import webcontroller_pb2
from protos_generated import webcontroller_pb2_grpc

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/controls")
def controls():
        return render_template('controls.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    with grpc.insecure_channel(wc_server_ip + ":" + str(wc_server_port)) as channel:
        stub = webcontroller_pb2_grpc.AgentStub(channel)
        response = stub.MoveInformationDeliveryChangeForward(webcontroller_pb2.MoveInformationRequest(name=robot_name))
        # print(
        #     response.name + ", " + 
        #     str(response.stop) + ", " + 
        #     str(response.speed) + ", " + 
        #     response.direction + ", " + 
        #     response.turn + ", " + 
        #     str(response.radius))
    return render_template('index.html', forward_message=forward_message);

@app.route("/backward/", methods=['POST'])
def move_backward():
    #Moving forward code
    backward_message = "Moving Back..."
    with grpc.insecure_channel(wc_server_ip + ":" + str(wc_server_port)) as channel:
        stub = webcontroller_pb2_grpc.AgentStub(channel)
        response = stub.MoveInformationDeliveryChangeBackward(webcontroller_pb2.MoveInformationRequest(name=robot_name))
        #print(
        #    response.name + ", " + 
        #    str(response.stop) + ", " + 
        #    str(response.speed) + ", " + 
        #    response.direction + ", " + 
        #    response.turn + ", " + 
        #    str(response.radius))
    return render_template('index.html', forward_message=backward_message)

@app.route("/leftturn/", methods=['POST'])
def turn_left():
    #Turn left code
    left_message = "Turning Left..."
    with grpc.insecure_channel(wc_server_ip + ":" + str(wc_server_port)) as channel:
        stub = webcontroller_pb2_grpc.AgentStub(channel)
        response = stub.MoveInformationDeliveryChangeLeftChange(webcontroller_pb2.MoveInformationRequest(name=robot_name))
        #print(
        #    response.name + ", " + 
        #    str(response.stop) + ", " + 
        #    str(response.speed) + ", " + 
        #    response.direction + ", " + 
        #    response.turn + ", " + 
        #    str(response.radius))
    return render_template('index.html', forward_message=left_message)

@app.route("/rightturn/", methods=['POST'])
def turn_right():
    #Moving forward code
    right_message = "Turning Right..."
    with grpc.insecure_channel(wc_server_ip + ":" + str(wc_server_port)) as channel:
        stub = webcontroller_pb2_grpc.AgentStub(channel)
        response = stub.MoveInformationDeliveryChangeRightChange(webcontroller_pb2.MoveInformationRequest(name=robot_name))
        #print(
        #    response.name + ", " + 
        #    str(response.stop) + ", " + 
        #    str(response.speed) + ", " + 
        #    response.direction + ", " + 
        #    response.turn + ", " + 
        #    str(response.radius))
    return render_template('index.html', forward_message=right_message)

@app.route("/start/", methods=['POST'])
def start():
    #Moving forward code
    right_message = "Starting Up..."
    with grpc.insecure_channel(wc_server_ip + ":" + str(wc_server_port)) as channel:
        stub = webcontroller_pb2_grpc.AgentStub(channel)
        # TODO: Pls add Start Method for Robot
        response = stub.MoveInformationDeliveryStop(webcontroller_pb2.MoveInformationSendStop(name=robot_name, stop=False))
        #print(
        #    response.name + ", " + 
        #    str(response.stop) + ", " + 
        #    str(response.speed) + ", " + 
        #    response.direction + ", " + 
        #    response.turn + ", " + 
        #    str(response.radius))
    return render_template('index.html', forward_message=right_message)


@app.route("/stop/", methods=['POST'])
def stop():
    #Moving forward code
    right_message = "Stopping Actions..."
    with grpc.insecure_channel(wc_server_ip + ":" + str(wc_server_port)) as channel:
        stub = webcontroller_pb2_grpc.AgentStub(channel)
        response = stub.MoveInformationDeliveryStop(webcontroller_pb2.MoveInformationSendStop(name=robot_name, stop=True))
        #print(
        #    response.name + ", " + 
        #    str(response.stop) + ", " + 
        #    str(response.speed) + ", " + 
        #    response.direction + ", " + 
        #    response.turn + ", " + 
        #    str(response.radius))
    return render_template('index.html', forward_message=right_message)


@app.route("/displayStatus/", methods=['POST'])
def returnStatus() :
    print("Hi, what is the status???")
    with grpc.insecure_channel(wc_server_ip + ":" + str(wc_server_port)) as channel:
        stub = webcontroller_pb2_grpc.AgentStub(channel)
        response = stub.MoveInformationGetLastSended(webcontroller_pb2.MoveInformationRequest(name=robot_name))
        status = [str(response.speed), str(response.speed), response.direction, response.turn, response.turn, response.radius, response.stop]
    #print(status)
    return render_template('index.html', entries=status, myGreatValue='hi')

    
@app.route("/downloadImg/", methods=['POST'])
def downloadSnapshot() :
    #print("Hi, let me download this Snap")
    return render_template('index.html')

def start(name : str, wc_ip : str, wc_port : int, debug_modus : bool, gui_ip : str, gui_port : int) -> None:
    global robot_name
    global wc_server_ip
    global wc_server_port
    robot_name = name
    wc_server_ip = wc_ip
    wc_server_port = wc_port

    app.run(debug=debug_modus, host=gui_ip, port=gui_port)
  
if __name__ == "__main__":
    app.run(debug=True)

