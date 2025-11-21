'''
for var in seq:
   #stmts
for var in enumerate(seq):
   #stmts
for var in range(start,end+1,step):
   #stmts
   
seq: list,tuple,set,dict,str,range()
'''

num=int(input("Enter the number:"))
for i in range(1,21):
    print(f'{num}*{i}={num*i}')
