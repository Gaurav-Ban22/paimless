import http.server
from socket import socket
import socketserver
#import modelapi
from tensorflow import keras
import numpy as np

model = keras.models.load_model(input("model path: "))

class httpServer:
    def __init__(self, port=8000, handler=None):
        self.port = port
        self.server = None
        self.handler = handler

    def start(self):
        if self.handler == None:
            self.handler = http.server.BaseHTTPRequestHandler
        else:
            self.server = http.server.HTTPServer(("", self.port), self.handler)
            self.server.serve_forever()

    def stop(self):
        self.server.shutdown()
        self.server.socket.close()



class selfHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print(self.wfile)
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p></body></html>", "utf-8"))
        self.wfile.close()

    def do_POST(self):
        body_inf = int(self.headers.get('Content-Length'))
        body = self.rfile.read(body_inf)
        print("body", body.decode("utf-8"))
        arr = np.fromstring(body.decode("utf-8"), dtype=np.float32, sep=" ")
        arr = np.expand_dims(arr, axis=0)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(np.array2string(model.predict(arr), separator=" "), "utf-8"))
        self.wfile.close()
        print(np.array2string(model.predict(arr), separator=" "))


try:
    serv = httpServer(8080, selfHandler)
    serv.start()
except KeyboardInterrupt:
    print(" Keyboard interrupt; stopping server")
    serv.stop()
    