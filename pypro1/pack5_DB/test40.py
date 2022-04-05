# 원격 데이터 베이스 연동

import MySQLdb

#conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
#print(conn)
#conn.close

config = {

    'host':'127.0.0.1',

    'user':'root',

    'password':'123',

    'database':'test',

    'port':3306,

    'charset':'utf8',

    'use_unicode':True

}

try:
    conn= MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    """
    print('insert---')
    #isql="insert into sangdata (code, sang, su, dan) values(10,'신상',5,5000)"
    #isql="insert into sangdata (code, sang, su, dan) values(%s,%s,%s,%s)"
    isql="insert into sangdata values(%s,%s,%s,%s)"
    sql_data= (10,'신상',5,5000)
    #sql_data= 10,'신상',5,5000
    cursor.execute(isql,sql_data)
    conn.commit()
    
    print('update---')
    usql="update sangdata set sang=%s, su=%s where code=%s"
    sql_data=('얼죽아',30,10)
    cou=cursor.execute(usql,sql_data)
    print('cou: ',cou)
    conn.commit()
    
    
    print('delete---')
    inputCode='10'
    #dsql="delete sangdata where code="+inputCode # 해킹되기 쉬움
    
    dsql="delete from sangdata where code=%s"
    cou=cursor.execute(dsql,(inputCode,))
    
    #dsql="delete from sangdata where code='{0}'".format(inputCode)
    #cou=cursor.execute(dsql)
    
    conn.commit()
    if cou>0:
        print('삭제 성공')
    else:
        print('삭제 실패')
    cursor.execute(dsql)
    """
    
    print('select----')
    sql ="select code, sang, su, dan from sangdata"
    cursor.execute(sql)
    
    for data in cursor.fetchall():
        #print(data)
        print('%s %s %s %s'%data)
        
    print()
    """
    for data in cursor:
        print(data[0],data[1],data[2],data[3])
    
    print()
    """
    
except MySQLdb.connections.Error as e:
    print("error: ",e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
    