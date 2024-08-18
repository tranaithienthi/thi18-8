# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:37:17 2024

@author: Student
"""

GPA=float(input("nhap diem trung binh:"))

if GPA<3.5:
    print("Hoc luc kem")
elif 3.5 <= GPA<5:
    print("hoc luc trung binh")
elif 7.0 <= GPA<8.0: 
    print("Hoc luc kha")
elif 8.0 <= GPA<9.0:
    print ("Hoc luc gioi")
else:
    print("Hoc luc xuat sac")