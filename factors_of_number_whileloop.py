num=int(input("Enter a number"))

temp = 1
print("the factors of {} number are ".format(num))

while temp<=num:
    if (num%temp==0):
        print("{}".format(temp))
    temp=temp+1