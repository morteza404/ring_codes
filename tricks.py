
# 1) create slicable dictionary. normal dictionary raise value error for absent key.

"""
from collections import defaultdict
data = defaultdict(lambda : "nothing")
print(data[1])
data[2] = "salam"
print(data[2])

"""


# 2) returns the fractional and integer parts of x in a two-item tuple.

"""

import math
num = math.modf(100.03625)
print(num[0])
print(num[1])

"""

# 3) To create an array of numeric values, we need to import the array module. 

"""

import array as arr
num = arr.array("H",[10,20,30,40,50])
print(num[0])
print(num[-1])
print(num[2:4])

"""

# 4) First method to create a 1D array 

"""

N = 5
arr = [0]*N 
print(arr)

"""

# 5) Second method to create a 1D array 

"""

N = 5
arr = [0 for i in range(N)]
print(arr)

"""

# 6) First method to create a 2D array 

"""

rows, cols = (5,5)
arr = [[0] * rows] * cols 
print(arr)

"""

# 7) Second method to create a 2D array 

"""

rows, cols = (5,5)
arr = [[0 for j in range(cols)] for i in range(rows)]
print(arr)

"""

# 8) r2p2d and devs

"""

replica, partition = (3,10)
r2p2d = [[1 for j in range(partition)] for i in range(replica)]
print("r2p2d")
print(r2p2d)
r2p2d[0][8] = 0
r2p2d[1][8] = 4
r2p2d[2][8] = 1

r2p2d[0][3] = 2
r2p2d[1][3] = 1
r2p2d[2][3] = 3

r2p2d[0][0] = 3
r2p2d[1][0] = 2
r2p2d[2][0] = 0

r2p2d[0][5] = 4
r2p2d[1][5] = 1
r2p2d[2][5] = 2

print("r2p2d")
print(r2p2d)
N = 5
devs = [i for i in range(N)]
print("devs")
print(devs)
devices = [devs[part2dev_id[5]] for part2dev_id in r2p2d]
print("devices")
print(devices)
"""


# 9) Display the quotient and the remainder, a//b, a%b:

"""
x = divmod(5,2)
print(x)
print(5//2,5%2)

"""

# 10) a >> b : shift a, b bit right i.e. a // (2 ** b)

"""
print(128 >> 6)

"""

# 11) a << b : shift a, b bit left i.e. a * (2 ** b)

"""
print(32 << 1)

"""

# 12) different between self and cls. PEP8

# Always use self for the first argument to instance methods.

# Always use cls for the first argument to class methods.

"""

class Test():

    def test_self(self):
        pass

    @classmethod
    def test_cls(cls):
        pass

"""

# 13) device skew

"""
wants, has = (400.0,396.0)
skew = (wants - has) / wants * 100 
print(skew)
"""

# 14) Convert Scientific Notation to Float

"""

x = 1e-10
print("%.10f" % x)
print(0.000000001 < 1e-10)

"""

# 15) shuffle list

"""

import random
x = [1,2,3,4,5]
random.shuffle(x)
print(x)

"""

# 16) create cycle

"""

import itertools

name = "morteza"

data = itertools.cycle(name)

# for i in data:
#     print(i)

"""

# 17) compute execution time of command 

"""

import timeit

print(timeit.timeit("a = 2 + 3"))

"""

# 18) get partition and replica from r2p2d

"""

b = [[2, 2, 1, 0, 3, 1, 1, 3, 0, 1, 3, 3, 3, 2, 3, 2, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 2, 0, 1, 3, 0, 3, 0, 3, 3, 3, 3, 2, 0, 1, 0, 1, 
2, 1, 1, 3, 0, 1, 2, 3, 3, 2, 3, 3, 0, 0, 1, 3, 1, 0, 0, 1, 2, 0, 2, 3, 1, 1, 1, 3, 2, 2, 1, 0, 1, 2, 2, 1, 0, 0, 1, 2, 0, 1, 2, 1, 1, 1, 0, 
1, 2, 1, 3, 3, 3, 0, 0, 0, 1, 1, 3, 1, 2, 3, 3, 3, 1, 2, 1, 0, 3, 1, 2, 3, 1, 3, 2, 0, 1, 0, 3, 3, 0, 1, 0, 1, 2, 0, 2, 2, 1, 3, 2, 3, 3, 1, 
3, 0, 3, 0, 2, 3, 1, 2, 1, 3, 1, 0, 2, 3, 3, 1, 2, 0, 3, 1, 3, 0, 3, 3, 0, 0, 0, 0, 2, 1, 3, 3, 2, 3, 2, 0, 2, 0, 0, 2, 1, 0, 1, 0, 0, 1, 0, 
2, 0, 3, 1, 3, 0, 0, 3, 2, 1, 2, 0, 2, 2, 2, 3, 3, 3, 1, 1, 2, 1, 2, 3, 2, 3, 0, 0, 2, 2, 2, 1, 3, 1, 2, 3, 1, 0, 3, 3, 3, 1, 3, 2, 2, 1, 3, 
0, 0, 2, 2, 2, 1, 1, 3, 2, 0, 3, 2, 1, 2, 0, 0, 2, 3, 3, 0, 3, 3, 3, 3, 0, 3, 1, 2, 3, 0, 1, 0, 0, 0, 0, 2, 2, 0, 3, 0, 1, 1, 2, 1, 3, 3, 0, 
2, 0, 3, 2, 0, 0, 2, 3, 3, 0, 0, 3, 0, 3, 2, 2, 1, 1, 3, 3, 1, 2, 1, 2, 3, 1, 0, 0, 0, 3, 3, 2, 0, 1, 2, 0, 0, 2, 0, 1, 0, 1, 2, 0, 3, 1, 0, 
3, 0, 0, 3, 3, 2, 1, 3, 0, 1, 1, 1, 0, 2, 0, 0, 0, 2, 2, 0, 0, 1, 3, 0, 2, 1, 0, 2, 1, 1, 2, 3, 1, 3, 1, 0, 2, 1, 1, 0, 0, 2, 1, 0, 0, 3, 3, 
0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 0, 1, 3, 3, 3, 0, 3, 3, 2, 2, 0, 2, 0, 2, 2, 1, 0, 2, 0, 0, 2, 1, 1, 3, 1, 2, 3, 0, 3, 0, 2, 2, 3, 1, 
3, 3, 0, 0, 2, 3, 2, 2, 3, 0, 0, 1, 2, 1, 0, 2, 3, 2, 3, 3, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 3, 0, 2, 2, 2, 1, 3, 3, 0, 0, 0, 3, 1, 2, 1, 
2, 1, 3, 2, 0, 1, 1, 2, 2, 0, 1, 2, 0, 3, 0, 1, 2, 2, 0, 0, 0, 1, 0, 3, 0, 3, 2, 0, 0, 3, 3, 0, 2, 1, 1, 0, 2, 0, 1, 3, 0, 3, 1, 3, 3, 2, 2, 
1, 2, 1, 0, 3, 3, 0, 1, 3, 0, 2, 1, 1, 1, 3, 2, 3, 2, 3, 2, 2, 1, 3, 1, 1, 3, 3, 2, 1, 3, 3, 2, 0, 1, 0, 0, 0, 2, 2, 1, 0, 3, 2, 1, 3, 3, 2, 
0, 1, 3, 1, 3, 0, 2, 2, 3, 2, 0, 2, 0, 2, 1, 2, 3, 0, 3, 1, 1, 3, 2, 3, 3, 1, 1, 1, 0, 3, 1, 1, 0, 1, 0, 0, 0, 2, 0, 1, 3, 1, 0, 1, 0, 3, 3, 
3, 2, 0, 1, 2, 0, 1, 2, 2, 0, 2, 1, 2, 2, 2, 1, 1, 1, 3, 1, 1, 2, 0, 3, 1, 2, 2, 0, 1, 1, 3, 3, 0, 2, 3, 1, 3, 0, 1, 0, 0, 1, 3, 1, 2, 0, 2, 
3, 1, 1, 3, 0, 3, 2, 3, 2, 3, 0, 2, 2, 2, 1, 3, 2, 3, 2, 0, 1, 2, 0, 3, 2, 1, 1, 0, 0, 3, 2, 0, 2, 3, 0, 0, 1, 2, 1, 0, 1, 2, 2, 1, 2, 3, 0, 
3, 1, 1, 3, 3, 2, 2, 3, 3, 1, 0, 0, 1, 1, 3, 0, 2, 0, 2, 3, 2, 1, 1, 0, 0, 3, 3, 0, 1, 3, 0, 1, 3, 1, 2, 2, 2, 1, 0, 2, 3, 1, 3, 0, 3, 3, 0, 
3, 3, 3, 1, 3, 1, 3, 3, 1, 2, 2, 3, 0, 1, 0, 2, 1, 3, 0, 3, 0, 2, 1, 2, 3, 2, 2, 3, 0, 0, 1, 3, 3, 2, 0, 2, 0, 1, 3, 0, 2, 0, 2, 2, 1, 3, 1, 
0, 3, 0, 2, 0, 2, 2, 1, 1, 2, 0, 1, 0, 3, 0, 1, 2, 2, 1, 2, 3, 0, 1, 1, 2, 0, 1, 1, 1, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 2, 0, 1, 3, 0, 3, 0, 1, 
0, 2, 1, 3, 3, 1, 1, 3, 3, 2, 0, 0, 3, 3, 1, 1, 2, 1, 3, 3, 3, 2, 1, 0, 2, 0, 3, 2, 1, 3, 2, 2, 3, 0, 1, 2, 3, 3, 3, 3, 2, 1, 3, 3, 2, 3, 2, 
1, 1, 1, 3, 3, 3, 3, 0, 3, 3, 1, 2, 3, 0, 2, 0, 3, 3, 1, 1, 0, 3, 1, 2, 0, 1, 1, 0, 1, 2, 3, 2, 1, 2, 0, 3, 2, 1, 1, 1, 2, 0, 3, 1, 0, 0, 1, 
2, 3, 0, 2, 1, 1, 0, 3, 2, 3, 2, 1, 3, 1, 2, 2, 2, 3, 0, 1, 1, 1, 1, 2, 0, 1, 0, 2, 3, 0, 1, 0, 3, 2, 2, 2, 2, 0, 2, 2, 1, 1, 3, 0, 1, 2, 3, 
2, 2, 1, 0, 0, 2, 1, 2, 3, 1, 0, 2, 3, 2, 3, 1, 0, 1, 3, 3, 1, 3, 2, 3, 3, 2, 0, 1, 0, 0, 2, 1, 2, 0, 2, 0, 2, 0, 3],
[3, 3, 2, 1, 0, 2, 2, 0, 1, 2, 0, 0, 0, 3, 0, 3, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 3, 1, 2, 0, 1, 0, 1, 0, 0, 0, 0, 3, 1, 2, 1, 2, 3, 2, 
2, 0, 1, 2, 3, 0, 0, 3, 0, 0, 1, 1, 2, 0, 2, 1, 1, 2, 3, 1, 3, 0, 2, 2, 2, 0, 3, 3, 2, 1, 2, 3, 3, 2, 1, 1, 2, 3, 1, 2, 3, 2, 2, 2, 1, 2, 3, 
2, 0, 0, 0, 1, 1, 1, 2, 2, 0, 2, 3, 0, 0, 0, 2, 3, 2, 1, 0, 2, 3, 0, 2, 0, 3, 1, 2, 1, 0, 0, 1, 2, 1, 2, 3, 1, 3, 3, 2, 0, 3, 0, 0, 2, 0, 1, 0, 
1, 3, 0, 2, 3, 2, 0, 2, 1, 3, 0, 0, 2, 3, 1, 0, 2, 0, 1, 0, 0, 1, 1, 1, 1, 3, 2, 0, 0, 3, 0, 3, 1, 3, 1, 1, 3, 2, 1, 2, 1, 1, 2, 1, 3, 1, 0, 2, 
0, 1, 1, 0, 3, 2, 3, 1, 3, 3, 3, 0, 0, 0, 2, 2, 3, 2, 3, 0, 3, 0, 1, 1, 3, 3, 3, 2, 0, 2, 3, 0, 2, 1, 0, 0, 0, 2, 0, 3, 3, 2, 0, 1, 1, 3, 3, 3, 
2, 2, 0, 3, 1, 0, 3, 2, 3, 1, 1, 3, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 3, 0, 1, 2, 1, 1, 1, 1, 3, 3, 1, 0, 1, 2, 2, 3, 2, 0, 0, 1, 3, 1, 0, 3, 1, 1, 
3, 0, 0, 1, 1, 0, 1, 0, 3, 3, 2, 2, 0, 0, 2, 3, 2, 3, 0, 2, 1, 1, 1, 0, 0, 3, 1, 2, 3, 1, 1, 3, 1, 2, 1, 2, 3, 1, 0, 2, 1, 0, 1, 1, 0, 0, 3, 2, 
0, 1, 2, 2, 2, 1, 3, 1, 1, 1, 3, 3, 1, 1, 2, 0, 1, 3, 2, 1, 3, 2, 2, 3, 0, 2, 0, 2, 1, 3, 2, 2, 1, 1, 3, 2, 1, 1, 0, 0, 1, 1, 1, 3, 2, 3, 3, 2, 
2, 2, 3, 3, 3, 1, 2, 0, 0, 0, 1, 0, 0, 3, 3, 1, 3, 1, 3, 3, 2, 1, 3, 1, 1, 3, 2, 2, 0, 2, 3, 0, 1, 0, 1, 3, 3, 0, 2, 0, 0, 1, 1, 3, 0, 3, 3, 0, 
1, 1, 2, 3, 2, 1, 3, 0, 3, 0, 0, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 3, 0, 1, 3, 3, 3, 2, 0, 0, 1, 1, 1, 0, 2, 3, 2, 3, 2, 0, 3, 1, 2, 2, 3, 3, 1, 
2, 3, 1, 0, 1, 2, 3, 3, 1, 1, 1, 2, 1, 0, 1, 0, 3, 1, 1, 0, 0, 1, 3, 2, 2, 1, 3, 1, 2, 0, 1, 0, 2, 0, 0, 3, 3, 2, 3, 2, 1, 0, 0, 1, 2, 0, 1, 3, 
2, 2, 2, 0, 3, 0, 3, 0, 3, 3, 2, 0, 2, 2, 0, 0, 3, 2, 0, 0, 3, 1, 2, 1, 1, 1, 3, 3, 2, 1, 0, 3, 2, 0, 0, 3, 1, 2, 0, 2, 0, 1, 3, 3, 0, 3, 1, 3, 
1, 3, 2, 3, 0, 1, 0, 2, 2, 0, 3, 0, 0, 2, 2, 2, 1, 0, 2, 2, 1, 2, 1, 1, 1, 3, 1, 2, 0, 2, 1, 2, 1, 0, 0, 0, 3, 1, 2, 3, 1, 2, 3, 3, 1, 3, 2, 3, 
3, 3, 2, 2, 2, 0, 2, 2, 3, 1, 0, 2, 3, 3, 1, 2, 2, 0, 0, 1, 3, 0, 2, 0, 1, 2, 1, 1, 2, 0, 2, 3, 1, 3, 0, 2, 2, 0, 1, 0, 3, 0, 3, 0, 1, 3, 3, 3, 
2, 0, 3, 0, 3, 1, 2, 3, 1, 0, 3, 2, 2, 1, 1, 0, 3, 1, 3, 0, 1, 1, 2, 3, 2, 1, 2, 3, 3, 2, 3, 0, 1, 0, 2, 2, 0, 0, 3, 3, 0, 0, 2, 1, 1, 2, 2, 0, 
1, 3, 1, 3, 0, 3, 2, 2, 1, 1, 0, 0, 1, 2, 0, 1, 2, 0, 2, 3, 3, 3, 2, 1, 3, 0, 2, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 2, 0, 0, 2, 3, 3, 0, 1, 2, 1, 3, 
2, 0, 1, 0, 1, 3, 2, 3, 0, 3, 3, 0, 1, 1, 2, 0, 0, 3, 1, 3, 1, 2, 0, 1, 3, 1, 3, 3, 2, 0, 2, 1, 0, 1, 3, 1, 3, 3, 2, 2, 3, 1, 2, 1, 0, 1, 2, 3, 
3, 2, 3, 0, 1, 2, 2, 3, 1, 2, 2, 2, 1, 2, 1, 1, 1, 3, 1, 1, 2, 1, 3, 1, 2, 0, 1, 0, 1, 2, 1, 3, 2, 0, 0, 2, 2, 0, 0, 3, 1, 1, 0, 0, 2, 2, 3, 2, 
0, 0, 0, 3, 2, 1, 3, 1, 0, 3, 2, 0, 3, 3, 0, 1, 2, 3, 0, 0, 0, 0, 3, 2, 0, 0, 3, 0, 3, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 2, 3, 0, 1, 3, 1, 0, 0, 2, 
2, 1, 0, 2, 3, 1, 2, 2, 1, 2, 3, 0, 3, 2, 3, 1, 0, 3, 2, 2, 2, 3, 1, 0, 2, 1, 1, 2, 3, 0, 1, 3, 2, 2, 1, 0, 3, 0, 3, 2, 0, 2, 3, 3, 3, 0, 1, 2, 
2, 2, 2, 3, 1, 2, 1, 3, 0, 1, 2, 1, 0, 3, 3, 3, 3, 1, 3, 3, 2, 2, 0, 1, 2, 3, 0, 3, 3, 2, 1, 1, 3, 2, 3, 0, 2, 1, 3, 0, 3, 0, 2, 1, 2, 0, 0, 2, 
0, 3, 0, 0, 3, 1, 2, 1, 1, 3, 2, 3, 1, 3, 1, 3, 1, 0],
[0, 0, 3, 2, 1, 3, 3, 1, 2, 3, 1, 1, 1, 0, 1, 0, 2, 2, 3, 2, 3, 3, 2, 2, 2, 3, 3, 3, 2, 0, 2, 3, 1, 2, 1, 2, 1, 1, 1, 1, 0, 2, 3, 2, 3, 0, 3, 3, 
1, 2, 3, 0, 1, 1, 0, 1, 1, 2, 2, 3, 1, 3, 2, 2, 3, 0, 2, 0, 1, 3, 3, 3, 1, 0, 0, 3, 2, 3, 0, 0, 3, 2, 2, 3, 0, 2, 3, 0, 3, 3, 3, 2, 3, 0, 3, 1, 1, 
1, 2, 2, 2, 3, 3, 1, 3, 0, 1, 1, 1, 3, 0, 3, 2, 1, 3, 0, 1, 3, 1, 0, 2, 3, 2, 1, 1, 2, 3, 2, 3, 0, 2, 0, 0, 3, 1, 0, 1, 1, 3, 1, 2, 1, 2, 0, 1, 3, 
0, 3, 1, 3, 2, 0, 1, 1, 3, 0, 2, 1, 3, 1, 2, 1, 1, 2, 2, 2, 2, 0, 3, 1, 1, 0, 1, 0, 2, 0, 2, 2, 0, 3, 2, 3, 2, 2, 3, 2, 0, 2, 1, 3, 1, 2, 2, 1, 0, 
3, 0, 2, 0, 0, 0, 1, 1, 1, 3, 3, 0, 3, 0, 1, 0, 1, 2, 2, 0, 0, 0, 3, 1, 3, 0, 1, 3, 2, 1, 1, 1, 3, 1, 0, 0, 3, 1, 2, 2, 0, 0, 0, 3, 3, 1, 0, 2, 1, 
0, 3, 0, 2, 2, 0, 1, 1, 2, 1, 1, 1, 1, 2, 1, 3, 0, 1, 2, 3, 2, 2, 2, 2, 0, 0, 2, 1, 2, 3, 3, 0, 3, 1, 1, 2, 0, 2, 1, 0, 2, 2, 0, 1, 1, 2, 2, 1, 2, 
1, 0, 0, 3, 3, 1, 1, 3, 0, 3, 0, 1, 3, 2, 2, 2, 1, 1, 0, 2, 3, 0, 2, 2, 0, 2, 3, 2, 3, 0, 2, 1, 3, 2, 1, 2, 2, 1, 1, 0, 3, 1, 2, 3, 3, 3, 2, 0, 2, 
2, 2, 0, 0, 2, 2, 3, 1, 2, 0, 3, 2, 0, 3, 3, 0, 1, 3, 1, 3, 2, 0, 3, 3, 2, 2, 0, 3, 2, 2, 1, 1, 2, 2, 2, 0, 3, 0, 0, 3, 3, 3, 0, 0, 0, 2, 3, 1, 1, 
1, 2, 1, 1, 0, 0, 2, 0, 2, 0, 0, 3, 2, 0, 2, 2, 0, 3, 3, 1, 3, 0, 1, 2, 1, 2, 0, 0, 1, 3, 1, 1, 2, 2, 0, 1, 0, 0, 1, 2, 2, 3, 0, 3, 2, 0, 1, 0, 1, 
1, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 1, 2, 0, 0, 0, 3, 1, 1, 2, 2, 2, 1, 3, 0, 3, 0, 3, 1, 0, 2, 3, 3, 0, 0, 2, 3, 0, 2, 1, 2, 3, 0, 0, 2, 2, 2, 
3, 2, 1, 2, 1, 0, 2, 2, 1, 1, 2, 0, 3, 3, 2, 0, 2, 3, 1, 2, 1, 3, 1, 1, 0, 0, 3, 0, 3, 2, 1, 1, 2, 3, 1, 2, 0, 3, 3, 3, 1, 0, 1, 0, 1, 0, 0, 3, 1, 
3, 3, 1, 1, 0, 3, 1, 1, 0, 2, 3, 2, 2, 2, 0, 0, 3, 2, 1, 0, 3, 1, 1, 0, 2, 3, 1, 3, 1, 2, 0, 0, 1, 0, 2, 0, 2, 0, 3, 0, 1, 2, 1, 3, 3, 1, 0, 1, 1, 
3, 3, 3, 2, 1, 3, 3, 2, 3, 2, 2, 2, 0, 2, 3, 1, 3, 2, 3, 2, 1, 1, 1, 0, 2, 3, 0, 2, 3, 0, 0, 2, 0, 3, 0, 0, 0, 3, 3, 3, 1, 3, 3, 0, 2, 1, 3, 0, 0, 
2, 3, 3, 1, 1, 2, 0, 1, 3, 1, 2, 3, 2, 2, 3, 1, 3, 0, 2, 0, 1, 3, 3, 1, 2, 1, 0, 1, 0, 1, 2, 0, 0, 0, 3, 1, 0, 1, 0, 2, 3, 0, 2, 1, 0, 3, 3, 2, 2, 
1, 0, 2, 0, 1, 2, 2, 3, 0, 3, 2, 3, 0, 0, 3, 0, 1, 2, 1, 3, 3, 1, 1, 0, 0, 1, 1, 3, 2, 2, 3, 3, 1, 2, 0, 2, 0, 1, 0, 3, 3, 2, 2, 1, 1, 2, 3, 1, 2, 
3, 1, 3, 0, 0, 0, 3, 2, 0, 1, 3, 1, 2, 1, 1, 2, 1, 1, 1, 3, 1, 3, 1, 1, 3, 0, 0, 1, 2, 3, 2, 0, 3, 1, 2, 1, 2, 0, 3, 0, 1, 0, 0, 1, 2, 2, 3, 1, 1, 
0, 2, 0, 2, 3, 1, 2, 0, 2, 0, 0, 3, 1, 3, 2, 1, 2, 0, 2, 0, 0, 3, 3, 0, 2, 3, 2, 1, 2, 3, 0, 0, 3, 0, 1, 2, 3, 3, 0, 2, 3, 3, 3, 2, 3, 2, 2, 2, 0, 
2, 2, 3, 2, 0, 2, 3, 1, 2, 1, 2, 3, 2, 0, 3, 1, 1, 3, 3, 1, 1, 0, 2, 2, 1, 1, 3, 3, 0, 3, 1, 1, 1, 0, 3, 2, 0, 2, 1, 0, 3, 1, 0, 0, 1, 2, 3, 0, 1, 
1, 1, 1, 0, 3, 1, 1, 0, 1, 0, 3, 3, 3, 1, 1, 1, 1, 2, 1, 1, 3, 0, 1, 2, 0, 2, 1, 1, 3, 3, 2, 1, 3, 0, 2, 3, 3, 2, 3, 0, 1, 0, 3, 0, 2, 1, 0, 3, 3, 
3, 0, 2, 1, 3, 2, 2, 3, 0, 1, 2, 0, 3, 3, 2, 1, 0, 1, 0, 3, 1, 3, 0, 0, 0, 1, 2, 3, 3, 3, 3, 0, 2, 3, 2, 0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 2, 0, 0, 3, 
3, 1, 2, 3, 0, 1, 0, 0, 3, 2, 2, 0, 3, 0, 1, 3, 2, 0, 1, 0, 1, 3, 2, 3, 1, 1, 3, 1, 0, 1, 1, 0, 2, 3, 2, 2, 0, 3, 0, 2, 0, 2, 0, 2, 1]]

print(f"number of replicas: {len(b)}")
print(f"number of partitions: {len(b[0])}")
# print(len(b[1]))
# print(len(b[2]))

"""

# 19) compute overload

"""

devs = []

infos = [{"region":1, "zone":1, "ip":168, "weight":100.0}, 
         {"region":1, "zone":1, "ip":169, "weight":200.0},
         {"region":1, "zone":1, "ip":170, "weight":500.0}]

for info in infos:
    devs.append(info)

print(devs)

from collections import defaultdict
        
weighted = defaultdict(float)

wanted = defaultdict(float)

for dev in devs:            
    dev_tier = (dev['region'], dev['zone'], dev['ip'])
    for i in range(len(dev_tier) + 1):
        tier = dev_tier[:i]
        weighted[tier] += 0.25

for dev in devs:            
    dev_tier = (dev['region'], dev['zone'], dev['ip'])
    for i in range(len(dev_tier) + 1):
        tier = dev_tier[:i]
        wanted[tier] += 0.42

for dev in devs:
    tier = (dev['region'], dev['zone'], dev['ip'])            
    required = (wanted[tier] - weighted[tier]) / weighted[tier]

print(required)

"""

# 20) convert timestamp to datetime



from datetime import datetime
import time

timestamp = 1525346445.31161
#timestamp = int(time.time()) + 446788
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", str(dt_object))


# 21) next itertools example


"""
import itertools

name = "morteza"

data = itertools.cycle(name)

t = next(data)

a = next(data)

b = next(data)

"""

# 22) bitmap

"""
import time
import binascii
from datetime import datetime

part_moved_bitmap = bytearray(max(2 ** (10 - 3), 1))

elapsed_hours = int(time.time() - 0) // 3600

# print(time.time())

# print(datetime.fromtimestamp(time.time()))

print(elapsed_hours)
"""

# 23) enumerate

"""

desired_lengths = [1024, 1024, 256]

print(list(enumerate(desired_lengths)))

"""

# 24) itertools repeat

"""

import itertools

NONE_DEV = 2 ** 16 - 1

desired_length = [0, 2, 3, 1]

print(list(itertools.repeat(NONE_DEV, 4)))

"""

# 25) default dictionary list

"""
from collections import defaultdict

to_assign = defaultdict(list)

print(to_assign[0])
"""

# 26) part replica

"""

r2p2d = [[0,2,1,3],[1,0,3,2],[3,1,2,0]]

def each_part_replica():    
    for replica, part2dev in enumerate(r2p2d):
        for part in range(len(part2dev)):
            yield (part, replica)

for part, replica in each_part_replica():
    print(replica)

"""

# 27) some checks

"""

print(list(enumerate(r2p2d)))

part_moved_bitmap = None

part_moved_bitmap = bytearray(max(2 ** (3 - 3), 1))

print(list(part_moved_bitmap))

lst = bytearray(10)

print(list(lst))

import time

print(time.time())

print(int(1608375856.55) // 3600)

print(44 < 0xff)

print(int("0xff", 16))

"""

# 28) remove devs

"""

devs = [{"id":0, "parts":-1},{"id":1, "parts":-1}, {"id":2, "parts":-1},{"id":3, "parts":-1}]

remove_devs = [{"id":0, "parts":-1},{"id":1, "parts":-1}]

remove_dev_id = remove_devs.pop()['id']

print(remove_dev_id)

removed_devs = 0

while remove_devs:
    remove_dev_id = remove_devs.pop()['id']
    devs[remove_dev_id] = None
    removed_devs += 1

print(removed_devs)

print(devs)

"""


# 29) map function

"""

def get_len(n):    
    print(len(n))

# get_len([0,1,2,3])

map(get_len, ([0,2,5], "salam", "hello", range(1,5)))

"""


# 30) getitem example

"""

class Person():

    def __init__(self, name, age):
        self.record = {"name": name,"age": age}

    def __getitem__(self, key):
        return self.record[key]



person = Person("morteza", 29)

print(person.__getitem__("age"))

"""

# 31) some checks

"""

import random

def sort_key_for():
    return (10, random.randint(0, 0xFFFF), 0)

print(sort_key_for())

print(int("0xFFFF",16))

from collections import defaultdict

tier2sort_key = defaultdict(tuple)

tier2sort_key["a"] = (1,2,3)

print(tier2sort_key.__getitem__("a"))

print(tier2sort_key.__getitem__("b"))

"""

# 32) build_tier_tree()

"""

from swift.common.ring import utils

devs = [{"region":"r1", "zone":"z1", "ip":"s1", "weight":100.0, "id":0,"parts_wanted":682, "tiers":(('r1',), ('r1', 'z1'), ('r1', 'z1', 's1'), ('r1', 'z1', 's1', 0))}, 
                  {"region":"r1", "zone":"z1", "ip":"s2", "weight":200.0, "id":1,"parts_wanted":1024,"tiers":(('r1',), ('r1', 'z1'), ('r1', 'z1', 's2'), ('r1', 'z1', 's2', 1))},
                  {"region":"r1", "zone":"z1", "ip":"s2", "weight":50.0, "id":2,"parts_wanted":341,"tiers":(('r1',), ('r1', 'z1'), ('r1', 'z1', 's2'), ('r1', 'z1', 's2', 2))},
                  {"region":"r1", "zone":"z2", "ip":"s3", "weight":500.0, "id":3,"parts_wanted":1025,"tiers":(('r1',), ('r1', 'z2'), ('r1', 'z2', 's3'), ('r1', 'z2', 's3', 3))}]

print(utils.build_tier_tree(devs))

"""

# 33) random seed

"""

import random

lst = [10,20,30,40]

random.seed(5)

random.shuffle(lst)

print(lst)

"""

# 34) assert

"""

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")

"""


# 35) unittest

import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
