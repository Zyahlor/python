# Dữ liệu giả lập (sau này thay bằng đọc file / output nmap)
def parse_line(line):
    ip,port,status = line.split(":")
    port = int(port)
    return ip,port,status
raw = """10.0.0.1:80:open
10.0.0.1:22:closed
10.0.0.2:443:open
10.0.0.3:3389:open
10.0.0.3:21:filtered
10.0.0.1:80:open"""

lines = raw.split("\n")
risky = [21, 23, 445, 3389]
""" 
Parse tất cả dòng bằng parse_line
Loại dòng trùng
In các port open, dạng ip:port
In riêng các port open nằm trong risky kèm chữ [!] NGUY HIEM
In thống kê: bao nhiêu open / closed / filtered
"""
new = [parse_line(x) for x in lines ]
print(new)
new_ip = []
for i in new:
    if i not in new_ip:
        new_ip.append(i)
print(new_ip)
dem_open =0
dem_closed = 0
dem_filtered = 0
dem_unknow = 0
for i in new_ip:
    if i[2] == 'open':
        if i[1] in risky:
         print(f"{i[0]}:{i[1]} [!] NGUY HIEM")
        else:
         print(f"{i[0]}:{i[1]}")
        dem_open+=1
    elif i[2] == 'closed': 
        dem_closed+=1
    elif i[2] == 'filtered':
        dem_filtered+=1
    else:
        dem_unknow+=1
print("==== tong ket ====")
print(f"open:{dem_open} | closed:{dem_closed} | filtered:{dem_filtered} | unknow:{dem_unknown}")
