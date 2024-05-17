#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:09:01 2024

@author: doudouliu
"""

from numpy import random
choices = ['rock', 'paper', 'scissors']
beats = {'rock':'scissors', 'paper':'rock', 'scissors': 'paper'} #set the winners

p1 = random. choice (choices)
p2 = random.choice(choices)

print (f'Player 1: {p1}\nPlayer 2: {p2}')
if beats[p1] == p2:
    print ('Player 1 wins!')
elif beats [p2] == p1:
    print ('Player 2 wins!')
else:
    print ('Tie.')
    
