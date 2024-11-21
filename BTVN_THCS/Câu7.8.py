#Câu7.8

#Nhập hệ số :
a_1 = float(input("Nhập hệ số của a_1:"))
b_1 = float(input("Nhập hệ số của b_1:"))
c_1 = float(input("Nhập hệ số của c_1:"))
a_2 = float(input("Nhập hệ số của a_2:"))
b_2 = float(input("Nhập hệ số của b_2:"))
c_2 = float(input("Nhập hệ số của c_2:"))

#Công thức cramer
d = a_1*b_1 - a_2*b_2
d_x = c_1*b_2 - c_2*b_1
d_y = a_1*c_2 - a_2*c_2
x = d_x/d
y = d_y/d

#Điều kiện
if d != 0:
    print("Hệ có nghiệm duy nhất")
elif d_x !=0 and d_y !=0:
    print("Hệ vô nghiệm")
else:
    print("Hệ có vô sốn nghiệm")
print(f"Hệ phương trình có nghiệm duy nhất : x={x},y={y}")  