#!/bin/python3

import math
import os
import random
import re
import sys

''' comparing with existing values in dt
while emailid not none:
     for i in range(N_itr+1):
'''

'''
if __name__ == '__main__':
    N = int(input().strip())
    dt={}
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        dt[firstName]=emailID
        
        
    if emailID is not None:
            print(firstName)
'''

dt={'parnika':12,'julia':23,'apurva':34}
print(dt.items())
l=list(dt.items())
print(l)
