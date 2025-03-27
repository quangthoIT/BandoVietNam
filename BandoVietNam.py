import turtle

# Thiết lập cửa sổ
win = turtle.Screen()
win.title("Bản đồ Việt Nam")
win.setup(width=800, height=600)

# Tạo đối tượng vẽ
pen = turtle.Turtle()
pen.speed(1)
pen.penup()

# Vẽ bản đồ Việt Nam
with open('VietNam.txt', 'r') as file:
    VietNam = file.readlines()

pen.color('red', 'red')
count = 0
for VietNam in VietNam:
    VN = VietNam.strip().split()
    if len(VN) == 2:
        pen.goto(float(VN[0]), float(VN[1]))
        if count == 0:
            pen.pendown()
            pen.begin_fill()
        count += 1
pen.end_fill()
pen.penup()

# Vẽ ngôi sao vàng
with open('SaoVang.txt', 'r') as file: 
    saovang = file.readlines()

pen.color("yellow", "yellow")
count = 0
for sao in saovang:
    s = sao.strip().split()
    if len(s) == 2:  # Kiểm tra số lượng phần tử
        pen.goto(float(s[0]), float(s[1])) # Đi đến toạ độ
        if count == 0: # Bắt đầu vẽ
            pen.pendown() # Đặt bút xuống
            pen.begin_fill() # Bắt đầu tô màu
        count += 1 # Đếm số lượng điểm
pen.end_fill() # Kết thúc tô màu
pen.penup()  # Nhấc bút

# Vẽ các đảo từ tệp cacdao.txt
pen.color('red', 'red')
pen.pensize(2)
with open('Dao.txt', 'r') as file:
    cacdao = file.readlines()

count = 0
for dao in cacdao:
    count += 1
    d = dao.strip().split()
    if len(d) == 2:  # Kiểm tra số lượng phần tử
        pen.goto(float(d[0]), float(d[1]))
        if count % 7 == 1:
            pen.pendown()
            pen.begin_fill()
        if count % 7 == 0:
            pen.end_fill()
            pen.penup()

pen.penup()

# Thêm tên các quần đảo Hoàng Sa và Trường Sa
pen.color('blue')  # Màu chữ

# Vẽ tên Hoàng Sa
pen.goto(200, 0)  # Tọa độ thử nghiệm cho Hoàng Sa
pen.write("Quần đảo\nHOÀNG SA", align="center", font=("Arial", 16, "bold"))

# Vẽ tên Trường Sa
pen.goto(230, -180)  # Tọa độ thử nghiệm cho Trường Sa
pen.write("Quần đảo\nTRƯỜNG SA", align="center", font=("Arial", 16, "bold"))

pen.hideturtle()

# Đợi người dùng đóng cửa sổ
win.mainloop()
