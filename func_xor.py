import math
import matplotlib.pyplot as plt


def xor16bit(x, const):
    out = (x ^ const) % pow(2, 16)
    if out >= pow(2, 15):
        out ^= pow(2, 16) - 1
        out *= -1
        out -= 1
    return out


n = int(pow(2, 16 - 1))
x = [i for i in range(-n, n)]

n = 100
x = [i for i in range(0, n)]
s = [int(math.sin(2*math.pi*i/n) * pow(2, 14 - 1)) for i in range(0, n)]

y = [xor16bit(i, 0xAAAA) for i in s]
z = [xor16bit(i, 0x5555) for i in s]

plt.plot(x, z)
plt.show()
