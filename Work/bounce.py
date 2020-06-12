# bounce.py
#
# Exercise 1.5

h = 100
d = 0

while d < 10:
    h = h * (3/5)
    d = d + 1
    print(d, round(h, 4))