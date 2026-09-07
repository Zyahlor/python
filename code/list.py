# a = [5,3,8,1,9,2]
# print(a)
# #1 them 7 vao cuoi list
# a.append(7)
# print(a)
# #2 chen 99 vao idx 2
# a.insert(2,99)
# print(a)
# #3 xoa phan tu co gia tri 3
# a.remove(3)
# print(a)
# #4 xoa phan tu cuoi, in ra vua xoa
# x = a.pop()
# print(x)
# #5
# print(a)

# a = [3, 7, 1, 9, 4, 6, 2, 8, 5]
# #1 in do dai
# print(a)
# print(len(a))
# #2 in phan tu index 4
# print(a[4])
# #3 lay 3 phan tu dau
# b = a[:3]
# print(b)
# #4 them 10 vao cuoi
# a.append(10)
# print(a)
# #5 chen 99 vao index 0
# a.insert(0,99)
# print(a)
# #6 xoa phan tu co gia tri 1
# a.remove(1)
# print(a)
# #7 kiem tra 7 co trong list
# if 7 in a:
#     print("True!")
# else:
#     print("False")
# #8 kiem tra dem 10 co trong list
# print(10 in a)
# #9
# for i in a:
#     print(i)
# a = [1,2,3,4,5,6]
# print(a)
# print("-".join(map(str,a)))

# a = [1,2,3,4,5,6,7,8,9,10]
#1 tao list moi gom binh phuong phan tu
# b = [x**2 for x in a]
# print(a)
# print(b)
# chan = [x for x in a if x % 2 ==0]
# print(chan)
# le = [i for i in a if i % 2 ==1]
# print(le)
# bp = [x**2 for x in a if x % 2 == 0 ]
# print(bp)
# lon_5 = [x for x in a if x > 5]


# ## bài tập tổng hợp
# a = [15, 3, 8, 22, 7, 1, 9, 14, 6, 11]
# print(a)
# #1 in do dai
# dai = len(a)
# print(dai)
# #2 in 3 dau, 3 cuoi
# print(f"3 phan tu dau:{a[:3]}, 3 phan tu cuoi:{a[-3:]}")
# #3 tong,min,max
# ##1 tong
# print(f"tong cua mang la:{sum(a)}")
# ##2 min
# print(f"so nho nhat trong mang la:{min(a)}")
# ##3 max
# print(f"so lon nhat trong mang la:{max(a)}")

# #4 sap xep tang dan, luu vao b, kiem tra a co doi
# ##1 sap xep tang dan
# b = sorted(a)
# print(b)
# print(a)

# #5 loc chan =  list comprehension
# chan = [x for x in a if x % 2 ==0]
# print(chan)

# #6 tao list = binh phuong so le
# bp_le = [x**2 for x in a if x %2 !=0]
# print(bp_le)

# #7 kiem tra 22 va 100 co trong list ko
# print(22 in a)
# print(100 in a)
# #8 xoa phan tu nho nhat
# nhonhat=min(a)
# a.remove(nhonhat)
# print(a)
# #9 them 99 vao cuoi,chen 50 vao index 3
# a.append(99)
# print(a)
# a.insert(3,50)
# print(a)
# #10 in list
# print(a)