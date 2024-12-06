#Bài12:


# Danh sách sinh viên dạng [(Tên, Điểm)]
students = [("Dung", 10.0), ("Quang", 5.3), ("Trang", 7.5)]

# In danh sách ban đầu
print("Danh sách sinh viên ban đầu:")
print(f"{'Ten':<10}{'Diem':>5}")
for name, score in students:
    print(f"{name:<10}{score:>5.1f}")

# Nhập tên sinh viên cần xóa
name_to_delete = input("\nNhập tên sinh viên cần xóa: ")

# Xóa sinh viên khỏi danh sách
students = [student for student in students if student[0] != name_to_delete]

# In danh sách sau khi xóa
print("\nDanh sách sinh viên sau khi xóa:")
if students:
    print(f"{'Ten':<10}{'Diem':>5}")
    for name, score in students:
        print(f"{name:<10}{score:>5.1f}")
else:
    print("Danh sách rỗng.")
