
def parse_line(a):
        ip,log = a.split()
        return ip,log
def find_suspicious(fail, threshold=2):
    result = []
    for key,value in fail.items():
        if value >= threshold:
            result.append(key)
    return result

def analyze_log(raw_logs,threshold =3):
    new_log =[]
    for i in raw_logs:
        result = parse_line(i)
        new_log.append(result)
    count = {}
    for i in new_log:
         if i[1] not in count:
            count[i[1]] = 1 
         else:
            count[i[1]]+=1
    fail = {}
    for i in new_log:
         if i[1] == "LOGIN_FAILED":
            if i[0] not in fail:
               fail[i[0]] = 1
            else:
               fail[i[0]] +=1
    return count,find_suspicious(fail,threshold)
raw_logs = [
    "192.168.1.10 LOGIN_SUCCESS",
    "192.168.1.20 LOGIN_FAILED",
    "192.168.1.20 LOGIN_FAILED",
    "192.168.1.10 LOGOUT",
    "192.168.1.30 LOGIN_FAILED",
]
count= {}


print("=== LOG  ===")
for key,value in count.items():
    print(f"{key}:{value}")

# print("=== IP LOGIN_FAILED ===")
# for key,value in fail.items():
#     print(f"{key}:{value}")

# suspicious_ips = find_suspicious(fail) 
# for key,value in fail.items():
#     if value >=2:
#         suspicious_ips.append(key)
# print(f"IP dang nghi:{analyze_log(raw_logs)}")
counts, suspicious = analyze_log(raw_logs, 2)

print(counts)
print(suspicious)
