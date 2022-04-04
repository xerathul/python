num=1; count=0; hap=0
def func():
    while num<100:
        if num%2==0:
            print(num)
            count+=1
            hap+=num
    print(hap, count)
    
func()

print(1)