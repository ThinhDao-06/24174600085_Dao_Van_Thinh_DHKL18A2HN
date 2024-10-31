#Câu6.8

#Menu phim
print("Chào mừng bạn đến rạp chiếu phim ABC")
print("Vui lòng chọn phim bạn muốn xem")
print("1: Phim tình cảm")
print("2: Phim kinh dị")
print("3: Phim hoạt hình")
print("4: Phim khoa học viễn tưởng")
#Nhập lưa chọn
lua_chon = float(input("Nhập bộ phim bạn muốn lựa chọn (1->4):"))
if lua_chon == 1:
    print("Phim tình cảm")
elif lua_chon == 2:
    print("Phim kinh dị")
elif lua_chon == 3:
    print("Phim hoạt hình")
elif lua_chon == 4:
    print("Phim khoa học viễn tưởng")
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn lại")