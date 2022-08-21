from http.server import SimpleHTTPRequestHandler, HTTPServer
import ssl
import os
httpd = HTTPServer(('0.0.0.0', 443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="key.pem", 
        certfile='cert.pem', server_side=True)
os.system("cls")
print("Serving HTTPS on port 443 https://127.0.0.1")
httpd.serve_forever()
