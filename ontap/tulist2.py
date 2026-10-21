
passwords = ["123456", "Admin@2024", 
             "password", "abc", "Tr0ub4dor&3", 
             "qwerty", "P@ssw0rd!", "12345678"]

"""
output:
Yeu:  ['123456', 'password', 'abc', 'qwerty', '12345678']
Manh: ['Admin@2024', 'Tr0ub4dor&3', 'P@ssw0rd!']
Luật: mật khẩu mạnh khi dài ≥ 8 và có ít nhất 1 chữ số và có ít nhất 1 ký tự đặc biệt (@ & ! #...). Còn lại là yếu.
"""
yeu = []
manh = []
so = '0123456789' 
ky_tu ='#%&*$!@' 

for i in passwords:
    if len(i) >= 8:
        co_so = False
        co_ky_tu = False 
        for chuoi in i:
            if chuoi in so :
                co_so = True
            if chuoi in ky_tu:
                co_ky_tu = True
        if co_ky_tu == True and co_so == True:
            manh.append(i)
        else:
            yeu.append(i)
    else:
        yeu.append(i)
print(manh)
print(yeu)
