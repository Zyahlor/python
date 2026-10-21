ds = {}
sv = []
number = int(input("nhap so luong sv:"))
for i in range(number):
    data = input("nhap ten sinh vien:")
    sv.append(data)
print(sv)
print("=== nhap diem ===")
for i in sv:
    if i not in ds:
        ds[i] = int(input(f"nhap diem cua {i}:"))
        if ds[i] > 10 or ds[i] < 0:
            print("[!] diem ko hop le!")
            del ds[i]
for key,value in ds.items():
    print(f"{key}:{value}")

while True:
   print("== menu ==")
   print("1.them sv")
   print("2.tim diem theo ten")
   print("3.cap nhap diem")
   print("4.liet ke sinh vien tu 8 tro len")
   print("5.hien thi toan bo danh sach")
   print("6.thoat")
   n = int(input("nhap lua chon:"))

   if n == 1:
       print("them sinh vien moi")
       name = input("nhap them ten sinh vien:")
       if name in ds:
           print(f"[!] ten {name} da co trong he thong")
       else:
           ds[name] = int(input(f"nhap diem cho sinh vien {name}:"))
           if ds[name] < 0 or ds[name] >10:
               print("[!] diem khong hop le!")
               del ds[name]
           else:
               print(f"[+] {name}:{ds[name]}")
   elif n ==2:
       print("tim diem theo ten")
       name = input("nhap ten sinh vien:")
       if name in ds:
           print(f"{name}:{ds[name]}")
       else:
           print("[!] khong co sinh vien nay!")
   elif n == 3:
    print("sua diem")
    name = input("nhap ten sinh vien:")

    if name in ds:
        score = int(input(f"nhap diem moi cho sinh vien {name}:"))

        if score > 10 or score < 0:
            print("[!] diem khong hop le!")
        else:
            ds[name] = score
            print(f"[+] {ds[name]}")
    else:
        print("[!] khong co sinh vien nay")
   elif n == 4:
       print("=== liet ke sinh vien tu 8 tro len ===")
       for key,value in ds.items():
           if value >= 8:
               print(f"{key}:{value}")
   elif n == 5:
        print("hien thi toan bo danh sach sinh vien")
        for key,value in ds.items():
         print(f"[+] {key}:{value}")
   elif n == 6:
       break
   else:
       print(f"[!] lua chon ko hop le!")
