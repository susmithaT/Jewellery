a,b=0,1
for i in range(0,11):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)


