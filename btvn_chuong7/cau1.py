import math

# Khai báo giá trị pi
pi = 3.14

# Nhập bán kính và chiều cao từ bàn phím
r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))

# Tính diện tích xung quanh
dien_tich_xung_quanh = 2 * pi * r * h

# Tính diện tích toàn phần
dien_tich_toan_phan = 2 * pi * r * (r + h)

# Tính thể tích
the_tich = pi * r**2 * h

# In kết quả và làm tròn đến chữ số thập phân thứ 2
print("Diện tích xung quanh của khối trụ là: {:.2f}".format(dien_tich_xung_quanh))
print("Diện tích toàn phần của khối trụ là: {:.2f}".format(dien_tich_toan_phan))
print("Thể tích của khối trụ là: {:.2f}".format(the_tich))
