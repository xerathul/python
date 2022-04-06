# Web Server : 클라이언트와 통신이 가능
# CGI: 웹서버와 외부 프로그램 사이에서 정보를 주고 받는 방법이나 규약, 대화형 웹페이지 작성가능
#    : DB자료 처리, form tag를 이용한 자료 전송 가능

from http.server import HTTPServer, CGIHTTPRequestHandler

PORT= 8888

class Handler(CGIHTTPRequestHandler):
    cgi_direcrories=['/cgi-bin']
    
serv = HTTPServer(('127.0.0.1',PORT), Handler)

print('웹 서비스 시작...')
serv.serve_forever()
