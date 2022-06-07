# print all intigers from 0 to 150

for x in range(0, 151):
    print(x)



# print all the multiples of 5 from5 to 1,000
for y in range(5, 1001, 5):
    print(y)





for i in range (1,101,1):
    if i % 5 == 0:
        print ('Coding')
    if i % 10 == 0:
        print ('Dojo')





for z in range(1, 101, 1):
    if z % 10 == 0:
        print("Doding Dojo")
    elif z % 5 == 0:
        print("coding")
    else:
        print(z)





sum = 0

for i in range(500001):
    if(i % 2 != 0 ):
        sum += i

        print(sum)


for x in range(2018,-1,-4):
    print(x)


low_num = 2
high_num = 9
mult = 3

for l in range(low_num,high_num + 1):
    if l % mult == 0:
        print(l)

