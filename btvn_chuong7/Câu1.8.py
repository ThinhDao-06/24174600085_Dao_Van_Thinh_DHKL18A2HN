#Câu1.8
year = int(input("Nhập năm: "))
#Điều kiện: Năm nhuận chia hết cho 4, không chia hết cho 100 hoặc chia hết cho 400
if year %4 == 0 and year %100 !=0 or year %400 == 0:
    print("Là năm nhuận")
else: 
    print("Không phải là năm nhuận, vui lòng nhập lại")
    