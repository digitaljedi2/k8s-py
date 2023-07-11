#!/usr/bin/env python3
import http.server
import socketserver
import time
import os

CONFIG_MAP_VALUE = os.environ.get('CFMAP_KEY')
PORT = 8090
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    time.sleep(30)
    print("Value of cfmap-fun-key:", CONFIG_MAP_VALUE)
    print("Serving at port", PORT)
    httpd.serve_forever()
