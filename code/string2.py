# bai tap
name = "Nguyen Van An"

# dem ky tu
# so_kt =0
# print(name[0:6])
# print(name[7:10])
# print(name[11:13])
# print(f"so ky tu co trong ten la:{len(name)}")
# print(f"so tu trong ten la:{len(name.split())}")

# new = "racecar"
# if new[::-1] == new:
#     print("no la chuo palindrome!")
# else:
#     print("no khong phai chuoi palindrome!")

#Chuẩn hóa " Nguyen Van An "

# nw_name = "  nguyen  van  an  "
# name_n = nw_name.split()
# name = " ".join(name_n)
# print(name)

# new_name="nguyen van an"
# new_name = new_name.split()
# print(f"ho:{new_name[0]}")
# print(f"ten:{new_name[-1]}")

s = "admin:password123"
#1 tach username,password
acc = s.split(":")
a= acc[0]
b= acc[-1]
print(f"username:{a}")
print(f"password:{b}")
number = '0123456789'
#2 ktra pass co so khong
for i in b:
    if i in number:
        print("pass co so")
        break
else:
    print("pass khong co so")

#3 so sanh admin
a = a.lower()
if a == 'admin':
    print("dung")
else:
    print('sai')
