import math

x = input("Enter number x: ")
y = input("Enter number y: ")

x = int(x) #Convert x from string to integer
y = int(y) #Convert y from string to integer

p = x**y  #x to the power of y
print ("x**y = " + str(p)) #Change p from integer to string to be able to print

l = math.log(x,2) #log2 of x 
print("log2(x) = " + str(l)) #Change l from integer to string to be able to print

print ("79826")