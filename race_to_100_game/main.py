x = int(input("Input a number between 1-9. Goal is to reach 100 before the computer: "))
if x < 1 or x > 9:
    print ("Error: Enter only numbers between 1-9")
    exit()
y = 10-x
z = x+y
print ("I pick " + str(y))
flag_error= False
while z < 100:
    x = int(input("Input another number between 1-9: "))
    if x < 1 or x > 9:
        print ("Error: Enter only numbers between 1-9")
        flag_error = True
        break
    print ("After your pick, the sum is " + str(z+x))
    y = 10-x
    print ("I pick " + str(y))
    z = z + x+y
if (not flag_error):
    print ("I win")