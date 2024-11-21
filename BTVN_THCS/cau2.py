import math 
# Nhập giá trị biểu thức
x = float(input("Nhập giá trị biểu thức x: "))
# Điều kiện của biểu thức
if x>=0 and x!=0: 
    print("Giá trị không được âm hoặc bằng 0")
else:
    print("Giá trị không thỏa mãn")
# Tính giá trị biểu thức
f_x = -x+math.sqrt(x**2 + 4)/math.pow(x**4+1,1/7)
# Kết quả
print(f"Giá trị biểu thức: {f_x:.2f}")
print("Kết thúc chương trình")