print("hello,World!")
print("=== text analyzer ===")
data = "hello world hello python python python"#input("nhap text can phan tich:")
print(f"chuoi:{data}")
sokytu = len(data) # dem so ky tu
data = data.strip() # xoa khaong cach dau cuoi
data = data.split() # tach cac tu trong chuoi = khoang cach => data = list
nudata = len(data) #  dem phan tu trong list
print("=== ket qua ===")
# so ky tu
print(f"so ky tu trong text la:{sokytu - (nudata -1 ) }") # sokytu da tru di khoang cach
# so tu ( cai nay da lam doan data.splist() )
print(f"so tu trong chuoi la:{nudata}")
# tim tu xuat hien nhieu nhat trong chuoi
dem,idx = 0,-1
for i in range(nudata):
    dem1 = 0
    for j in range (i+1,nudata):
        if data[i] == data[j]:
            dem1+=1
    if dem1 > dem:
        dem = dem1
        idx = i
        thongtin = (data[idx],dem+1)
if idx == -1:
    print("khog co tu xuat hien nhieu nhat!")
else:
    print(f"tu xuat hien nhieu nhat:{data[idx]}")
print(f"xuat hien nhieu nhat:{thongtin[0]} voi {thongtin[1]} lan xuat hien!")
# cac tu duy nhat dung set 
duynhat =  set(data)
print(f"cac tu duy nhat:{duynhat}")
# tu dau tien => ap dung idx lay tu list
print(f"tu dau tien trong chuoi la:{data[0]}")
# tu cuoi cung y cach lam y chang tren
print(f"tu cuoi cung:{data[-1]}")
