#Câu2.8

#Nhập tọa độ
x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
a = float(input("Nhập tọa độ a của điểm I: "))
b = float(input("Nhập tọa độ b của điểm I: "))
r = float(input("Nhập bán kính R: "))
m_i = (x-a)**2 + (y-b)**2
ban_kinh = r**2
#Xét điều kiện khi MI <= R
if m_i <= ban_kinh:
    print("Nằm trong đường tròn tâm I")
    print("Đúng")
else: 
    print("Không nằm trong đường tròn tâm I")
    print("Sai")