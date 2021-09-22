tot = 0
a = 1
b = 1
h = 0

while h <= 4000000:
    if h % 2 == 0:
        tot += h
    a = b
    b = h
    h = a + b

print(tot)