#coding:utf-8
import http.server 
#import socketserver

port = 8080
address = ("", port)

server = http.server.HTTPServer
#handler = http.server.SimpleHTTPRequestHandler
"""
httpd = socketserver.TCPServer(address, handler)

print(f"Serveur démarré sur le Port : {port}")

httpd.serve_forever()
"""
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)

print(f"Serveur démarré sur le Port : {port}")

httpd.serve_forever()
