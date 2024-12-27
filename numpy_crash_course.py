

!pip install numpy

import numpy as np

"""# 1. Create"""

data = np.random.rand(2,3,4)
zeroes = np.zeros((2,2,2))
full = np.full((2,2,2), 7)
ones = np.ones((2,2,2))

data

ones

arr = np.array([[1,2,3,4],[1,2,3,4]])

type(arr)



"""# 2. Read"""

# Attributes
shape = data.shape
size = data.size
types = data.dtype

types

# Slicing
arr = data[0]
slicer = data[0][0:2]
reverse = data[-1]
singleval = data[0][0][0]

singleval

data

"""# 3. Update"""

list1 = np.random.rand(10)
list2 = np.random.rand(10)

list2

# Basic Math
add = np.add(list1, list2)
sub = np.subtract(list1, list2)
div = np.divide(list1, list2)
mult = np.multiply(list1, list2)
dot = np.dot(list1, list2)

dot

# Stat Functions
sqrt = np.sqrt(25)
ab = np.abs(-2)
power = np.power(2,7)
log = np.log(25)
exp = np.exp([2,3])
mins = np.min(list1)
maxs = np.max(list1)

maxs

data

data[0][0][0] = 700

data

data.sort()
data

print(data.shape)

data = data.reshape((2,2,-1))
data.shape

zeroes = np.zeros((8))
print(zeroes)
zeroes = np.append(zeroes, [3,4])
print(zeroes)

zeroes = np.insert(zeroes, 2, 1)
print(zeroes)

"""# 4. Delete"""

data

np.delete(data, 0, axis=1)

np.save("new array", data)

test = np.load("new array.npy")

test

