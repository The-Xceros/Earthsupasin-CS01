Num = int(input('Enter loop'))
NumTotal = []
for i in range(Num):
    data = int(input('Enter Data'))
    NumTotal += [data]
print(NumTotal)
NumTotal.sort()
print(NumTotal)