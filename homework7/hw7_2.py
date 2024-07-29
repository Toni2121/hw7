str1 = "  fun-day  "
print(str1.strip())

str2 = "hello"
print(f"str hello contains only letters: {str2.isalpha()}")

str3 = "777"
print(f"str 777 contains only numbers: {str3.isdigit()}")

str3 = " "
print(f"str   contains only spaces: {str3.isspace()}")

list1: list[str] = ['N', 'I', 'N', 'J', 'A']
str4: str = "".join(list1)
print(str4.replace("", "*"))

str5 = "hELLo"
print("e".lower() in str5.lower())

str6 = input("please enter a string: ")
comp = [char for char in str6.upper() if char.isalpha()]
print(comp)