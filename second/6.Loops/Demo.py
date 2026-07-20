# ranges
# 10 - 100
# 23 - 56
# 0 - 46

''' range(10, 101, 1)
range(23, 57, 1)
range(0,47)'''

'''for v in range(10,21,2):
    print(v) '''

# for v in range(5, 51, 5):
#     print(v)

''' v = int(input("Pls tell your number : "))

for s in range(v,(v*10)+1,v):
    print(s) '''

# a = "Students"

# for i in a:
    # print(i)

# for v in range(0,len(a)):
#     print(f"{v} : {a[v]}")

# for v in range(1, 11):
#     if v == 4:
#         break
#     print(v)
# else:
#     print("Loop end 3")

# for v in range(1, 11):
#     if v == 4 or v == 6:
#         continue
#     print(v)
# else:
#     print("skip 4 & 6")

''' 1. n = int(input("tell me number: "))
for v in range(n):
    print("Hello World")

2. n = int(input("tell me number: "))
for v in range(1, n+1):
    print(v) 

3. n = int(input("Tell me your number: "))
for v in range(n,0,-1):
    print(v) 

4. n = int(input("Which table u want to know: "))

for v in range(1, 11):
    print(f"{n} x {v} = {n*v}") '''

# s = 0
# v = int(input("tell me your no where u want sum: "))
# for vs in range(1,v+1):
#     s = s + vs

s = 0
v = int(input("Tell me the number up to which you want the sum: "))

for vs in range(1, v + 1):
    s = s + vs

print("Sum =", s)