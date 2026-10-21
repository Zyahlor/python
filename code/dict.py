student = {
    "name": "An",
    "age": 18,
    "score": 7.5
}
# dung del "age"
del student["age"]
# dung pop() xoa "score" va luu bien
score = student.pop("score")
print(score)

# .get() lay score - chua co thi return 0
a = student.get("score",0)
if "score" in student:
    print(student["score"])
else:
    print("Chua co diem")
print(student.keys())

print(student.values())
print(student.items())

scores = {
        "toan":8,
        "van":7,
        "anh":9
        }
for key,value in scores.items():
    print(f"{key}:{value}")

fruits = ["tao", "cam", "tao", "chuoi", "cam", "tao"]
count={}
for key in fruits:
    if key not in count:
        count[key] = 1
    else:
        count[key]+=1
print(count)
for key,value in count.items():
    print(f"{key}:{value}")

text = "banana"
count ={}
for i in text:
    if i not in count:
        count[i] = 1
    else:
        count[i]+=1
print(count)
for key,value in count.items():
    print(f"{key}:{value}")

students = {
    "Bao": 8.5,
    "An": 7.0,
    "Minh": 9.0
}
for key,value in students.items():
    if value >= 8.0:
        print(f"{key}:{value}")

print(students["An"])
students["An"] = 8.0
print(students["An"])

students["Lan"] = 8.0
students["An"] = 8.5
for key,value in students.items():
    if value >= 8.0:
        print(f"{key}:{value}")
for key,value in students.items():
    print(f"{key}:{value}")
