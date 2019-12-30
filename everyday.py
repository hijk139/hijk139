import time
import calendar
k=0
def nowtime():
    t1=time.time()
    localt1=time.localtime(t1)
    localtime=time.asctime(localt1)
    print (localtime)
while k<=1:
    k+=1
    time.sleep(2)
    nowtime()
for i in range(1,13):
    print ('2017年%s月的日历\n'%i,calendar.month(2017,i))
    time.sleep(1)
