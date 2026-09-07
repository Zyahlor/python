# tro choi vuot nguc
nv_hp=100
zom_hp=150
nv_dmg = 30
zom_dmg = 35
health = 40
sheld = 3
while True:
    print("======= menu =======")
    print("tro choi vuot nguc")
    print("1. choi")
    print("2. thoat")
    print("3. chinh sua")
    opt = int(input("nhap lua chon:"))
    if opt ==1:
        nv_hp=100
        zom_hp=150
        sheld = 3
        print("tro choi bat dau!")
        while True:
            print("-----------------------------")
            print(f"mau cua quai vat:{zom_hp}")
            print(f"mau cua nguoi choi:{nv_hp}")
            print("nhap lua chon:")
            print("1. tan cong")
            print("2.phong thu")
            print("3. bo cuoc")
            opt_game = int(input("nhap lua chon:"))
            if opt_game == 1:
                print("-----------------------------")
                print("ban da chon tan cong!")
                zom_hp = zom_hp - nv_dmg
                nv_hp -= zom_dmg
                print(f"mau cua zombie con lai la:{zom_hp}")
                print(f"zombie da phan cong, so mau con lai:{nv_hp}")
                print("-----------------------------")
                if zom_hp <= 0:
                    print("mau zombie da ve 0,ban da thang!")
                    break
                elif nv_hp <= 0:
                    print("mau cua ban, ban da thua")
                    break

            elif opt_game == 2:
                print("-----------------------------")
                print("ban chon phong thu!")
                if sheld > 0:
                    nv_hp = nv_hp + health
                    sheld -= 1
                    print(f"mau cua ban da duoc hoi , so mau ban co la:{nv_hp}")
                    print(f"so khien con lai:{sheld}")
                else:
                    print("ban da het luot phong thu!")


            elif opt_game == 3:
                print("-----------------------------")
                print("ban da bo cuoc! ga")
                break

            else:
                print("-----------------------------")
                print("lua chon khong hop le!")

    elif opt == 2:
        print("-----------------------------")
        print("ket thuc chuong trinh!")
        break

    elif opt == 3:
        print("-----------------------------")
        print("Chinh sua nhan vat:")
        nv_dmg = int(input("Nhap sat thuong moi: "))
        health = int(input("Nhap mau hoi phuc moi: "))
        print(f"Da cap nhat! DMG:{nv_dmg} | Heal:{health}")

    else:
        print("-----------------------------")
        print("nhap sai lua chon!")