print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

second = int(input("Enter your seconds: "))
hour = second // 3600
sec_remain = second % 3600
minute = sec_remain // 60
sec_remain = second % 60



print(f"{second} seconds = {hour} hour, {minute} minute, {sec_remain} second")