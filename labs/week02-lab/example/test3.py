# Shopping Calculator Template

item_price = float(input("Enter item price: "))

quantity = int(input("Enter quantity: "))
cost_item = item_price * quantity

discount_percent = float(input("Enter discount %: "))
discount = discount_percent / 100 * cost_item
price = cost_item - discount
tax_percent = float(input("Enter tax %: "))
tax = price * (tax_percent / 100)

total_price = price + tax

# TODO: Calculate subtotal #ราคาเต็มเท่าไหร่
print(f"Subtotal = {item_price}")
# TODO: Calculate discount amount #ได้ส่วนลดเท่าไหร่
print(f"discount = {discount}")
# TODO: Calculate price after discount #ราคาหลังลด
print(f"Price after discount = {price}")
# TODO: Calculate tax amount #ราคาภาษี
print(f"Tax amount = {tax}")
# TODO: Calculate final total #สรุปราคาที่ต้องจ่าย
print(f"Final total = {total_price}")
# TODO: Display itemized receipt #แสดงออกมาจากทางหน้าจอ


