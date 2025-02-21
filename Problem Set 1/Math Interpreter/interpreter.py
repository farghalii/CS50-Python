expression=input("enter the expression   ").strip()
x, y, z = expression.split(" ")
if y=='+':
    print(float(x)+float(z))
elif y=='-':
    print(float(x)-float(z))
elif y=='*':
    print(float(x)*float(z))
elif y=='/' and z!=0 :
    print(float(x)/float(z))
