#Nhập thời gian
t_g = float(input("Nhập thời gian:"))
#Điều kiện thời gian
if t_g > 0:
    #Chi tiết bóng đèn
    h_d_t = 220
    cuong_do_dong_dien = 2.7
    cong_suat = 7000
    #Phép tính
    cong_suat = t_g*h_d_t*cuong_do_dong_dien/3600*1000
    #Tính
    phai_tra = cong_suat*7000
    #Kết quả
    print("Tiền phải trả là: ",phai_tra)
else:
    print("Thời gian sử dụng phải lớn hơn 0.")