ho_va_ten = input("Nhap vao ten:")
ten_nhap_vao = ho_va_ten.split()
ho_ten=ten_nhap_vao[0]             #Họ chạy từ 0
ten_dem=" ".join(ten_nhap_vao[1:]) #Tên đệm chạy từ 1 đến còn lại
print(f"Ho: {ho_ten}")
print(f"Ten dem: {ten_dem}")