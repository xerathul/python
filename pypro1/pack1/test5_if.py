#if
var=5

if var >=3:
    print('bigger')
    print('True')
    
print('end1')

if var >=3:
    #print('bigger2')
    pass
else:
    print('less2')
print('end2')

print()
money= 300
age=23
if money >= 500:
    item='apple'
    if age <= 30:
        msg ='young'
    else:
        msg ='old'
else:
    item='orange'
    if age > 20:
        msg='man'
    else:
        msg='child'
        
print(item, msg)

print()
jum= 60
res=''

if jum>=90:
    res='a'
elif jum>= 70:
    res='b'
else:
    res='c'
print('res: '+res)

if 90 <=jum <= 100:
    res ='a'
elif 70 <= jum <90:
    res='b'
else:
    res='c'
print('res :', res)

print()
names=['tom','sul','bada']
print(names[0])
if 'sul' in names:
    print('friends')
else:
    print("who?")
    
print()
a='kbs'
b=9 if a == 'kbs' else 11
print(b)

a= 11
b='mbc' if a == 9 else 'kbs'
print(b)

print()
a=7
if a<5:
    print(0)
elif a<10:
    print(1)
else:
    print(2)
    
print(0 if a<5 else 1 if a<10 else 2)

print()
res= a *2 if a>5 else a+2
print(res)

print((a+2, a*2)[a>5])
