# vong lap: while, for
# > while python == while c++ => can dieu kien de chay

# print("kiem tra chan le:")
# n = int(input("nhap gia tri de biet do la chan hay le(nhan 0 de thoat):"))

# while n != 0:
#     n = int(input("nhap gia tri de biet do la chan hay le(nhan 0 de thoat):"))
#     if n % 2 == 0:
#         print(f"{n} la so chan!")
#     else:
#         print(f"{n} la so le!")

# print("tinh tong:")

# n = int(input("nhap so tu 1-10:"))
# sum =0
# for i in range(1,n+1):
#     sum +=i
# print(sum)

# info = {"name": "bao", 
#         "age":20,
#         "school":"cao thang"}
# for i,value in info.items():
#     print(f"infomation:{i} -> values:{value}" )


# targets = ["192.168.1.1", "192.168.1.254", "10.0.0.1"]
# for idx, ip in enumerate(targets, start=1):
#     print(f"Target #{idx}: {ip}")

# print("bai 1:")
# fruits = ["apple", "banana", "mango", "grape", "orange"]
# for index,fruit in enumerate(fruits, start = 1):
#     print(f"{index}:{fruit}")


# print("bai 2:")
# ports = [21, 22, 80, 443, 8080, 3306, 23]
# for idx,port in enumerate(ports,start=1):
#     if port != 23 :
#         print(f"target {idx}:{port}")
#     else:
#         print(f"target {idx}:{port} - telnet, khong an toan")


# print("bai 3:")
# scan_results = ["open", "closed", "open", "filtered", "open", "closed"]
# ports = [22, 23, 80, 443, 8080, 3306]
# for idx, (port,status) in enumerate(zip(ports,scan_results),start=1):
#     if status == "open":
#         print(f"Target {idx}:{port} - {status}")


# print("bai 4:")
# attempts = 0
# max_attempts = 5
# password = "admin123"
# while attempts <= max_attempts:
#     attempts += 1
#     print(f"attempt #{attempts}: trying ...")
#     if attempts ==3:
#         print(f"Found! after {attempts} attempts")
#         break
#     if max_attempts == attempts:
#         print("failed after 5 attempts")

# print("bai 5:")
# open_ports = [21, 22, 80, 443, 8080]
# target_port = 9999
# for port in open_ports:
#     if port == target_port:
#         print(f"port {port} is open!")
#         break
# else:
#     print(f"port {target_port} is close/filtered!")

# print("bai 6:")
# services = ["ftp", "ssh", "http", "telnet", "https", "rdp"]
# dangerous = ["ftp", "telnet", "rdp"]

# for idx,service in enumerate(services,start=1):
#     if service in dangerous:
#         print(f"target #{idx}| service:{service}")
#     else:
#         print(f"target #{idx}| service:{service}| dangerous")

# print("bai 7:")
# hosts = ["web01", "db01", "mail01", "proxy01"]
# ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]
# status = ["online", "offline", "online", "offline"]

# for idx,(host,ip,status) in enumerate(zip(hosts,ips,status),start=1):
#     if status == "offline":
#         print(f"#{idx} | {host} | {ip} | {status}")

# print("bai 8:")
# wordlist = ["password", "123456", "admin", "letmein", "secret"]
# correct = "letmein"
# n = 0
# while n < len(wordlist):
#     if correct == wordlist[n]:
#         print(f"Cracked!...")
#         break
#     n+=1

# print("bai 9")
# subnet = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"]
# target = "192.168.1.5"

# for i in subnet:
#     if i == target:
#         print("host is up!")
#         break
# else:
#     print("host unreachable!")


# print("bai 10:")
# ports = [22, 80, 23, 443, 21, 8080, 3306]
# status = ["open", "open", "open", "closed", "open", "filtered", "open"]
# dangerous_ports = [23, 21]
# target_port = 443

# for idx,(port,status) in enumerate(zip(ports,status),start=1):
#     if status == "open":
#         if port in dangerous_ports:
#             print(f"#{idx}|{port}|{status}|dangerous!")
            
#         else:
#             print(f"#{idx}|{port}|{status}")
#         if port == target_port:
#             print(f"found! is {port}")
#             break
# else:
#     print("can't found the target port!")

# print("bai 11:")

# role = "admin"
# valid_roles = ["admin", "moderator", "superuser"]
# if role in valid_roles:
#     print("access")
# else:
#     print("denied")

# print("bai 12:")
# response_code = 404
# success_codes = [200, 201, 204]
# error_codes = [400, 401, 403, 404, 500]

# if response_code in success_codes:
#     print("request ok")
# elif response_code in error_codes:
#     print("requets failed")
# else:
#     print("unknown code")

# print("bai 13:")
# packets = [
#     {"ip": "192.168.1.1", "port": 80},
#     {"ip": "10.0.0.1", "port": 23},
#     {"ip": "172.16.0.1", "port": 443},
#     {"ip": "10.0.0.2", "port": 21},
# ]
# blacklist_ip = ["10.0.0.1", "10.0.0.2"]
# dangerous_ports = [23, 21]

# for i in packets:
#     if i["port"] in dangerous_ports:
#         print(f"{i['ip']}:{i['port']} | dangerous port!")
#     elif i["ip"] in blacklist_ip:
#         print(f"{i['ip']} | blocked IP!")
#     else:
#         print(f"{i['ip']}:{i['port']} | ✅ OK")

# print("bai 14:")
# allowed_ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
# request_ip = "10.0.0.2"

# if request_ip in allowed_ips:
#     print("access!")
# else:
#     print("denied!")

# print("bai 15:")
# scan = ["open", "closed", "open", "filtered", "open", "closed"]
# print(f"co {len(scan)} ports da tim thay")

# print("bai 16:")
# logs = [
#     {"ip": "192.168.1.1", "action": "login", "status": "success"},
#     {"ip": "10.0.0.1", "action": "login", "status": "failed"},
#     {"ip": "192.168.1.1", "action": "download", "status": "success"},
#     {"ip": "10.0.0.1", "action": "delete", "status": "failed"},
# ]
# for i in logs:
#     if i["status"] == "failed":
#         print(i)

# print("bai 17:")
# login_attempts = {
#     "192.168.1.1": 2,
#     "10.0.0.1": 7,
#     "172.16.0.1": 1,
#     "10.0.0.2": 9,
# }
# threshold = 5

# for i,count in login_attempts.items():
#     if count > threshold:
#         print(f"ip:{i}|threshold:{count}|Brute force detected: IP")

# print("bai 18:")
# firewall_rules = [
#     {"ip": "10.0.0.1", "port": 22, "action": "block"},
#     {"ip": "192.168.1.1", "port": 80, "action": "allow"},
#     {"ip": "10.0.0.2", "port": 23, "action": "block"},
#     {"ip": "172.16.0.1", "port": 443, "action": "allow"},
# ]
# dangerous_ports = [22, 23]

# for i in firewall_rules:
#     if i["action"] == "block":
#         print(f"ip:{i['ip']} | port:{i['port']} | block")
#     elif i["action"] == "allow" and i["port"] in dangerous_ports:
#         print(f"ip:{i['ip']} | port:{i['port']} | allow but risky")
#     else:
#         print(f"ip:{i['ip']} | port:{i['port']} | ok")

# print("bai 19:")

# users = [
#     {"name": "bao", "role": "admin", "login": 3},
#     {"name": "an", "role": "user", "login": 8},
#     {"name": "binh", "role": "user", "login": 1},
#     {"name": "cuong", "role": "admin", "login": 6},
# ]
# threshold = 5

# for i in users:
#     if i['role'] == 'user' and i['login'] > threshold:
#         print(f"name:{i['name']} | role:{i['role']} | login:{i['login']}")

# n = int(input("nhap so can kiem tra nguyen to:"))
# dem =0
# for i in range(2,n//2):
#     if n % i == 0:
#         dem+=1
# if dem == 0:
#     print(f"{n} la so nguyen to!")
# else:
#     print(f"{n} khong phai la so nguyen to")