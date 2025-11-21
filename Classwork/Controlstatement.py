'''
for var in seq:
   #stmts

seq: list,tuple,set,dict,str,range()
'''

lang={1:'python',2:'java',3:'c',4:'c++'}

for i in lang:
    print(f'key-{i} value-{lang[i]}')

for i in enumerate(lang):
    print(f'index-{i[0]} key-{i[1]} value- {lang[i[1]]}')

