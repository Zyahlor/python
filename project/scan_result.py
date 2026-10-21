def add_result(result,ip,port,service):
    record = (ip,port,service)
    result.append(record)
def lay_port(record):
    return record[1]
scan_old = [("192.168.1.10", 22, "ssh"), ("192.168.1.10", 80, "http"),
            ("192.168.1.20", 445, "smb"), ("192.168.1.20", 445, "smb")]
scan_new = [("192.168.1.10", 22, "ssh"), ("192.168.1.10", 443, "https"),
            ("192.168.1.30", 3389, "rdp")]

for ip,port,service in scan_old:
    print(f"IP:[{ip}] | PORT:[{port}] | SERVICE:[{service}]")

print("=== sap xep theo port tang dan === ")
# lambda = ham an danh , dung cho cac tac vu don gian
sort_scan= sorted(scan_old ,key=lambda r:r[1] ,reverse=True) # key=lambda = lay gia tri idx cua tuple
for ip,port,service in sort_scan:
    print(f"IP:[{ip}] | PORT:[{port}] | SERVICE:[{service}]")

print("add new_scan:")
add_result(scan_new,"192.168.1.10",1234,"http")
for ip,port,service in scan_new:
    print(f"IP:[{ip}] | PORT:[{port}] | SERVICE:[{service}]")

print("=== set ===")
scan_new = set(scan_new)
for ip,port,service in scan_new:
    print(f"IP:[{ip}] | PORT:[{port}] | SERVICE:[{service}]")


