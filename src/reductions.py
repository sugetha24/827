'''
Created on Oct 7, 2012

@author: sugethk
'''
import re
a = []
line = open('prod.txt','r')
reg1=re.compile(r"""([0-9]+)""",re.VERBOSE)
for i in range(121):
    j=reg1.findall(line.readline())
    a.append(j)
print('the A stack is',a)