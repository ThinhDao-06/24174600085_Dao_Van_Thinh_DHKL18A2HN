#Bài11: 

# Danh sách sinh viên dạng [(Tên, Điểm)]
students = [("Dung", 10.0), ("Quang", 5.3), ("Trang", 7.5)]

# In tiêu đề
print(f"{'Ten':<10}{'Diem':>5}")

# In từng sinh viên trong danh sách
for name, score in students:
    print(f"{name:<10}{score:>5.1f}")
