#웹용 파이썬 모듈: 요청시 정보를 달고 넘어옴
import cgi

form= cgi.FieldStorage()

name= form['name'].value
age= form['age'].value

print('Content-Type:text/html;charset=utf-8\n')
print('''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>

<body>
<h1>my.py</h1>
이름: {}<br/>
나이: {}
<br>
<a href='../main.html'>back to main</a>
</body>
</html>
'''.format(name, age))