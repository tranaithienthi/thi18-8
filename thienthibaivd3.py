# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:16:38 2024

@author: Student
"""

distance=float(input("nhap do dai doan duong den truong (m):"))
if distance<300:
    print("duong den nha qua gan. Thoi!Di bo")
elif distance>1200:
    print("Duong den nha qua xa. Thoi! Di xe may")
elif distance>=300 and distance <=700:
    print("duong den truong khong xa. Thoi! Di xe dap")
else:
    print("khong xac dinh")