import math
#Nhập giá trị
x = float(input("Nhập giá trị vào phương trình: "))
#Điều kiện log phải lớn hơn 0
if x>0:
    print("Giá trị của x phải lớn hơn 0")
else:
    print("Giá trị không thỏa mãn")
#Tính phương trình
log4x = math.log(x,4)
logx2 = math.log(2,x) 
y=log4x+logx2
#Tính đến số thập phân thứ 2
print(f"Giá trị của phương tình là:{y:.2f}")
   