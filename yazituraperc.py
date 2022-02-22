# @author: Berke Altıparmak
# You may use, distribute and modify this code under the
# terms of the Beerware license, which unfortunately won't be
# written for another century.
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <berkealtiparmak@outlook.com> wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.   Berke Altıparmak
# ----------------------------------------------------------------------------
#


from datetime import time

import matplotlib.pyplot as plt
import numpy
import random
import time

t0 = time.process_time()

arr = ['yazi','tura']
count = int(input("How many times you wanna flip?: "))
saved, yazi, tura = [], [], []

for x in range(count):
    tot = random.choice(arr)
    saved.append(tot)

for y in range(len(saved)):
    if saved[y] == 'yazi':
        yazi.append(saved[y])
    elif saved[y] == 'tura':
        tura.append(saved[y])
    else:
        pass

savedlen, yazilen, turalen = len(saved), len(yazi), len(tura)
percyazi = yazilen*100/savedlen
perctura = turalen*100/savedlen

#print(saved)
print(f"{savedlen} kere atıldı")
print("Yazı gelenlerin sayısı: ",yazilen)
print("Tura gelenlerin sayısı: ",turalen)
print("Yazı gelenlerın oranı: "+str(percyazi)+"%")
print("Tura gelenlerın oranı: "+str(perctura)+"%")

names = ['YAZI ', 'TURA']
values = [percyazi, perctura]
plt.figure(figsize=(4, 4))
bar = plt.bar(names, values)
plt.title(f"{savedlen} kere atıldı")
plt.ylabel("PERCENTAGE")

for bar in bar:
    yval = round(bar.get_height(), 2)
    plt.text(bar.get_x() + .25, yval - 25, yval, fontsize=15)

t1 = time.process_time()-t0
print(f"{t1} seconds passed during execution.")

plt.show()



