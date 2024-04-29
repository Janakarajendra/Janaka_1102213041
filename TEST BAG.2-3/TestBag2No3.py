
def raw_input():
o = int(raw_input("Masukin Angka Genap= "))
x=2
for i in range(o):
    if i<=(o/2):
        print(" "*((o/2)-(i-1)) + "*"*i + "*"*(i-1))
    else:
        print(" "*(1*x)+"*"*(o-i) +"*"*(o-(i+1)))
        x=x+1