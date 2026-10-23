# f de giu doi tuong file
# open("data.txt","r") mo file de doc

# f = open("data.txt","r")
# data = f.read()  f.read() doc noi dung file - data chua toan bo noi dung doc
# print(data)
# f.close()  dong file lai

# cach tren buoc phai mo file ra de doc va phai dong thu cong file

# cach 2
# with open("data.txt","r") as f:
#     data = f.read()
# print(data)
#
# as f = dat ten f cho doi tuong file dang mo  
# with tu dong file khi ra khoi lenh, ke ca loi khi xu ly

# read tung dong
# dung readline()
with open("data.txt","r") as f:
    # data4=f.readlines()
    data1=f.readline()
    data2=f.readline()
    data3 =f.readlines()

print(data1)
print(data2)
print(data3)
# print(data4)
# dem so dong
with open("data.txt","r")as f:
    lines = f.readlines()
    count = len(lines)
print(count)

#ghi du lieu vao file
with open("programming.txt","w") as f:
    f.write("c++\n")
    f.write("python\n") 
    f.write("networking\n")

with open("programming.txt","r") as f:
    data =  f.read()
    lines = f.readlines()
print(data)
print(lines)

# tim tu trong file

# 1. tao file log.txt
raw_log="""
User Bao login success
User An login failed
User Minh login success
User Bao login failed
User An login failed
"""
with open("log.txt","w") as f:
    f.write(raw_log)

count = 0
with open("log.txt", "r") as f:
    log_line = f.readlines()

for line in log_line:
    if "failed" in line:
        print(line.strip())
        count += 1
print(f"so lan dang nhap that bai:{count}")

# keyword = input("nhap tu khoa de tim:")
# for line in log_line:
#     if keyword in line:
#         print(line.strip())

# neu khong thich phan biet hoa - tuong
# demo 
# keyword = input("nhap tu khoa:").lower()
# for line in log_line:
#     if keyword in line.lower():
#         print(line.strip())

user =set() 
for i in log_line:
    if "failed" in i.lower():
       data = i.split(" ")
       user.add(data[1])
print(user)
print(f"so nguoi dang nhap that bai:{len(user)}")

print("======================")
raw_log2 = """
2026-10-22 20:01:05 192.168.1.10 login success
2026-10-22 20:02:11 192.168.1.20 login failed
2026-10-22 20:03:45 192.168.1.10 login failed
2026-10-22 20:04:02 192.168.1.30 login success
2026-10-22 20:05:19 192.168.1.20 login failed
"""
with open("log2.txt","w") as f:
    f.write(raw_log2)
clean_log = []
with open("log2.txt","r") as f:
    data = f.readlines()
for line in data:
    parts=line.split()
    if "failed" in line:
        print(f"{parts[2]}")

failer ={} 
for i in data:
    line = i.split()
    if "failed" in line:
        if line[2] not in failer:
            failer[line[2]] = 1 
        else:
            failer[line[2]] +=1 
for ip,status in failer.items():
    print(f"{ip}:{status} lan")

# for ip,status in failer.items():
#     if status >=2 :
#         print(f"{ip}:{status} lan")
log_status = {}
for i in data:
    line = i.split()
    if len(line) < 5:
        continue
    elif line[2] not in log_status:
       log_status[line[2]]={"success":0,"failed":0}

for i in data:
     line = i.split()
     if len(line) < 5:
         continue
     if "failed" in line:
         log_status[line[2]] ["failed"]+=1
     elif "success" in line:
         log_status[line[2]]["success"]+=1
print(log_status)
