# ranges
# 10 - 100
# 23 - 56
# 0 - 46

range(10, 101, 1)
range(23, 57, 1)
range(0,47)

'''for v in range(10,21,2):
    print(v) '''

# for v in range(5, 51, 5):
#     print(v)

v = int(input("Pls tell your number : "))

for s in range(v,(v*10)+1,v):
    print(s)