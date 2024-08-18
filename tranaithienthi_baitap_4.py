# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:08:24 2024

@author: Student
"""

a=float(input("So km di duoc:"))
if a<1:
    print("So tien can phai tra la:", 20*a)
elif a<=3:
    print("So tien can phai tra la:", 13*a)
elif a>=4 and a<=8:
    print("So tien can phai tra la:", 3*13+a*12)
else: 
    print("So tien can phai tra la:", 3*13+5*12+a*10)

    