#- Nhập list
# - Tính tổng
# - Đếm chẵn/lẻ
# - Tìm max/min
# - Tìm kiếm
# - Xóa phần tử
# - Đảo list
# - Tìm số lớn thứ hai
# - Lọc số nguyên tố
# - Sort thủ công

#1 nhap list
nhap = list(map(int , input("nhap list(co the nhap nhieu = cach nhau):").split()))
print(nhap)
#tinh tong
print(f"tong:{sum(nhap)}")
#dem chan le
dem=0
dem1=0
for i in nhap:
    if i % 2==0:
        dem+=1
print(f"co {dem} so chan trong list!")
for i in nhap:
    if i % 2!=0:
        dem1 +=1
print(f"co {dem1} so le trong list!")
#tim max min
max = max(nhap)
min = min(nhap)
print(f"lon nhat la:{max}, nho nhat la:{min}")
#tim kiem
if 10 in nhap:
    print(f"co 10 trong diem da nhap!")
else:
    print("khong co diem 10 nao ca!")
#xoa phan tu
# xoa = int(input("nhap phan tu can xoa:"))
# nhap.remove(xoa)
#dao list
a= sorted(nhap,reverse=True)
print(a)
#tim so lon thu 2
lon2 = 0
for  i in nhap:
    if i < max:
        if i > lon2:
            lon2 = i
print(f"so lon thu 2 la:{lon2}")
# Lọc số nguyên tố
nguyen_to = []
for i in nhap:
    dem =0
    if i < 2:
        continue
    for j in range(1,i+1):
        if i % j == 0:
            dem +=1
    if dem == 2:
        nguyen_to.append(i)
print(nguyen_to)
