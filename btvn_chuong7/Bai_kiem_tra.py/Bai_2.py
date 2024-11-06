#Bài2

#S1
tong_s1 = 0
n = int(input("Nhap vao gia tri nguyen duong: "))
for i in range(n+1):
    tong_s1 = tong_s1 + i
    if i > 0:
        print(f"Tong cac so tu nhien: {tong_s1}")
#S2
tich_s2 = 1
n = int(input("Nhap vao gia tri nguyen duong: "))
for i in range(n-1):
    if i > 0:
        tich_s2 = tich_s2 * i
        print(f"Tich cac so tu nhien: {tich_s2}")
#S3
s3 = 0
n = int(input("Nhap cac so nguyen duong: "))
for i in range(1, n+1):
    s3 = (-1)**(i+1) / i
    print(f"Tong s3 den n = {n} la: {s3}")   
#S4
s4 = 0
n = int(input("Nhap gia tri nguyen duong: "))
for k in range(n):
    s_4 = s4 + k / (k+2)
    print(f"Tong s4 den k = {n} la: {s4}")
