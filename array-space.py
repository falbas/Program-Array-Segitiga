a = [["1", "111", "11"], ["222", "3333", "1"], ["1111", "222222", "1"]]
n = len(a)

sl = 0
for i in range(n):
  for j in range(n):
    sl = max(sl, len(a[i][j]))
sl += 1

for i in range(n):
  for j in range(n):
    print(a[i][j], end='')
    for k in range(sl-len(a[i][j])):
      print(" ", end='')
  print()
