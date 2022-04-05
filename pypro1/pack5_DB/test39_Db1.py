# Database 연동 프로그래밍

# 개인용 database 
import sqlite3
print(sqlite3.sqlite_version)

print()
#conn = sqlite3.connect('exam.db')  #DB와 연결
conn = sqlite3.connect(':memory:') #실험용 - ram에 생성

try:
    cur = conn.cursor() # SQL문 실행
    
    #cur.execute("""create table if not exists friends(name text, phone text, addr text)""")
    cur.execute("create table if not exists friends(name text, phone text, addr text)")

    cur.execute("insert into friends values('홍길동', '111-1111', '서초1동')")
    cur.execute("insert into friends values(?, ?, ?)", ('신기루', '222-2222','서초2동'))
    inputData = ('신선한','333-222','서초2동')
    cur.execute("insert into friends values(?, ?, ?)", inputData)
    conn.commit()

    cur.execute("select * from friends")
    #print(cur.fetchone())
    print(cur.fetchall())

    print()
    cur.execute("select name, addr, phone from friends")
    for r in cur:
        print(r[0], r[1], r[2])


except Exception as e:
    print('error:', e)
    conn.rollback()
finally:
    cur.close()
    conn.close()
