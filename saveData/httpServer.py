import http.server
from socket import socket
import socketserver


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
        

try:
    serv = httpServer(8000, selfHandler)
    serv.start()
except KeyboardInterrupt:
    print(" Keyboard interrupt; stopping server")
    serv.stop()
    