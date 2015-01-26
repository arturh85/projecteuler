'''
Created on 04.02.2012

@author: arturh
'''

for i in range(1, 10):
    s = "src.problem00" + str(i)
    
    a = __import__(s)
    dict(a)