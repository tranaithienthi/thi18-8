# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:56:14 2024

@author: Student
"""

a=float(input("nhap a:"))
b=float(input("nhap b:"))
c=float(input("nhap c:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("a,b,c la tam giac deu")
    elif a==b or b==c or c==a:
        print("a,b,c la tam giac can")
    elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print("a,b,c la tam giac vuong")
else: 
        print("a, b, c khong phai la mot tam giac")
        

    

