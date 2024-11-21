#Câu3.8

#Nhập ba số từ người dùng
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

#Tìm số nhất nhất
if a >= b and a >= c:
    so_lon_nhat = a
elif b >= a and b >= c:
    so_lon_nhat = b
else:
    so_lon_nhat = c

print(f"Số lớn nhất là: {so_lon_nhat}")