come = int(input('Enter loop:'))
back = []
for i in range(come):
    data = int(input('Enter Data:'))
    back += [data]
print(min(back))
print(max(back))