x = input().strip()

sum = 0
for i in range(12):
    sum += (13-i) * int(x[i])
n12 = (11 - sum%11) % 10

print(x[0] + " "
      + x[1:5] + " "
      + x[5:10] + " "
      + x[10:12] + " "
      + str(n12))