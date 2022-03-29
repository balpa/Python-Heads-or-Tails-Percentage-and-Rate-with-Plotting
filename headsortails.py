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
import random
import time

t0 = time.process_time()

arr = ["heads", "tails"]
count = int(input("How many times you wanna flip?: "))
saved, heads, tails = [], [], []

for x in range(count):
    tot = random.choice(arr)
    saved.append(tot)

for y in range(len(saved)):
    if saved[y] == "heads":
        heads.append(saved[y])
    elif saved[y] == "tails":
        tails.append(saved[y])
    else:
        pass

savedlen, headslen, tailslen = len(saved), len(heads), len(tails)
percheads = headslen * 100 / savedlen
perctails = tailslen * 100 / savedlen

print(f"{savedlen} times flipped")
print("Heads count: ", headslen)
print("Tails count: ", tailslen)
print("Heads percentage: " + str(percheads) + "%")
print("Tails percentage: " + str(perctails) + "%")

names = ["HEADS ", "TAILS"]
values = [percheads, perctails]
plt.figure(figsize=(4, 4))
bar = plt.bar(names, values)
plt.title(f"{savedlen} times flipped")
plt.ylabel("PERCENTAGE")

for bar in bar:
    yval = round(bar.get_height(), 2)
    plt.text(bar.get_x() + 0.25, yval - 25, yval, fontsize=15)

t1 = time.process_time() - t0  # time elapsed during process
print(f"{t1} seconds passed during execution.")

plt.show()
