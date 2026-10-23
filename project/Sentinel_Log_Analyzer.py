"""
Ý tưởng: Xây dựng công cụ phân tích log đăng nhập để
phát hiện IP có nhiều lần đăng nhập thất bại, 
thống kê tài khoản và tạo báo cáo bảo mật.

1. Bốn cấu trúc dữ liệu sẽ phối hợp thế nào?
Cấu trúc	Vai trò trong project
list	Lưu danh sách các sự kiện log theo thứ tự
tuple	Biểu diễn một sự kiện đã phân tích, gồm thời gian, trạng thái, user, IP
set	Lấy danh sách IP và tài khoản duy nhất
dict	Đếm số lần đăng nhập thành công/thất bại theo IP hoặc user

Dùng .strip() và .splitlines() để lấy các dòng log, bỏ dòng rỗng.
Duyệt từng dòng và dùng .split("|") để tách bốn trường.
Dùng strip() loại bỏ khoảng trắng quanh từng trường.
Đóng gói bốn trường thành tuple rồi thêm vào list tên events.
"""
raw_logs = """20:10:01 | FAIL | bao | 192.168.1.10
20:10:03 | FAIL | admin | 192.168.1.10
20:10:05 | SUCCESS | bao | 192.168.1.20
20:10:08 | FAIL | admin | 192.168.1.10
20:11:00 | SUCCESS | root | 192.168.1.30
20:11:05 | FAIL | bao | 192.168.1.20"""
lines =[x for x in raw_logs.split("\n") if x!=""] 
print(lines)
events = []

for line in lines:
    fields = line.split("|")

    time = fields[0].strip()
    status = fields[1].strip()
    account = fields[2].strip()
    ip = fields[3].strip()

    event = (time, status, account, ip)
    events.append(event)
print(events)
