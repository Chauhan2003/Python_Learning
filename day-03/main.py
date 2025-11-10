# String - It is a datatype that stores a sequence of characters.
str1 = "Gagan" # 'G' + 'a' + 'g' + 'a' + 'n'
str2 = 'Gagan'
str3 = """Gagan"""
str4 = '''Gagan'''

print(str1)
print(str2)
print(str3)
print(str4)

# Escape sequence character - It is a combination of a backslash (\) followed by one or more characters that has a special meaning inside a string.
# \' - \" - \n -\t
str5 = "This is a \"String\". \nWe can create it in \tpython."
print(str5)

# Concatenation - To add 2 string.
firstName = "Gagan"
lastName = "Chauhan"
print(firstName + lastName) # GaganChauhan
# print(firstName - lastName) - Error

# Length function - Find the length of string.
print(len(firstName)) # 5

# Indexing - We can only access the character of string can't manipulate.
str6 = "Hello World"
print(str6[6]) # W - Character at index 6

# Slicing - Accessing parts of a string.
print(str6[3:9])
print(str6[2:])
print(str6[-2]) # l - from backward

# String functions
print(str6.endswith("ld")) # True
print(str6.capitalize())
print(str6.replace("Hello", "Hii")) # Hii World
print(str6.find("W")) # 6 - index
print(str6.count("l")) # 3