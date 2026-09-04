
'''# Converting string to number
apple = input("Enter a number: ")
try:
    x = int(apple) - 10
    print(f"Result: {x}")
except ValueError:
    print("Please enter a valid number!")
    '''
'''print("\n=== TRAVERSING STRINGS ===")
message = "hello"
index = 0

print("Method 1: Using for loop with enumerate")
for i, char in enumerate(message):
    print(f"message[{i}] = {char}")
    '''
str1 = 'Hello'
str2 = 'World!'

'''# Concatenation
result = str1 + str2
print(f"str1 + str2 = {result}")
# Multiplication
repeat = str1 * 3
print(f"str1 * 3 = {repeat}")
'''
'''#1 รับค่า text จากผู้ใช้
#2 รับค่าอักชระที่ต้องการค้นหาจากผู้ใช้
#3 แดสงผลจำนวนอักขระในข้อความ text

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Enter your Name Letters: ")
char_find = str(input("Character to find: "))

for letter in text:
    if letter == char_find:
        count += 1
print(f"{count} letters found in '{char_find}'")
'''
'''print("\n=== MEMBERSHIP TEST ===")
print("'a' in 'program':", 'a' in 'program')
print("'at' not in 'battle':", 'at' not in 'battle') 
'''

password = print("Insert your Password: ")
for i in password:
    if len(password) > 8:
        if password == '@'
        word = password.spilt('@')




