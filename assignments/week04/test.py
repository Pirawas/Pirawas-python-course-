# รับชื่อจริง(หรือข้อความ) จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว (a, e, i, o, u)
#โดยต้องใช้ loop-for ด้วยเท่านั้น

#ตัวอย่างหน้าจอ
# What is your name?: Booncho
# Your text have 4 vowels.

name = str(input("Enter your name: "))
vowels = 0
letters = list(name)
print(letters)
for letters in name:
    if letters == "a" or letters == "A":
        vowels += 1
    elif letters == "e" or letters == "E":
        vowels += 1
    elif letters == "i" or letters == "I":
        vowels += 1
    elif letters == "o" or letters == "O":
        vowels += 1
    elif letters == "u" or letters == "U":
        vowels += 1
print(vowels)