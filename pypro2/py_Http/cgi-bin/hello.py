# 웹용 파이썬 모듈

a=10
b=20
c=a+b
mbc='파이썬 만세'


print('Content-Type:text/html;charset=utf-8\n')
print('<html><body>')
print('<b>Hello</b> 파이썬 모듈로 작성한 문서 입니다.<br>')
print('<hr>')
print('합은: ',c)
print('<br>메세지는 %s'%mbc)
print('<p>작성자 : 이슬</p>')
print('</body></html>')