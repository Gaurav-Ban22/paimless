import http.server
from socket import socket
import socketserver


class httpServer:
    def __init__(self, port=8080):
        self.port = port
        self.server = None
        self.handler = None

    def start(self):
        self.handler = http.server.SimpleHTTPRequestHandler
        self.server = socketserver.TCPServer(("", self.port), self.handler)
        self.server.serve_forever()

    def stop(self):
        self.server.shutdown()
        self.server.socket.close()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print(self.wfile)
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p></body></html>", "utf-8"))
        self.wfile.close()


try:
    serv = httpServer(8000)
    serv.start()
except KeyboardInterrupt:
    print(" Keyboard interrupt; stopping server")
    serv.stop()
    