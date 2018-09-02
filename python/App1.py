
#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/temp/myapp.log',
                    filemode='w')

class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/API1':
            logging.info('starting API1')
            os.system('python ./server/CPULoadGenerator.py -l 0.2 -d 60 -c 0')
            logging.info('stoping API1')
        if self.path == '/API2':
            logging.info('starting API2')
            os.system('python ./server/CPULoadGenerator.py -l 0.4 -d 60 -c 0')
            logging.info('stoping API2')
        if self.path == '/API3':
            logging.info('starting API3')
            os.system('python ./server/CPULoadGenerator.py -l 0.85 -d 60 -c 0')
            logging.info('stoping API3')

def run():
    logging.info('http server is starting...')

    server_address = ('', 8090)
    httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
    logging.info('http server is running...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
