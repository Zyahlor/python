# tao may bien doi chu
print("may bien doi chu")
name =  input("nhap chuoi ma ban can bien doi: ")
while True:
    print(f"chuoi cua ban la:[{name}]")
    print("-----------------------------")
    print("===== menu =====")
    print("1. chu hoa")
    print("2. chu thuong")
    print("3. xoa khoang chan chu")
    print("4. dem do dai chu")
    print("5. tach chu thanh list, muon dung lam gi thi lam")
    print("6. doi tu trong chuoi")
    print("7. so tu trong chuoi")
    print("8. tim tu trong chuoi")
    print('0. thoat')
    opt = int(input("nhap lua chon ma ban muon:"))
    if opt == 1:
        a = name.upper()
        print(a)
    elif opt == 2:
        b = name.lower()
        print(b)
    elif opt == 3:
        c = name.strip()
        print(c)
    elif opt == 4:
        total = len(name)
        print(f"tong chuoi:{total}")
    elif opt == 5:
        ds = name.split()
        print(ds)
    elif opt == 6:
        old = input("nhap tu can thay the: ")
        new = input("nhap tu moi:")
        s = name.replace(old,new)
        print(f"chuoi moi:{s}")
    elif opt == 7:
        so_tu = len(name.split())
        print(f"so tu trong chuoi la:{so_tu}")
    elif opt == 8:
        char = input("nhap ky tu can tim: ")
        vitri = name.find(char)
        if vitri != -1 :
            print(f"co trong chuoi, o vitri: {vitri}")
        else:
            print("khong co")
    elif opt == 0:
        print("ket thuc chuong trinh")
        break
    else:
        print("chon sai!")


