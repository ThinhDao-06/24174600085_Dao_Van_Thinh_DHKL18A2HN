#Bài11

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))


x, y = a, b
while y != 0:
    x, y = y, x % y

ucln = x

# Tính BCNN dựa trên công thức BCNN= 
#BCNN= 
#UCLN(a,b)∣a×b
bcnn = abs(a * b) // ucln
print(f"Bội chung nhỏ nhất của {a} và {b} là: {bcnn}")