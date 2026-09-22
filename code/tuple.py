# a = (10, 20, 30, 40, 50, 60, 70)

# # (10, 20, 30)
# print(a[0:3])

# # (50, 60, 70)
# print(a[-3:])

# #(10, 30, 50, 70)
# print(a[::2])

# # Kết quả mong đợi: (60, 50, 40, 30, 20)
# print(a[1:6])
# b = a[5:0:-1]

# print(b)
# # Bài 5 (khó hơn): Cho chuỗi s, lấy ký tự ở vị trí lẻ rồi đảo ngược
# s = "abcdefgh"
# b=[]
# # Kết quả mong đợi: 'hfdb'
# for i in range(len(s)):
#     if i % 2 != 0:
#         b.append(s[i])
# print(b)
# b = "".join(b[::-1])
# print(b)

# a = (5, 15, 25, 35, 45, 55, 65, 75)

# # Kết quả mong đợi: (5, 15, 25)
# print(a[:3])

# # Kết quả mong đợi: (25, 35, 45)
# print(a[2:5])

# # Kết quả mong đợi: (15, 35, 55, 75)
# print(a[1::2])

# # Kết quả mong đợi: (75, 65, 55, 45, 35, 25, 15, 5)
# print(a[::-1])

# # Kết quả mong đợi: (25, 35, 45, 55)
# print(a[2:7])

# # Bài 6 (khó): Cho chuỗi s, lấy ký tự vị trí chẵn, không đảo ngược, viết hoa hết
# s = "python3programming"
# # Kết quả mong đợi: 'PTO3RGAMN'
# print(s[::2].upper())

# a = (1, 2, 3, 4, 5, 6)

# # x=1, y=6
# x,*mid,y = a
# print(x,y)

# # first=1, second=2, rest=[3,4,5,6]
# f,s,*end = a
# print(f,s)

# data = ("Bao", (20, "HCMC"))
# # name="Bao", age=20, city="HCMC"
# name,(age,city) = data
# print(f"ten ban la:{name}")
# print(f"so tuoi cua ban la:{age}")
# print(f"ban dang sinh song o:{city}")

# #p, q, r = 1, 2, 3
# c = (1,2,3)
# r,p,q = c
# print(r,p,q)

# log = "192.168.1.1:8080:OPEN"
# # ip="192.168.1.1", port="8080", status="OPEN"
# log = log.split(":")
# print(log)


# pairs = [(1, "a"), (2, "b"), (3, "c")]

# 1 - index
ports = (21, 22, 53, 80, 443, 3306)

print(ports[0])  # ports[0] = 21
print(ports[-1]) # ports[-1] = 3306
print(ports[-3]) # ports[-3] = 80
print(ports[1:4])# ports[1:4]= (22,53,80)
print(ports[::-1])# ports[::-1]=(3306,443,80,53,22,21)

# 2 - nest tuple
scan = ("192.168.1.10",(22, 80, 443),"Linux")
print(f"IP:{scan[0]} | port:{scan[1][1]} | OS:{scan[2]}")

# 3 - slice
ports = (21, 22, 23, 25, 53, 80, 110, 443)
# 1 - 3 port dau -> ports[0:3]
print(ports[0:3])
# 2 - 3 ports cuoi -> ports[-3:]
print(ports[-3:])
# 3 - lay ports vi tri chan
print(ports[::2])
# 4 - dao nguoc tuple
print(ports[::-1])
# 5 - lay 23,53,80
print(ports[2:3] + ports[4:6])

# 6 - unpacking
result = ("192.168.1.10", 443, "open")
ip,port,status = result
print(f"IP:{ip} | port:{port} | status:{status}")

# 7 — Mini project: Port Scanner Result
results = (
    ("192.168.1.10", 22, "open"),
    ("192.168.1.10", 80, "open"),
    ("192.168.1.10", 443, "open"),
    ("192.168.1.10", 3306, "closed"),
)
for i in range(len(results)):
    ip,port,status = results[i]
    if status == 'open':
        print(f"IP:{ip} | port:{port} | status:{status}")