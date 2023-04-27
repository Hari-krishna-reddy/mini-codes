from random import randint

def calcu(list,length):
    l=length
    list_length=len(list)
    if l>list_length:
        while l>list_length:
            l=l-list_length
    list.remove(list[l-1])
    if len(list)==1:
        return list
    else:
        list=list[l-1:]+list[:l-1]
        return calcu(list,length)
print('THIS CODE IS WRITTEN BY\n\nHARI KRISHNA REDDY\n')
name1=input('Enter your name:')
name2=input('Enter another person name:')
num2_list=list(name2)
f_list=[]
for i in name1:
    if i !=' ':
        if i not in num2_list:
            f_list.append(i)
        if i in num2_list:
            num2_list.remove(i)
length=len(num2_list)+len(f_list)

d={'f':name1+' and '+name2+' are friends',
   'l':name1+' and '+name2+' are lovers',
   'a':'There is only attraction between '+name1+' and '+name2,
   'm':name1+' and '+name2+' are going to get married',
   'e':name1+' and '+name2+' are enemies',
   's':name1+' and '+name2+' are siblings'
   }

if length!=0:
    x=calcu([x for x in 'frames'],length)
    print()
    print(d.get(x[0]))
    
    
else:
    var=[x for x in 'flames']
    r=randint(0,5)
    print()
    print(d.get(var[r]))
            
