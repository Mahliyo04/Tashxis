# -*- coding: utf-8 -*-
"""sodiqova.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LTGqQxiZKMg5wbo3UbMWBL4V98MaX-9L
"""

def kasallik_tashxisi(belgi):
 if belgi == "Istima":
    return "Paracetamol iching"
 elif belgi == "Bosh og'rig'i":
    return "Bolnol"
 elif belgi == "Tish og'rig'i":
    return "Senepal"
 elif belgi == "Oshqozon og'rig'i":
    return "Noshpa"
 elif belgi == "Qo'l og'rig'i":
    return "Kuyupen"
 else:
    return "Shifokorga murojaat qiling"
belgi=input("Kasallik belgisini kiriting")
natija=kasallik_tashxisi(belgi)
print(natija)