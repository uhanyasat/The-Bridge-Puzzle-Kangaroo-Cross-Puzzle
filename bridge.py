# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 21:56:46 2021

@author: Sathish
"""
#person_time=[]

def across_bridge(time1):
    person_time=time1
    fast_person=min(person_time)
    person_time.remove(fast_person)
    slow_p=0
    for i in range(3):
        slow_p+=person_time[i]
        
        
    Min_time_cross_bridge=(2*fast_person)+slow_p
    return Min_time_cross_bridge
time1=[6,3,5,4]
print(across_bridge(time1))
    
    
