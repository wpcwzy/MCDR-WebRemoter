import requests
import time
import sys
import threading

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
sys.path.append("plugins/WebRemoterServer")
from WebServer import app

headers={"MCDR-WebRemoter":"wpcwzy"}
serverUp=False

#-----Configuration-----

serverPort=8080
executeInterval=5

def loop(server):
    while True:
        command=requests.get("http://localhost:"+str(serverPort)+"/get_command",headers=headers).text
        if(len(command)>1):
            server.execute(command)
            print(command)
        time.sleep(executeInterval)

def start_server():
    http_server = WSGIServer(('0.0.0.0', serverPort), app, handler_class=WebSocketHandler)
    http_server.serve_forever()

def on_info(server,info):
    if serverUp:
        d = {'output': str(info.content)}
        r = requests.post("http://localhost:"+str(serverPort)+"/upload", data=d,headers=headers)

def on_server_startup(server):
    global serverUp
    webserver=threading.Thread(target=start_server)
    webserver.setDaemon(True)
    webserver.start()
    print("Server UP!")
    serverUp=True
    loop(server)