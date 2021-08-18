def my_list(ber):
    for i in ber:
        print(i)

num = ['5','10','15','20','25','50','20']
for i in range(len(num)):   
   if (num[i] == '20'):
        num[i] = '200'
my_list(num)

