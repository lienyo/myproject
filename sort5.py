
#------------累加----------------------------------------------------------- 
def add(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum)

#----------排序-------------------------------------------------------------- 
l = []
for i in range(5):
    x = int(input('integer:\n'))
    l.append(x)
print('\n原始輸入=',sep=' ',end=' ')
print (l)
print('排序=',sep=' ',end=' ')
l.sort()
print (l)
print('總和=',sep=' ',end=' ')
add(*l)
print('最大值=',sep=' ',end=' ')
print(max(*l))
print('最小值=',sep=' ',end=' ')
print(min(*l))
