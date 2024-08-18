# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:11:05 2024

@author: Student
"""
import math
a=float(input("nhap a:"))
b=float(input("nhap b:"))
c=float(input("nhap c:"))
if a==0:
    if b==0:
        if c==0:
            print("phuong trinh co vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        if c==0:
            print("Phuong trinh co mot nghiem x=0")
        else:
            print("phuong trinh xo 1 nghiem x=", -c/b)
else:
    delta=b*b-4*a*c
    if delta>0:
        print("phuong trinh co hai nghiem phan biet:")
        print("x1=", (-(b)+ math.sqrt(delta))/(c*a))
        print("x1=", (-(b)- math.sqrt(delta))/(c*a))
    elif delta<0:
        print("phuong trinh vo nghiem")
    elif delta ==0:
        print("phuong trinh co nghiem kep: x1=x2 ", -b/(2*a))
       
        
            