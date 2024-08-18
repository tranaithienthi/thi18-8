# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:46:03 2024

@author: Student
"""

a=float(input("Nhap a:"))
b=float(input("nhap b:"))

if a==0:
    if b==0:
        print("phuong trinh vo so nghiem")
    else:
        print("phuong trinh vo nghiem")
else:
    x=-b/a
    print("nghiem cua phuong trinh la: x=", x)