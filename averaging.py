import re
fin = open("26.07_all_new.txt", "r")
fout = open("26.07_all_new_new.txt", "w")
text = fin.read().split('\n')

a = []
for i in range(52, len(text) - 1):
    x = text[i]
    while x[0] == " ":
        x = x[1:]
    while x[len(x) - 1] == " ":
        x = x[:len(x) - 1]
    y = re.split(' *', x)
    y = y[:9] + y[10:]
    for i in range(1, len(y)):
        y[i] = float(y[i])
    a.append(y)

for i in range(0, len(a), 10):
    b = [0.0 for j in range(1, len(a[i]))]
    for j in range(1, len(a[i])):
        for k in range(i, i + 10):
            b[j - 1] += a[k][j]

    ans = a[i][0] 
    for j in range(0, len(a[i]) - 1):
        ans += '\t' + str(b[j] / 10.0)
    fout.write(ans + '\n')
