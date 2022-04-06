#웹용 파이썬 모듈
ss1='자료1'
ss2='data2'

print('Content-Type:text/html;charset=utf-8\n')

print('''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>Nice to meet you</h2>
자료출력: {} {}
<p/>
<img src='../images/daum.png' width='60%' />
<br>
<a href='../main.html'>back to main</a>
</body>
</html>
'''.format(ss1,ss2))