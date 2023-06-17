import math

s = "chillout"

ss = s.split(" ")
target = "".join(ss)

l = len(target)
sqrt_l = math.sqrt(l)
row = math.floor(sqrt_l)
col = math.ceil(sqrt_l)

if row * col < l:
    row += 1

encrypted_list = []

start = 0
for _ in range(row):
    encrypted_list.append(target[start : start + col])
    start += col

res = ""
for i in range(col):
    for j in range(row):
        try:
            word = encrypted_list[j][i]
            res += word
        except Exception:
            break
    res += " "

print(res)
