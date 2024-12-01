column1 = []
column = []
with open("q1") as f:
    for line in f:
        n1, n2 = line.split()
        column1.append(n1)
        column.append(n2)
column1.sort()
column.sort()
sum = 0
for i in range(len(column1)):
    sum += abs(int(column1[i]) - int(column[i]))
print("difference", sum)
similarity = 0
for num in column1:
    similarity += int(num) * column.count(num)
print("similarity", similarity)