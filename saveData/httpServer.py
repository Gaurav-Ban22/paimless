import http.server
from socket import socket
import socketserver


PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("hosting on", PORT)
    httpd.serve_forever()