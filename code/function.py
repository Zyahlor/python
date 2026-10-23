import re


def binhphuong(a):
    return a*a
def hieu(a,b):
    return a-b

def is_even(n):
    return n % 2== 0
def count_even(a):
    count = 0
    for i in a:
        if is_even(i):
            count+=1
    return  count
def mx(a):
    mx_list = a[0]
    for i in range(1,len(a)):
        if mx_list < a[i]:
            mx_list = a[i]
    return mx_list
def is_prime(a):
    count = 2
    if a < 2 :
       return False 
    for i in range(2,a-1):
        if a % i == 0:
            count+=1
            print(i)
            return False
    if count == 2:
        return True 
    else:
        return False
def reverse_list(a):
    b =[]
    for i in range(len(a) -1,-1 , -1):
        b.append(a[i])
    return b
def find_max(a):
    mx = a[0]
    idx = 0
    for i,value in enumerate(a):
        if mx < value:
            mx = value
            idx = i

    return mx,idx

def analyze_numbers(number):
    max_value= mx(number)
    even = count_even(number)
    tong = 0
    for i in number:
        tong +=int(i)
    result = (max_value,even,tong)
    return result
def calculate(a,b,op="add"):
    if op == "add":
        return a+b
    elif op == "sub":
        return a-b
    elif op == "mul":
        return a*b
    else:
        return None
a = [1,2,3,4,5,56,6,8]
count = count_even(a)
mx_list =  mx(a)
c = 7
if is_prime(c)== 1:
    print(f"[+] {c} la so nguyen to!")
else:
    print(f"[!] {c} khong phai la so nguyen to!")
print(f"so lon nhat trong list la:{mx_list}")
print(f"so luong phan tu chan la:{count}")
b = reverse_list(a) 
for i in b:
    print(i)

max_value,index = find_max(a)
print(analyze_numbers(a))

print(calculate(10, 5) )         # 15
print(calculate(10, 5, "sub"))       # 5
print(calculate(10, 5, op="mul"))      # 50
print(calculate(10, 5, op="divide") )  # None
