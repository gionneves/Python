import math
import random
import time
vAnt =  13070 #13033 #13012 #12985 #12729 #12297 #11705 #11419 #10427

# ASUS limit: 12032 #11976 #11914 #11895 #11883 #11802 #11740 #11729 #11632 #11624 #11440 #11360 #11318 #10874 #10000

# Samsung limit: 8239 #8232 #8192 #8130 #8100 #8085 #8081 #8051 #8038 #8029 #7996 #7749 #7634 #7609 #7494 #7418 #7375 #7106 #7050 #6808 #6661 #6529 #6488 #6479 #6387 #6318 #6154 #5667 #4326

# Iphone limit: 6487 #6483 #6458 #6451 #6450 #6440 #6432 #6427 #6423 #6397 #6382 #6338 #6311 #6122 #6056 #5790 #5603 #5360 #5356 #5340 #5302 #4929

file = open("resul.txt", "w")

vNovo = 0

while True:
    vNovo = 0
    for x in range(10):
        vNovo += math.floor(random.random() * (300 + 800) + 300)
        pass
    file.write(str(vNovo) + "\n")
    if vNovo > vAnt:
        print(vNovo)
        break
    else:
        pass

input()
