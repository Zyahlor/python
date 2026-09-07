# 26 - 08 - 2026
# string

#slice "hello,world"

s = "hello,world"
print(s)
print(s[0:5]) # 'hello' -> lay tu idx 0 -> 5
print(s[6:])  # 'world' -> lay tu 6 -> het
print(s[::-1])# 'dlrow,olleh' -> day la step, am = dao ngc chuoi
print(s[0:5:2])# 'hlo' -> start = 0 , stop = 5 , step = 2

print(f"do dai cua chuoi s la:{len(s)}")

a = s[0:5]     # a = "hello"
print(a)       
print(a.upper()) # "HELLO"

b = s[6:]       # b = "world"
print(b)    
print(b.upper())#"WORLD"
print(b.lower())#"world"

b = "   Le dinh Bao  "
print(f"{b.strip()}") # "Le dinh Bao"
print(b)    # "   Le dinh Bao   "

c = "ip address is : 192.168.1.1"
print(c.split())  #["ip","address","is",":","192.168.1.1"]
print(c.split('.'))#["ip address is : 192","168","1","1"]

print(s)
print(s.split(","))
print(len(s.split(",")))