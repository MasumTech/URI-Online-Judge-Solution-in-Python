def check_value(a):
    if a==1:
        print('Total: R$ '+ '%.2lf' % float(int(b)*float(4.00)))
    elif a==2:
        print('Total: R$ '+ '%.2lf' % float(int(b)*float(4.50)))
    elif a==3:
        print('Total: R$ '+ '%.2lf' %  float(int(b)*float(5.00)))
    elif a==4:
        print('Total: R$ '+ '%.2lf' %  float(int(b)*float(2.00)))
    elif a==5:
        print('Total: R$ '+ '%.2lf' %  float(int(b)*float(1.50)))




r1 = input().split(" ")

a, b = r1

check_value(int(a))