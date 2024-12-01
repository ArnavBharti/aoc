row1 = []
row2 = []
with open("q1_1") as f:
    for line in f:
        n1, n2 = line.split()
        row1.append(n1)
        row2.append(n2)
row1.sort()
row2.sort()
sum = 0
for i in range(len(row1)):
    sum += abs(int(row1[i]) - int(row2[i]))
print("difference", sum)
similarity = 0
for num in row1:
    similarity += int(num) * row2.count(num)
print("similarity", similarity)