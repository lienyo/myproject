
a=input("enter a numa:")
b=input("enter a numb:")

a=int(a)
b=int(b)

   
print('\n原始輸入=',sep=' ',end=' ')
print (a,b)

print('請輸入四則運算選項 1.a+b  2.a-b  3. a*b  4. a/b',sep=' ',end=' ')
c = input('請輸入\n')  
c= int(c)

print('\n運算結果=',sep=' ',end=' ')
if c==1:
    e=a+b
elif c==2:    
     e=a-b
elif c==3:    
    e=a*b
elif c==4:    
     e=a/b
else:   
    print('\n輸入錯誤',sep=' ',end=' ')
e=float(e)
print(e)

print('---------------------------------------------------------------')

for x in range(1, 10):
    print
    for y in range(1, 10):
        print ('%d*%d=%d' % (x, y, x*y))
