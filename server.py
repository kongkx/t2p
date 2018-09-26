
import http.server
import cgi
import base64
import json
import subprocess
import re
import os
import datetime
import random
from urllib.parse import urlparse, parse_qs

PORT = 9888

class CustomServerHandler(http.server.BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header(
            'WWW-Authenticate', 'Basic realm="Demo Realm"')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    
    def do_JSONHEAD(self, code):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):

        self.do_JSONHEAD(200)

        response = {
            'success': True,
            'message': 'server is running',
        }

        self.wfile.write(bytes(json.dumps(response), 'utf-8'))

        return

    def do_POST(self):
        key = self.server.get_token()

        ''' Present frontpage with user authentication. '''
        if self.headers.get('Authorization') == None:
            self.do_AUTHHEAD()

            response = {
                'success': False,
                'error': 'No auth header received'
            }

            self.wfile.write(bytes(json.dumps(response), 'utf-8'))

        elif self.headers.get('Authorization') == 'Token ' + str(key):
            # self.send_response(200)
            # self.send_header('Content-type', 'application/json')
            # self.end_headers()

            # handle updated file
            content_type = self.headers['content-type']
            if not content_type:
                self.do_JSONHEAD(422)
                response = {
                    'success': False,
                    'error': "Content-Type header doesn't contain boundary"
                }
                self.wfile.write(bytes(json.dumps(response), 'utf-8'))
                return
            else:
                boundary = content_type.split("=")[1].encode()
                remainbytes = int(self.headers['content-length'])
                line = self.rfile.readline()
                remainbytes -= len(line)
                if not boundary in line:
                    self.do_JSONHEAD(422)
                    response = {
                        'success': False,
                        'error': "Content NOT begin with boundary"
                    }
                    self.wfile.write(bytes(json.dumps(response), 'utf-8'))
                    return
                
                line = self.rfile.readline()
                remainbytes -= len(line)
                fn = re.findall(r'Content-Disposition.*name="file"; filename="(.*)"', line.decode())
                if not fn:
                    
                    self.do_JSONHEAD(422)
                    response = {
                        'success': False,
                        'error': "Can't find out file name..."
                    }
                    self.wfile.write(bytes(json.dumps(response), 'utf-8'))
                    return
                
                dirpath = self._get_temp_dir()
                basename = fn[0]
                tempname = self._get_uinque_filename(basename)
                temppath = os.path.join(dirpath, tempname)
                outputpath = os.path.join(dirpath, 'output_'+tempname)
                line = self.rfile.readline()
                remainbytes -= len(line)
                line = self.rfile.readline()
                remainbytes -= len(line)
                try:
                    out = open(temppath, 'wb')
                except IOError:
                    self.do_JSONHEAD(500)
                    responses = {
                        'success': False,
                        'error': "Can't find out file name..."
                    }
                    self.wfile.write(bytes(json.dumps(response), 'utf-8'))
                    return

                preline = self.rfile.readline()
                remainbytes -= len(preline)
                while remainbytes > 0:
                    line = self.rfile.readline()
                    remainbytes -= len(line)
                    if boundary in line:
                        preline = preline[0:-1]
                        if preline.endswith(b'\r'):
                            preline = preline[0:-1]
                        out.write(preline)
                        out.close()

                        '''call inkscape and then return svg''' 
                        returncode = subprocess.call(['inkscape', '-T', str('-f=%s' % temppath), str('-l=%s' % outputpath) ])
                        
                        try:
                            f = open(outputpath, 'r', encoding='utf-8')
                            self.send_response(200)
                            self.send_header('Content-Type', 'image/svg+xml; charset=utf-8')
                            self.send_header('Cotnent-Diposition', 'attachment; filename="[output]' + basename +'"')
                            self.end_headers()
                            self.wfile.write(f.read().encode())
                            f.close()
                            return
                        except FileNotFoundError:
                            self.do_JSONHEAD(500)
                            responses = {
                                'success': False,
                                'error': 'Failed to process uploaded file.'
                            }
                    else:
                        out.write(preline)
                        preline = line
                
                self.do_JSONHEAD(422)
                responses = {
                    'success': False,
                    'error': "Can't find out file name..."
                }
                self.wfile.write(bytes(json.dumps(response), 'utf-8'))
                return
        else:
            self.do_AUTHHEAD()

            response = {
                'success': False,
                'error': 'Invalid credentials'
            }

            self.wfile.write(bytes(json.dumps(response), 'utf-8'))

        response = {
            'path': self.path,
            'get_vars': str(getvars),
            'get_vars': str(postvars)
        }

        self.wfile.write(bytes(json.dumps(response), 'utf-8'))

    def _get_temp_dir(self):
        return self.server.get_cache_dir()

    def _get_uinque_filename(self, name):
        filename, file_extension = os.path.splitext(name)
        time = int (datetime.datetime.now().timestamp())
        return str('%d_%d%s' % (time, random.randint(0, 100), file_extension))

class CustomHTTPServer(http.server.HTTPServer):
    key = ''
    cached_dir = ''

    def __init__(self, address, handlerClass=CustomServerHandler):
        super().__init__(address, handlerClass)

    def set_token(self, token):
        self.key = token

    def get_token(self):
        return self.key

    def set_cache_dir(self, path):
        cached_dir = os.path.abspath(path)
        if not os.path.exists(cached_dir):
            os.makedirs(cached_dir)
        self.cached_dir = cached_dir

    def get_cache_dir(self):
        return self.cached_dir

def main():
    try: 
        with open('config.json') as f:
            config = json.load(f)

        server = CustomHTTPServer(('', config['port']))
        print("serving at port", config['port'])
        
        server.set_token(config['token'])
        server.set_cache_dir(config['cache_dir'])
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()

if __name__ == '__main__':
    main()