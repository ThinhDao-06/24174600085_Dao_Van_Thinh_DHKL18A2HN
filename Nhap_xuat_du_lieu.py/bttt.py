a,b,c = map(int, input ("nhập a,b,c")).split()
delta = float(b*b-4*a*c)
if delta <0:
    print("phương trinh vô nghiệm ")
elif delta ==0:
    print ("phương trình có nghiệm kép ")
    print ("x=", -b/2*a)
else:
    print("phương trình có 2 nghiệm kép ")

print("x1= 0=", (-b+math.sprt (delta))/(2*a))
print("x1= 0=", (-b-math.sprt (delta))/(2*a))