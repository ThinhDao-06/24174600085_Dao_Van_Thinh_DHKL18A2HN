diem_chuyen_can = float(input("Nhập điểm chuyên cần: "))
diem_giua_ky = float(input("Nhập điểm giữa kỳ: "))
diem_cuoi_ky = float(input("Nhập điểm cuối kỳ: "))
diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky) / 3
if diem_trung_binh >= 9:
    loại = "A"
elif diem_trung_binh >= 7:
    loai = "B"
elif diem_trung_binh >= 5:
    loai = "C"
else:
    loai = "D"
print(f"Điểm của sinh viên là: {diem_trung_binh:.2f}")
print(f"Xếp loại: {loai}")
