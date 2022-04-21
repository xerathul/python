#Local DataBase 연동 후 DataFrame으로 저장

import sqlite3
sql= 'create table if not exists mytab(product varchar(10), maker varchar(10), weight real, price integer)'

conn = sqlite3.connect(':memory:')  #ram상에서 만들기
#conn= sqlite3.connext('testdb')

conn.execute(sql)
conn.commit()

data1 = ('신상1','롯데리아',45,5000)
stmt= 'insert into mytab values(?,?,?,?)'
conn.execute(stmt, data1)
data2 = ('신상2','맥도날드',55,5500)
conn.execute(stmt, data2)

cursor = conn.execute('select * from mytab')
rows= cursor.fetchall()

for a in rows:
    print(a)
    
import pandas as pd

df1= pd.DataFrame(rows, columns=['product','maker','weight','price'])
print(df1)

print('-------------')
df2 = pd.read_sql("select * from mytab", conn)
print(df2)
#print(df2.to_html())

#DataFrame을 DB로 저장
data= {
        'product':['연필','볼펜'],
        'maker':['monami','monami'],
        'weight':[1.5,2.3],
        'price':[500,1000]
    }
frame= pd.DataFrame(data)
print(frame)
print()
frame.to_sql("mytab",con= conn, if_exists='append', index=False)
df3= pd.read_sql('select * from mytab', conn)
print(df3)

print(pd.read_sql('select count(*) as count from mytab', conn))

