# Bài 7: viết hàm min_max(a) trả về (nhỏ nhất, lớn nhất) của list
# rồi unpack kết quả vào 2 biến lo, hi
# min_max([4, 7, 1, 9, 3]) → lo=1, hi=9
def min_max(ds):
    return min(ds), max(ds)

lo, hi = min_max([4, 7, 1, 9, 3])
print(lo, hi)    # 1 9
# Bài 8: lọc kết quả scan
scan = [
    ("10.0.0.1", 80, "open"),
    ("10.0.0.1", 22, "closed"),
    ("10.0.0.2", 443, "open"),
    ("10.0.0.3", 21, "filtered"),
]
# In ra các dòng open theo dạng "10.0.0.1:80"
# Gợi ý duy nhất: dùng unpacking trong vòng for
# TODO
for ip,port,status in scan:
    if status == 'open':
        print(f"{ip} | port:{port} | status:{status}")
# Bài 9: cho tuple 6 phần tử 
t = (1, 2, 3, 4, 5, 6)
# Dùng unpacking lấy: phần tử đầu, phần tử cuối, và list phần giữa
# TODO → 1 6 [2, 3, 4, 5]
x,*mid,y = t
print(f"x:{x}|y:{y}|mid:{mid}")

# Bài 10: dùng tuple làm key trong dict
# Lưu trạng thái: (ip, port) → status, rồi tra "10.0.0.1", 80
status = {}
status[('1.1.1.1',80)] ='open' 
print(status[('1.1.1.1',80)])
# TODO: thêm 3 mục tùy ý, rồi in status[("10.0.0.1", 80)]
