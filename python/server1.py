
#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import os


#Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):

    #handle GET command
    def do_GET(self):
        if self.path == '/API1':
            print('starting API1')
            os.system('python ./server/CPULoadGenerator.py -l 0.2 -d 60 -c 0')
            print('stoping API1')
        if self.path == '/API2':
            print('starting API2')
            os.system('python ./server/CPULoadGenerator.py -l 0.4 -d 60 -c 0')
            print('stoping API2')
        if self.path == '/API3':
            print('starting API3')
            os.system('python ./server/CPULoadGenerator.py -l 0.85 -d 60 -c 0')
            print('stoping API3')





def run():
    print('http server is starting...')

    server_address = ('', 8090)
    httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
